-- CREATE DATABASE `group7project`;
-- USE `group7project`;

CREATE TABLE customer (
  customer_id VARCHAR(50) NOT NULL PRIMARY KEY,
  name_first VARCHAR(50) NOT NULL,
  name_middle VARCHAR(50),
  name_last VARCHAR(50) NOT NULL,
  date_of_birth date NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE account (
  account_id VARCHAR(50) NOT NULL PRIMARY KEY,
  customer_id VARCHAR(50) NOT NULL,
  account_name VARCHAR(100) NOT NULL,
  balance INT NOT NULL, -- in terms of CENTS with 2 dec places (E.G. $100.45 will be 10045)
  currency_iso VARCHAR(5) NOT NULL,
  actype VARCHAR(255) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

CREATE TABLE transaction (
  trans_id VARCHAR(50) NOT NULL PRIMARY KEY,
  amount INT NOT NULL, -- in terms of CENTS with 2 dec places (E.G. $100.45 will be 10045)
  trans_datetime TIMESTAMP NOT NULL,
  type VARCHAR(50) NOT NULL,
  from_account VARCHAR(50) NOT NULL,
  to_account VARCHAR(50) NOT NULL,
  FOREIGN KEY (from_account) REFERENCES account (account_id),
  FOREIGN KEY (to_account) REFERENCES account (account_id)
);

CREATE TABLE transactionremarks (
  trans_id VARCHAR(50) NOT NULL,
  remarks VARCHAR(500),
  PRIMARY KEY (trans_id, remarks),
  FOREIGN KEY (trans_id) REFERENCES transaction (trans_id)
);

CREATE TABLE security_ques (
  ques_id INT NOT NULL PRIMARY KEY,
  ques VARCHAR(255) NOT NULL
);

CREATE TABLE login_info (
  username VARCHAR(50) NOT NULL PRIMARY KEY,
  customer_id VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

CREATE TABLE login_has_sec (
  username VARCHAR(50) NOT NULL,
  ques_id INT NOT NULL,
  ques_ans VARCHAR(100) NOT NULL,
  PRIMARY KEY (username, ques_id),
  FOREIGN KEY (username) REFERENCES login_info (username),
  FOREIGN KEY (ques_id) REFERENCES security_ques (ques_id)
);

CREATE TABLE login_details (
  username VARCHAR(50) NOT NULL,
  login_datetime TIMESTAMP NOT NULL,
  PRIMARY KEY (username, login_datetime),
  FOREIGN KEY (username) REFERENCES login_info (username)
);