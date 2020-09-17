# Admin section

## Exploitation

On the `/whatever` page, there is a file named `htpasswd`.

Download it

```
$ wget http://192.168.1.48/whatever/htpasswd
```

There is some credentials

```
root:8621ffdbc5698829397d97767ac13db3
```

We know there is a `/admin` page, we can try to login on this page with these credentials

It doesn't work. The password seems to be a hash, so we can try to crack it with an online tool like crackstation.net

It works! The password is `dragon`

We can login on the `/admin` page with the couple `root`/`dragon`

Script it!

## How to fix it?

- An .htaccess on the directory
- Don't put passwords on a directory served by apache or an other webserver
- On Apache, we can disabling listing directories by disabling the module mod_autoindex
- On Apache, we can also disabling listing for specific directories with specific rules on the VirtualHost

Exemple for VirtualHost:

```
<Directory /var/www/blabla/whatever>
    Options -Indexes
</Directory>
```

https://www.simplified.guide/apache/disable-directory-listing
