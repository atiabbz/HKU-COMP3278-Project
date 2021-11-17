# Group Project

> **Deadline: 11:59PM - 17 November, 2021**

## Preparing Database

1. Run ```sqltables.sql``` file to create the tables.
2. Run ```sqldata.sql``` to populate tables with placeholder data.
3. Open ```./crudproject/mysql_option_file.cnf``` and change ```user``` and ```password``` field values according to credentials of local installation of MySQL.

## Running Server

0. Mac: ```brew install mysql``` (from a group member's experience)
1. Make sure terminal is at repository root.
2. Create virtual Python environment: ```python -m venv env```
   1. (```python3``` instead sometimes on Mac)
3. Activate the environment -- Windows: ```env/Scripts/Activate``` | Mac: ```source env/bin/activate```
4. Install all the required packages: ```python -m pip install -r requirements.txt```
5. cd into server project: ```cd crudproject```
6. Start the server: ```python manage.py runserver```

## Facial Recognition Training

1. While the server is running go to <http://127.0.0.1:8000/train> on a browser.
2. The face capture script should start running.
3. Wait until training is complete.
4. The browser should be redirected to the login page now.

## Project Description

You are invited to develop an **Intelligent Know Your Customer (iKYC)** system with **facial ID login function**.

You need to implement

- A Graphical User Interface (GUI)
- A database

to meet the below requirements.

## Requirements

- When a customer login with their face ID, their information *(such as)*
  - Name
  - Login time
  - Login history
  - Customized welcome message

  will be presented in the GUI.

- The customer can view their account information *(such as)*
  - A list of accounts (e.g. savings, current, HKD, USD, etc.)
  - Account numbers
  - Balances, etc.

- The customer can click the account to
  - See detailed transactions
  - Search the transactions based on
    - Month
    - Day
    - Time
    - Amount

- The transactions can be presented in the GUI. **`(???)`**

## Further Information

- **Group**: 1-5 students as a group.
- **GUI**: Each group may design GUI based on the understanding of the above user requirement -- *Make your own design choice*.
- **Database**: Your database should have at least **five** tables.
  <!-- from Sep 9 Tutorial page 2 -->
  - Customer
  - Account
  - Transaction
  - linkCustomerAccount
  - linkAccountTransaction
  - *... Make your own table design choices*

## Development Tools

- **Face Recognition**: Python + OpenCV *(full code provided)*
- **GUI**: PySimpleGUI / HTML *TODO*
- **Database**: Python + MySQL *(sample code provided)*
- Use of any other development packages is allowed, except that the DBMS must be MySQL.

## Assessment

- **20%** of final mark
  - Software development **[10%]**
    - Database implementation **[6%]**
    - GUI implementation **[4%]**
  - Presentation **[10%]** *(strict 2%-deduction for violating time/page limit)*
    - 5 minutes
    - 3 pages
      - Development plan
      - Milestones
      - **Contribution of each member**
      - **Video recording of demo**
      - Software design
      - Database design
        - **ER diagram**
        - **Tables**
      - Difficulties encountered
        - **and how they were solved**

- Live demo is allowed for stably working program

> **Bonus points**

- Creative GUI desgin
- Creative software functions
- Creative DB design
