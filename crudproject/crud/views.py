from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from mysql.connector import connect
from .wazup import wazup

from django.db import connection

import sys

sys.path.append("FaceRecognition")
import faces


# Create your views here.
def index(request):
    return render(request, "crud/index.html")


def js_on(request):
    # query database
    # get results
    # create dictionary
    return JsonResponse({"foo": "bar"})


def login(request):
    # if faces.main():
    #     return render(request, "crud/logged.html")
    # else:
    #     return HttpResponse("LOL FUCK U")
    return render(request, "crud/login.html")


def landing(request):
    return render(request, "crud/landing.html")


def notes(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from notes;")
        results = {"results": dictfetchall(cursor)}
        print(results)
    return render(request, "crud/notes.html", results)


def create(request):
    content = request.POST["new_note"]
    with connection.cursor() as cursor:
        cursor.execute("insert into notes (content) values (%s);", [content])
    return redirect("notes")


def update(request):
    updated_note = request.POST["updated_note"]
    note_id = int(request.POST["note_id"])
    with connection.cursor() as cursor:
        cursor.execute(
            f"update notes set content=%s where note_id={note_id};", [updated_note]
        )
    return redirect("notes")


def delete(request):
    body = request.GET
    note_id = body["note_id"]
    with connection.cursor() as cursor:
        cursor.execute("delete from notes where note_id=%s;", [note_id])
    return redirect("notes")


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def layout(request):
    return render(request, "crud/layout.html")
