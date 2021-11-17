# Group Project

> **Deadline: 11:59PM - 17 November, 2021**

## Preparing Database

1. Open MySQL Workbench and add a new MySQL Connection.
2. Set your own connection name, username and password.
3. Click into ```file``` then ```Open SQL Script```. Run ```sqltables.sql``` file to create the tables.
4. Click onto the ```group7project``` database, go to ```file``` and ```Open SQL Script```. Run ```sqldata.sql``` to populate tables with placeholder data.
5. Open ```./crudproject/mysql_option_file.cnf``` and change the ```user``` and ```password``` field values according to credentials of local installation of MySQL.

## Running Server

0. Mac: ```brew install mysql``` (from a group member's experience)
1. Make sure terminal is at repository root.
2. Create virtual Python environment: ```python -m venv env```
   1. (```python3``` instead sometimes on Mac)
3. Activate the environment -- Windows (**PowerShell**): ```env/Scripts/Activate``` | Mac: ```source env/bin/activate```
4. Install all the required packages: ```python -m pip install -r requirements.txt```
5. cd into server project: ```cd crudproject```
6. Start the server: ```python manage.py runserver```

### Helpful links

1. Python virtual environments: <https://realpython.com/python-virtual-environments-a-primer/>
2. Django servers: <https://docs.djangoproject.com/en/3.2/intro/tutorial01/#the-development-server>
3. Windows PowerShell script execution policy (Example 6): <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2#example-6--set-the-execution-policy-for-the-current-powershell-session>

## Facial Recognition Training

1. While the server is running go to <http://127.0.0.1:8000/train> on a new tab/browser.
2. The face capture script should start running. Please allow camera access to this tab/browser.
3. Patiently wait until the training is completed.
4. The browser should be redirected to the login page now.
5. You will be able to login by clicking on the face recognition login button. (Note: The speed of logging in differs in each system)

**Note**: We have noticed significant differences in facial recognition completion across a variety of hardware. Experimentation of confidence value in ```./crudproject/FaceRecognition/faces.py | line 63``` is advised.

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

- The transactions can be presented in the GUI.

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
