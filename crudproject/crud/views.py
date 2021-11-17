from django.db.backends.utils import CursorDebugWrapper
from django.http.request import QueryDict
from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from mysql.connector import connect
import json
from datetime import datetime
from dateutil import parser

from django.db import connection

import sys

sys.path.append("FaceRecognition")
import faces
import face_capture
import train


# Create your views here.
def index(request):
    return render(request, "crud/login.html")


def facial(request):
    name = faces.main()
    if name:
        return redirect(reverse("home") + f"?username={name.capitalize()}")
    else:
        return render(request, "crud/error.html")


def login(request):
    body = json.loads(request.body)
    username = body["username"]
    password = body["password"]
    print(username, password)
    with connection.cursor() as cursor:
        cursor.execute(
            "select * from login_info where username=%s and password=%s",
            [username, password],
        )
        results = {"results": dictfetchall(cursor)}
        print(results)
        if results["results"]:
            print("ok")
            return JsonResponse({"login": True})
        else:
            print("not ok")
            return JsonResponse({"login": False})


def home(request):
    username = request.GET.get("username")
    results = {}
    with connection.cursor() as cursor:
        query = "INSERT INTO login_details (username, login_datetime)  VALUES (%s, %s);"
        cursor.execute(query, [username, str(datetime.now())])
        query = "SELECT * FROM login_details where username=%s order by login_datetime desc;"
        cursor.execute(query, [username])
        results["login_details"] = dictfetchall(cursor)
        print(results["login_details"])
    with connection.cursor() as cursor:
        query = "select a.account_id, a.account_name, a.balance, a.currency_iso, a.actype FROM account a, login_info l, customer c WHERE l.customer_id = c.customer_id AND a.customer_id = c.customer_id AND l.username = %s"
        cursor.execute(query, [username])
        results["accounts"] = dictfetchall(cursor)
    return render(
        request,
        "crud/home.html",
        {
            "username": username,
            "accounts": results["accounts"],
            "login_details": results["login_details"],
        },
    )


def logout(request):
    return redirect("index")


def transactions(request):
    username = request.GET.get("username")
    account = request.GET.get("account")

    minTime = request.GET.get("minTime")
    maxTime = request.GET.get("maxTime")
    minAmount = request.GET.get("minAmount")
    maxAmount = request.GET.get("maxAmount")
    # print(minTime, maxTime, minAmount, maxAmount)
    results = {}
    with connection.cursor() as cursor:
        if account == "all":
            query = "SELECT t.trans_id, t.amount, t.trans_datetime, t.type, t.from_account, t.to_account FROM transaction t WHERE t.from_account IN (SELECT a.account_id FROM account a, customer c, login_info l WHERE a.customer_id = c.customer_id AND l.customer_id = c.customer_id AND l.username = %s) OR t.to_account IN (SELECT a.account_id FROM account a, customer c, login_info l WHERE a.customer_id = c.customer_id AND l.customer_id = c.customer_id AND l.username = %s)"
            cursor.execute(query, [username, username])
        else:
            query = "SELECT DISTINCT t.trans_id, t.amount, t.trans_datetime, t.type, t.from_account, t.to_account FROM transaction t, account a WHERE (t.from_account = a.account_id OR t.to_account = a.account_id) AND (t.from_account = %s OR t.to_account = %s)"
            cursor.execute(query, [account, account])
        if minTime and maxTime and minAmount and maxAmount:
            print("hello")
            print(minTime, maxTime, minAmount, maxAmount)
            query = "SELECT * from transaction t WHERE t.amount BETWEEN %s AND %s AND t.trans_datetime between %s and %s ORDER BY DATE(t.trans_datetime) desc"
            cursor.execute(query, [minAmount, maxAmount, minTime, maxTime])
        results["transactions"] = dictfetchall(cursor)
        print(results["transactions"])
    return render(
        request,
        "crud/transactions.html",
        {"transactions": results["transactions"], "username": username},
    )


def transfer(request):
    results = {}
    username = request.GET.get("username")
    fromAcc = request.GET.get("fromAcc")
    toAcc = request.GET.get("toAcc")
    amount = request.GET.get("amount")
    with connection.cursor() as cursor:
        query = "SELECT MAX(t.trans_id) as baseId from transaction t ORDER BY t.trans_id desc;"
        cursor.execute(query)
        newTransId = int(dictfetchall(cursor)[0]["baseId"]) + 1
        # print(newTransId)
        query = "INSERT INTO transaction (trans_id, amount, trans_datetime, type, from_account, to_account) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(
            query, [newTransId, amount, str(datetime.now()), "bill", fromAcc, toAcc]
        )

        query = "UPDATE account a INNER JOIN transaction t ON a.account_id = t.from_account SET a.balance = a.balance - t.amount WHERE t.from_account = %s AND t.trans_id = %s;"
        cursor.execute(query, [fromAcc, newTransId])

        query = "UPDATE account a INNER JOIN transaction t ON a.account_id = t.to_account SET a.balance = a.balance + t.amount WHERE t.to_account = %s AND t.trans_id = %s;"
        cursor.execute(query, [toAcc, newTransId])
    return redirect(reverse("home") + f"?username={username}")


def history(request):
    username = request.GET.get("username")
    results = {}
    with connection.cursor() as cursor:
        query = "SELECT * FROM login_details where username=%s order by login_datetime desc;"
        cursor.execute(query, [username])
        results["login_details"] = dictfetchall(cursor)
    return render(
        request,
        "crud/history.html",
        {"login_details": results["login_details"], "username": username},
    )


def settings(request):
    username = request.GET.get("username")
    results = {}
    with connection.cursor() as cursor:
        query = "SELECT c.customer_id, c.phone, c.email, c.name_first, c.name_middle, c.name_last, c.date_of_birth FROM customer c, login_info l WHERE c.customer_id = l.customer_id AND l.username = %s;"
        cursor.execute(query, [username])
        results["details"] = dictfetchall(cursor)
        query = "SELECT s.ques FROM security_ques s, login_has_sec lo WHERE lo.ques_id = s.ques_id AND lo.username = %s;"
        cursor.execute(query, [username])
        results["question"] = dictfetchall(cursor)
        print(results["question"])
    return render(
        request,
        "crud/settings.html",
        {
            "details": results["details"][0],
            "question": results["question"][0],
            "username": username,
        },
    )


def updateDetails(request):
    newPhone = request.GET.get("newPhone")
    newEmail = request.GET.get("newEmail")
    newPass = request.GET.get("newPass")
    question = request.GET.get("question")
    customerId = request.GET.get("customerId")
    username = request.GET.get("username")
    with connection.cursor() as cursor:
        if newPhone:
            query = "UPDATE customer c SET c.phone = %s WHERE c.customer_id = %s"
            cursor.execute(query, [newPhone, customerId])
        if newEmail:
            query = "UPDATE customer c SET c.email = %s WHERE c.customer_id = %s"
            cursor.execute(query, [newEmail, customerId])
        if newPass:
            query = "UPDATE login_info li INNER JOIN customer c ON li.customer_id = c.customer_id INNER JOIN login_has_sec ls ON li.username = ls.username SET li.password = %s WHERE ls.ques_ans = %s"
            cursor.execute(query, [newPass, question])
    return redirect(reverse("settings") + f"?username={username}")


def error(request):
    return render(request, "crud/error.html")


def retrain(request):
    face_capture.main()
    train.main()
    return redirect("index")


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
