Created: 2023-02-16 13:05
#note

A view is a virtual table based on the result-set of an SQL statement.
You can add SQL statement and functions to a view and present the data if the data were coming from one single table.
```sql
CREATE VIEW view_name AS
SELECT column1, column2,...
FROM table_name
WHERE condition;
```

**Note:** A view always shows up-to-date data! The database engine recreates the view, every time a user queries it.

A view can be updated as follows:
```sql
CREATE OR REPLACE VIEW view_name AS
SELECT columns1, column2,...
FROM table_name
WHERE condition;
```

#### Tags
#sql