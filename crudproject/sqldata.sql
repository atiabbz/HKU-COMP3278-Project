INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('131100', 'Alice', 'De', 'Lena', '2000-07-04', '91728365', 'aliceccabc@gmail.com');
INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('124320', 'Denise', 'El', 'Shaun', '1989-03-01', '53627184', 'denden1989ise@yahoo.com');
INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('137921', 'Ben', '', 'Ng', '1994-12-19', '67493810', 'bennyben149@gmail.com.hk');
INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('110172', 'Escanor', '', 'Ai', '2002-09-10', '90172836', 'car78esmeme@yahoo.com.hk');
INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('189463', 'Elizabeth', 'Rachel', 'Choi', '1998-06-24', '52638172', 'lizarachoi@qq.com');
INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('100001', 'Comp', '', 'UTA', '1993-08-22', '53648273', 'comphku@gmail.com');

INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, password) VALUES ('1772837468', '131100', 'Alice De LENA', '8789091', 'HKD', 'Anjyd_6291@jd');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, password) VALUES ('4966283918', '124320', 'Denise Fashion LTD', '172698', 'USD', 'Den_iseF@shion');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, password) VALUES ('2736154801', '137921', 'Ben Beauty COMPANY', '5362870', 'CAD', 'BenBEN1872TY');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, password) VALUES ('7182745279', '110172', 'Escanor AI', '16279836', 'RMB', 'EScaNOR7878');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, password) VALUES ('8172635409', '189463', 'Elizabeth Shipping Htd LTD', '1726389', 'HKD', 'Lizliz8_th');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, password) VALUES ('1000000001', '100001', 'Comp BANK', '10000000', 'HKD', 'Comp3278');

INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101000', '54687', '2019/08/01 15:00:03', 'transfer', '0', '1772837468', '8172635409');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101001', '728364', '2019/12/04 09:47:12', 'transfer', '3150', '4966283918', '1000000001');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101002', '435192', '2021/08/01 15:00:03', 'transfer', '0', '1772837468', '8172635409');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101003', '3000', '2021/08/02 16:10:23', 'bill', '0', '4966283918', '2736154801');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101004', '32000', '2021/08/03 06:00:00', 'wage', '100', '7182745279', '1000000001');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101005', '450', '2021/08/03 16:30:05', 'credit', '20', '2736154801', '1772837468');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101006', '800', '2021/08/04 12:00:00', 'interest', '0', '4966283918', '7182745279');

INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101000', 'Goods Shipping');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101001', 'Notes receivables');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101002', 'Delivery');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101003', 'Bill payment');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101004', 'Salary for August');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101005', 'Credit card payment');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101006', 'Stock Interest');

INSERT INTO security_ques (ques_id, ques) VALUES ('01', 'Where do you live in?');
INSERT INTO security_ques (ques_id, ques) VALUES ('02', 'What is the name of your first pet?');
INSERT INTO security_ques (ques_id, ques) VALUES ('03', 'What is your favourite food?');
INSERT INTO security_ques (ques_id, ques) VALUES ('04', 'Who are you?');

INSERT INTO login_info (username, customer_id, password)  VALUES ('Alice', '131100', 'Trying*001');
INSERT INTO login_info (username, customer_id, password)  VALUES ('Denise', '124320', 'admiN123');
INSERT INTO login_info (username, customer_id, password)  VALUES ('BenBeauty', '137921', 'Easy_pw001');
INSERT INTO login_info (username, customer_id, password)  VALUES ('Escanor', '110172', 'BORA@bora1');
INSERT INTO login_info (username, customer_id, password)  VALUES ('ElizabethShipping', '189463', '12Liz_ship');
INSERT INTO login_info (username, customer_id, password)  VALUES ('COMP BANK', '100001', 'comp3278_HKU');

INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('Alice', '01', 'HK');
INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('Denise', '01', 'Japan');
INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('BenBeauty', '02', 'None');
INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('Escanor', '03', 'Hotpot');
INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('ElizabethShipping', '04', 'Elizabeth Shopping');
INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('COMP BANK', '04', 'Greatest Bank Alive');

INSERT INTO login_details (username, login_datetime)  VALUES ('Alice', '2019/08/01 15:00:03');
INSERT INTO login_details (username, login_datetime)  VALUES ('Denise', '2019/08/01 15:00:03');
INSERT INTO login_details (username, login_datetime)  VALUES ('BenBeauty', '2019/08/01 15:00:03');
INSERT INTO login_details (username, login_datetime)  VALUES ('Escanor', '2019/08/01 15:00:03');
INSERT INTO login_details (username, login_datetime)  VALUES ('ElizabethShipping', '2019/08/01 15:00:03');
INSERT INTO login_details (username, login_datetime)  VALUES ('COMP BANK', '2019/08/01 15:00:03');