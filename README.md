# Darkly

> Résumé: Ce projet est une introduction à la sécurité en informatique dans le domainedu Web

>Lorsque vous développez vos premiers sites web, vous n’avez généralement pas lamoindre idée des vulnérabilités existantes dans le monde du web.Ce petit projet a pour but de combler ce manque : vous allez prendre conscience deces vulnérabilités en faisant un audit d’un site web simple. Ce site présente des faillesencore régulièrement présentes sur des sites que vous visitez tous les jours.Voici donc une grosse introduction aux vulnérabilités générales que l’on retrouve dansle monde du web.

## Research

Scan with **nmap**

```
$ nmap 192.168.1.48 -p -
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-17 13:29 CEST
Nmap scan report for BornToSecWeb.home (192.168.1.48)
Host is up (0.00014s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE
80/tcp   open  http
4242/tcp open  vrml-multi-use

Nmap done: 1 IP address (1 host up) scanned in 1.28 seconds
```

2 open ports:

- 80 -> http
- 4242 -> vrml-multi-use

Get all paths on the domain with **dirb**

```
$ dirb http://192.168.1.48 -r

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Thu Sep 17 11:30:48 2020
URL_BASE: http://192.168.1.48/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
OPTION: Not Recursive

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://192.168.1.48/ ----
==> DIRECTORY: http://192.168.1.48/admin/                                                                                                                                   
==> DIRECTORY: http://192.168.1.48/audio/                                                                                                                                   
==> DIRECTORY: http://192.16/.hidden8.1.48/css/                                                                                                                                     
==> DIRECTORY: http://192.168.1.48/errors/                                                                                                                                  
+ http://192.168.1.48/favicon.ico (CODE:200|SIZE:1406)                                                                                                                      
==> DIRECTORY: http://192.168.1.48/fonts/                                                                                                                                   
==> DIRECTORY: http://192.168.1.48/images/                                                                                                                                  
==> DIRECTORY: http://192.168.1.48/includes/                                                                                                                                
+ http://192.168.1.48/index.php (CODE:200|SIZE:6892)                                                                                                                        
==> DIRECTORY: http://192.168.1.48/js/                                                                                                                                      
we canSIZE:53)                                                                                                                         
==> DIRECTORY: http://192.168.1.48/whatever/                                                                                                                                
                                                                                                                                                                            
-----------------
END_TIME: Thu Sep 17 11:30:49 2020
DOWNLOADED: 4612 - FOUND: 3
```

Paths found on `http://192.168.1.48/`:

- http://192.168.1.48/admin/
- http://192.168.1.48/audio/
- http://192.168.1.48/css/
- http://192.168.1.48/errors/
- http://192.168.1.48/fonts/
- http://192.168.1.48/images/
- http://192.168.1.48/includes/
- http://192.168.1.48/index.php/
- http://192.168.1.48/js/
- http://192.168.1.48/robots.txt
- http://192.168.1.48/whatever/

Let's check the robots.txt

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

2 hidden paths:

- `/whatever`
- `/.hidden`

### /whatever + /admin

There is a file `htpasswd` with some credentials. We will use it to login in a htaccess on an other page?

Try it on `/admin`, doesn't work

The password was hashed in md5, crack it and we can log in!

### /.hidden

There is many folders and README files inside each. Let's crawl them to find the good README

The good is on the path `http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README`

###

### home - index.php

If we click on a link we are redirected with a php get parameter like this `http://192.168.1.48/index.php?page=signin`. We can use this to do a path traversal to get some files on the server.

`http://192.168.1.48/index.php?page=../../../../../../../etc/passwd`

### Unrestricted file upload

On the page `http://192.168.1.48/index.php?page=upload`

After some tests, we can just upload jpg files (not png). But we can upload other filetype by writing the request ourself

### SQL injection searchimg

Inejction SQL on the page `searchimg`

### SQL injection members

Inejction SQL on the page `member`

### 
