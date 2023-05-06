Created: 2023-02-15 12:23
#note

A *JOIN* clause is used to combine rows from two or more tables, based on a related column between them. Example:
```sql
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrdersDate
FROM Orders JOIN Customers ON Orders.CstomersID=Customers.CustomerID
```

There are different types of the JOINs in SQL:
-   *(INNER) JOIN*: Returns records that have matching values in both tables;
-   *LEFT (OUTER) JOIN*: Returns all records from the left table, and the matched records from the right table;
-   *RIGHT (OUTER) JOIN*: Returns all records from the right table, and the matched records from the left table;
-   *FULL (OUTER) JOIN*: Returns all records when there is a match in either left or right table.

![[sql-joins.jpg]]

**Implicit JOIN**: the join's condition is specified in the WHERE clause.
```sql
SELECT *
FROM table1, table2
WHERE table1.columns = table2.column
```
**Explicit JOIN**: this is the *INNER JOIN*, where we define the condition in the FROM clause.
```sql
SELECT *
FROM table1 JOIN table2 ON table1.column=table2.column
```

## INNER JOIN 
It selects records that have matching values in both tables.

**Note:** The *INNER JOIN* keyword selects all rows from both tables as long as there is a match between the columns. If there are records in the one table that do not have matches in the other one, these records will not be shown!

## LEFT JOIN
It returns all records from the left table, and the matching records from the right one. 

**Note:** The *LEFT JOIN* keyword returns all records from the left table, even if there are no matches in the right table.

## RIGHT JOIN
It returns all records from the right table, and the matching records from the left table.

**Note:** The *RIGHT JOIN* keyword returns all records from the right table, even if there are no matches in the left table.

## FULL OUTER JOIN
It returns all records when there is a match in the left or right table records.

**Note:** The *FULL OUTER JOIN* keyword returns all matching records from both tables, whether the other table matches or not. So, if there are rows in the first table that do not have matches in the other table, or if there are rows in the second table that do not have matches in the first one, those rows will be listed as well.

## SELF JOIN
It is a regular *JOIN*, but we are joining a table with itself. 

#### Tags
#sql