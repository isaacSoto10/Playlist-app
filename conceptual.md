### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
## It is An open source Relational Database.
- What is the difference between SQL and PostgreSQL?
## They are both use as a Relational Database, but the diferrence is that PSQL have certain extra functionalities that are not in SQL. But the most important is: SQL is not open source.
- In `psql`, how do you connect to a database?
## you connect to a datbase using the next command: PSQL (Name of the database)
- What is the difference between `HAVING` and `WHERE`?
## The fundamental difference between WHERE and HAVING is this: WHERE selects input rows before groups and aggregates are computed (thus, it controls which rows go into the aggregate computation), whereas HAVING selects group rows after groups and aggregates are computed.
- What is the difference between an `INNER` and `OUTER` join?
## inner joins result in the intersection of two tables, whereas outer joins result in the union of two tables

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
## The key difference between a left outer join, and a right outer join is that in a left outer join it's the table in the FROM clause whose all rows are returned. Whereas, in a right outer join we are returning all rows from the table specified in the join clause.

- What is an ORM? What do they do?
## Object Relational Mapper: Are libraries that automates the transfer of data stored in databases into more comminy used in application Code

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
##  It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.
- What is CSRF? What is the purpose of the CSRF token?
## Cross-Site Request Forgery and it is used  to prevent CSRF attacks by making it impossible for an attaker to construck a valid HTTP request suitable for feeding to a victim user
- What is the purpose of `form.hidden_tag()`?
- ## The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. 
