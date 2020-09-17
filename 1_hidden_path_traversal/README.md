# .hidden Path traversal

## Exploitation

On the `/.hidden` page, there is many folders with README files inside each

```
../
amcbevgondgcrloowluziypjdh/                        11-Sep-2001 21:21                   -
bnqupesbgvhbcwqhcuynjolwkm/                        11-Sep-2001 21:21                   -
ceicqljdddshxvnvdqzzjgddht/                        11-Sep-2001 21:21                   -
doxelitrqvhegnhlhrkdgfizgj/                        11-Sep-2001 21:21                   -
eipmnwhetmpbhiuesykfhxmyhr/                        11-Sep-2001 21:21                   -
ffpbexkomzbigheuwhbhbfzzrg/                        11-Sep-2001 21:21                   -
ghouhyooppsmaizbmjhtncsvfz/                        11-Sep-2001 21:21                   -
hwlayeghtcotqdigxuigvjufqn/                        11-Sep-2001 21:21                   -
isufpcgmngmrotmrjfjonpmkxu/                        11-Sep-2001 21:21                   -
jfiombdhvlwxrkmawgoruhbarp/                        11-Sep-2001 21:21                   -
kpibbgxjqnvrrcpczovjbvijmz/                        11-Sep-2001 21:21                   -
ldtafmsxvvydthtgflzhadiozs/                        11-Sep-2001 21:21                   -
mrucagbgcenowkjrlmmugvztuh/                        11-Sep-2001 21:21                   -
ntyrhxjbtndcpjevzurlekwsxt/                        11-Sep-2001 21:21                   -
oasstobmotwnezhscjjopenjxy/                        11-Sep-2001 21:21                   -
ppjxigqiakcrmqfhotnncfqnqg/                        11-Sep-2001 21:21                   -
qcwtnvtdfslnkvqvzhjsmsghfw/                        11-Sep-2001 21:21                   -
rlnoyduccpqxkvcfiqpdikfpvx/                        11-Sep-2001 21:21                   -
sdnfntbyirzllbpctnnoruyjjc/                        11-Sep-2001 21:21                   -
trwjgrgmfnzarxiiwvwalyvanm/                        11-Sep-2001 21:21                   -
urhkbrmupxbgdnntopklxskvom/                        11-Sep-2001 21:21                   -
viphietzoechsxwqacvpsodhaq/                        11-Sep-2001 21:21                   -
whtccjokayshttvxycsvykxcfm/                        11-Sep-2001 21:21                   -
xuwrcwjjrmndczfcrmwmhvkjnh/                        11-Sep-2001 21:21                   -
yjxemfsgdlkbvvtjiylhdoaqkn/                        11-Sep-2001 21:21                   -
zzfzjvjsupgzinctxeqtzzdzll/                        11-Sep-2001 21:21                   -
README                                             11-Sep-2001 21:21                  34
```

The README file does not contain the flag but we can assume the flag is on one of the directories. We can write a script to open all the possible links with the directories and check on the README file if there is the flag

We will do it with our script `exploit.py`. It's long but we have the flag!

```
...
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/iumzgolywwwsdqbunmlkagpfqu/README/
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/juavephzegfusfrqelvumphzat/
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/juavephzegfusfrqelvumphzat/README/
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/kbjjgbfcbchslgysntmtmcxzyr/
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/kbjjgbfcbchslgysntmtmcxzyr/README/
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/
process: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README/
Flag found!
Path: http://192.168.1.48/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
Try: 15693
The flag is:
99dde1d35d1fdd283924d84e6d9f1d820
```

The flag was on the path: `http://borntosecweb/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README`

## How to fix it?

- An .htaccess on the directory
- On Apache, we can disabling listing directories by disabling the module mod_autoindex
- On Apache, we can also disabling listing for specific directories with specific rules on the VirtualHost

Exemple for VirtualHost:

```
<Directory /var/www/blabla/.hidden>
    Options -Indexes
</Directory>
```

https://www.simplified.guide/apache/disable-directory-listing
