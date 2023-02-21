Created: 2023-02-15 11:34
#note

## INTRO
A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data..

Most of the actions made on a database are done with SQL statement.

**NOTE:** SQL keywords are not case-sensitive, i.e. *select* is the same as *SELECT*.

In some database systems, a semicolon at the end of each SQL statement is required.


## SELECT
It is used to select data from a database. We can specify which columns to return or return all the fields using '\*'.

We can use *SELECT DISTINCT* statement to return only distinct values, i.e. the database contain many duplicates and we are not interested in them. 

*SELECT TOP* clause is used to specify the number of records o return. Some databases use the *LIMIT* clause to do the same thing.

**SELECT INTO**: it copies data from one table into a new one.
```sql
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```

## WHERE
It is used to filter records, that means that by using a specified condition, we can extract only those records that fulfill such statement.

The operators are the usual ones: *=,>,<,>=,<=,<>(or !=)*, plus some others like *BETWEEN, LIKE, IN*.

Several *WHERE* clauses can be combined with *AND, OR, NOT* operators.

## ORDER BY
It is used to sort the result-set in ascending (*ASC*) or descending (*DESC*) order (by default in ascending).
We can specify several columns to sort by, in that case we sort according to the first specified column and the according to the second. 

## INSERT INTO
It is used to insert new records in a table.
It is possible to write the *INSERT INTO* statement in two ways:
1. Specify both the column names and the values to be inserted:```
INSERT INTO _table_name_ (_column1_, _column2_, _column3_, ...)  VALUES (_value1_, _value2_, _value3_, ...);```
2. If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the *INSERT INTO* syntax would be as follows: `INSERT INTO _table_name_  VALUES (_value1_, _value2_, _value3_, ...);`

It is also possible to only insert data in specific columns.

With *INSERT INTO SELECT* statement, we can copy data from one table and insert it into another one. Example (insert all data from table1 in table2):
```sql
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
```

## NULL value
A field with a *NULL* value is a field with no value.

To check for *NULL* values, we can use the following operators: *IS NULL* and *IS NOT NULL*.

## UPDATE
It is used to modify the existing records in a table.
```sql
UPDATE table_name
SET column1 = value1, column2 = value2,...
WHERE condition;
```

It is the *WHERE* clause that determines how many records will be updated.

**NOTE:** If you omit the *WHERE* clause, ALL records will be updated!

## DELETE
It is used to delete (extraordinary, I know...) existing records in a table.
```sql
DELETE FROM table_name
WHERE condition
```

## MIN() and MAX()
They return the min/max value of the selected column.
```sql
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```

## COUNT()
It returns the number of rows that matches a specified criterion.
```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

## AVG()
It returns the average value of a numeric column.
```sql
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

## SUM()
It returns the total sum of a numeric column.
```sql
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

## LIKE
It is used in a *WHERE* operator to search for a specified pattern in a column.
There are two wildcards often used in conjunction with the *LIKE* operator:
-    The percent sign (%) represents zero, one, or multiple characters;
-    The underscore sign (\_) represents one, single character
Examples:
- WHERE CustomerName LIKE 'a%' ⇾ Finds any values that start with "a"
- WHERE CustomerName LIKE '\_r%' ⇾ Finds any values that have "r" in the second position

## IN
It allows specifying multiple values in a *WHERE* clause. It is a shorthand for multiple *OR* conditions. Example:
```sql
SELECT * 
FROM Customers
WHERE Country IN ("Germany", "France", "Uk");
```

## BETWEEN
It selects values within a range. Values can be numbers, texts, or dates.
This operator is inclusive: begin and end values are included.

## Aliases
*SQL Aliases* are used to give a table, or a column in a table, a temporary name. They are often used to make names more readable.
An alias only exists for the duration of that query.
```sql
SELECT column_name AS alias_name
FROM table_name;
```

## JOIN
An [[SQL JOIN]] clause is used to combine rows from two or more tables, based on a related column between them.

## UNION
It is used to combine the result-set of two or more *SELECT* statement.
-   Every *SELECT* statement within *UNION* must have the same number of columns
-   The columns must also have similar data types
-   The columns in every *SELECT* statement must also be in the same order

To allow duplicates, use *UNION ALL*.

## GROUP BY
This statement groups rows that have the same value into summary rows. It is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns. Example:
```sql
SELECT COUNT(column1), column2
FROM table
GROUP BY column2;
```
## HAVING
It is a *WHERE* statement that is used with aggregate functions.
```sql
SELECT COUNT(column1), column2
FROM table
GROUP BY column2
HAVING COUNT(column1)>3;
```
## EXISTS
It is used to test for the existence of any record in a subquery. It returns True is the subquery returns one or more records.

## ANY and ALL
It allows to compare single column value with  range of other values. Example:
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
	(SELECT column_name
	FROM table_name
	WHERE condition);
```
where *operator* is a standard comparison operator.

## CASE Expression
The `CASE` expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement). So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the `ELSE` clause.

If there is no `ELSE` part and no conditions are true, it returns NULL.
```sql
CASE
	WHEN condition1 THEN result1
	WHEN condition2 THEN result2
	WHEN condition3 THEN result3
	ELSE result
END;
```

## Comments
Single line comments start with '--'.
Multi-line comments start with '/*' and end with '\*/'.

## Operators
They are more or less the ones used also in other contexts.
Overview [here](https://www.w3schools.com/sql/sql_operators.asp).

## CREATE
To create a new database:
```sql
CREATE DATABASE databasename;
```

To create a new table in a database:
```sql
CREATE TABLE table_name (
	column1 datatype,
	column2 datatype,
	column3 datatype,
	....
);
```
The column parameters specify the names of the columns of the table.
The datatype parameter specifies the type of data the column can hold (e.g. varchar, integer, date, etc.).
For an overview f the available data types, see [here](https://www.w3schools.com/sql/sql_datatypes.asp).

We can create a copy of an existing table using *CREATE TABLE*:
```sql
CREATE TABLE new_table AS
	SELECT column1, column2,...
	FROM existing_table_name
	WHERE ...;
```

## DROP
To drop an existing SQL database:
```sql
DROP DATABASE databasename;
```

To drop an existing table in a database:
```sql
DROP TABLE table_name;
```

## TRUNCATE
It is used to delete the data inside a table, but not the table itself:
```sql
TRUNCATE TABLE table_name;
```

## ALTER 
The *ALTER TABLE* statement is used to add, delete, or modify columns in an existing table.
The *ALTER TABLE* statement is also used to add and drop various constraints on an existing table.
```sql
ALTER TABLE table_name
ADD column_name datatype;
```
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```
```sql
ALTER TABLE table_name
RENAME COLUMN old_name to new_name;
```
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

#### Tags
#sql