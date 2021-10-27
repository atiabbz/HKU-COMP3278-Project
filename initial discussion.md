# breakdown

## GUI

### Screens

1. Login with face recognition + password
2. Summary (name, login time, ...)
    1. list of accounts -- account numbers, balances... (links)
        1. on click: see detailed transactions for that account
    2. 10 most recent transactions from all accounts with a link to see all transactions at the bottom
3. Logout

### cReAtiVitY

1. ability to hide balance
2. currency conversion
3. filters for transactions lists (by date, type, ...)
4. changing login info
5. pie charts

## Database

### Attributes

- Customer
  - customerId
  - name (first, last)
  - password
  - email
  - phone
  - birthday

- Account
  - accountId
  - balance
  - currency

- Transaction
  - transactionId
  - type (grocery, food, ...)
  - from
  - to
  - date/time
  - amount
  - remarks

- linkCustomerAccount
  - customerId
  - accountId

- linkAccountTransaction
  - accountId
  - transactionId

- securityQuestions
  - customerId
  - question
  - answer

- Login
  - customerId
  - loginTime

### ideas

1. security questions
2. password random characters
3. scheduled transactions

GUI Screens

1. Oscar
2. Ingrid

Connecting frontend and backend
figure out how the face recognition would work on webpage
figure out how to do query and entry into db

1. Atiab

Database design

1. Marsha
2. Justin