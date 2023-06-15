Created: 2023-02-15 15:47
#note

A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

So if you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.

You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.

Create a stored procedure:
```sql
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
```
Execute a stored procedure:
```sql
EXEC procedure_name;
```

Example of stored procedure with parameter:
```sql
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30)
AS
SELECT * FROM Customers WHERE City = @City
GO;
```
```sql
EXEC SelectAllCustomers @City = 'London';
```

#### Tags
#sql