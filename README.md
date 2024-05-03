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
    "database":"yourDatabaseNama",
    "username":"yourUsername",
    "password":"yourPassword",
    "driver":"psqlodbca.so"
} > config.json
```

```sql
CREATE DATABASE amazon;
```
