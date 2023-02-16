Created: 2023-02-16 13:02
#note

SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

Constraints can be column level or table level. Column level constraints apply to a column, and table level constraints apply to the whole table.

Constraints can be specified when the table is created with the *CREATE TABLE* statement, or after the table is created with the *ALTER TABLE* statement.
```sql
CREATE TABLE table_name (
	column1 datatype constraint,
	column2 datatype constraint,
	column3 datatype constraints,
	...
);
```

The following constraints are commonly used in SQL:

-   [NOT NULL](https://www.w3schools.com/sql/sql_notnull.asp)- Ensures that a column cannot have a NULL value
-   [UNIQUE](https://www.w3schools.com/sql/sql_unique.asp) - Ensures that all values in a column are different
-   [PRIMARY KEY](https://www.w3schools.com/sql/sql_primarykey.asp) - A combination of a *NOT NULL* and *UNIQUE*. Uniquely identifies each row in a table. A table can have just one primary key.
-   [FOREIGN KEY](https://www.w3schools.com/sql/sql_foreignkey.asp) - Prevents actions that would destroy links between tables. It consists in a field (or collection of fields) in one table that refers to the Primary Key in another table
-   [CHECK](https://www.w3schools.com/sql/sql_check.asp) - Ensures that the values in a column satisfies a specific condition
-   [DEFAULT](https://www.w3schools.com/sql/sql_default.asp) - Sets a default value for a column if no value is specified
-   [CREATE INDEX](https://www.w3schools.com/sql/sql_create_index.asp) - Used to create and retrieve data from the database very quickly

## NOT NULL

#### Tags
#sql