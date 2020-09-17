# Index path traversal

## Exploitation

When testing the homepage, if we click on a link, for exemple `signin`, we can see how the application redirect the pages. It using a get parameter `page`. We can try to get another file on the server with `..`

For exemple `/etc/passwd`

`http://192.168.1.48/index.php?page=../../../../../../../etc/passwd`

It works!

## How to fix it?

- Don't use a parameter to get the next page but use a router on the backend
- On Apache, we can disabling listing directories by disabling the module mod_autoindex
- On Apache, we can also disabling listing for specific directories with specific rules on the VirtualHost

Exemple for VirtualHost:

```
<Directory /var/www/blabla/.hidden>
    Options -Indexes
</Directory>
```

https://www.simplified.guide/apache/disable-directory-listing
