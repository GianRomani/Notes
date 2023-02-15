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

## INNER JOIN 
It selects records that have matching values in both tables.



#### Tags
#sql