# Amazon tech best sellers

## instalation in postgres:
```bash
sudo apt install odbc-postgresql
# source: https://medium.com/@murat.bilal/installing-and-configuring-ubuntu-odbc-drivers-for-postgresql-database-c67500e87ead
```

```bash
touch config.json
echo {
    "server":"localhost",
    "database":"yourDatabaseName",
    "username":"yourUsername",
    "password":"yourPassword",
    "driver":"YourPostgresDriverName"
} > config.json
```
- driver on ubuntu: psqlodbcw.so
- psqlodbca.so is getting error: https://github.com/mkleehammer/pyodbc/issues/169

```sql
CREATE DATABASE amazon;
```
