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

https://zestedesavoir.com/tutoriels/945/les-injections-sql-le-tutoriel/les-injections-sql-classiques/affichage-denregistrements/


