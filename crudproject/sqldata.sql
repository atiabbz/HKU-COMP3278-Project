INSERT INTO customer (customer_id, name_first, name_middle, name_last, date_of_birth, phone, email) VALUES ('131100', 'Jack', '', 'Chan', '2000-07-04', '91728365', 'jackchan@gmail.com');

INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, actype) VALUES ('1772837550', '131100', 'Jack Chan Ltd', '8789091', 'HKD', 'HKD Savings');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, actype) VALUES ('1772837551', '131100', 'Jack Chan L', '1000293', 'HKD', 'HKD Current');
INSERT INTO account (account_id, customer_id, account_name, balance, currency_iso, actype) VALUES ('1772837552', '131100', 'Jack Chan Lt', '5648', 'USD', 'USD Savings');

INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101000', '54687', '2019-08-01 15:00:03', 'transfer', '0', '1772837550', '1772837551');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101001', '7283', '2019-12-04 09:47:12', 'transfer', '3150', '1772837551', '1772837552');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101002', '435192', '2021-08-01 15:00:03', 'transfer', '0', '1772837551', '1772837550');
INSERT INTO transaction (trans_id, amount, trans_datetime, type, charges, from_account, to_account) VALUES ('100000010101003', '3000', '2021-08-02 16:10:23', 'bill', '0', '1772837551', '1772837550');

INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101000', 'Goods Shipping');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101001', 'Notes receivables');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101002', 'Delivery');
INSERT INTO transactionremarks (trans_id, remarks) VALUES ('100000010101003', 'Bill payment');

INSERT INTO security_ques (ques_id, ques) VALUES ('01', 'Where do you live in?');
INSERT INTO security_ques (ques_id, ques) VALUES ('02', 'What is the name of your first pet?');
INSERT INTO security_ques (ques_id, ques) VALUES ('03', 'What is your favourite food?');
INSERT INTO security_ques (ques_id, ques) VALUES ('04', 'Who are you?');

INSERT INTO login_info (username, customer_id, password)  VALUES ('Jack', '131100', 'Try_001');

INSERT INTO login_has_sec (username, ques_id, ques_ans)  VALUES ('Jack', '01', 'HK');

INSERT INTO login_details (username, login_datetime)  VALUES ('Jack', '2019-08-01 15:00:03');
INSERT INTO login_details (username, login_datetime)  VALUES ('Jack', '2019-09-23 15:53:08');
INSERT INTO login_details (username, login_datetime)  VALUES ('Jack', '2020-07-14 12:34:13');
INSERT INTO login_details (username, login_datetime)  VALUES ('Jack', '2020-10-25 15:40:49');
INSERT INTO login_details (username, login_datetime)  VALUES ('Jack', '2021-01-09 14:02:14');
INSERT INTO login_details (username, login_datetime)  VALUES ('Jack', '2021-12-01 09:34:27');
