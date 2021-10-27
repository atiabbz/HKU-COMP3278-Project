# Group Project

> **Deadline: 11:59PM - 17 November, 2021**

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
