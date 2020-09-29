# Open redirect

## Exploitation

On the bottom of the home page, there is some socials links (facebook, twitter...). When inspecting the source code, we can check how the redirection is made

```html
<ul class="icons">
	<li>
        <a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>
    </li>
	<li>
        <a href="index.php?page=redirect&site=twitter" class="icon fa-twitter"></a>
    </li>
    <li>
        <a href="index.php?page=redirect&site=instagram" class="icon fa-instagram"></a>
    </li>
</ul>
```

It using a page named `redirect` with a parameter `site`. Let's see what happens when we change the link to redirect to another page with an open redirect

Change the redirection parameter and click on the link

```html
<ul class="icons">
	<li>
        <a href="index.php?page=redirect&site=https://google.com" class="icon fa-facebook"></a>
    </li>
	<li>
        <a href="index.php?page=redirect&site=twitter" class="icon fa-twitter"></a>
    </li>
    <li>
        <a href="index.php?page=redirect&site=instagram" class="icon fa-instagram"></a>
    </li>
</ul>
```

We have the flag!

We can do it in a faster way with a manual request on the page redirect

```
$ ./exploit.py 
Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
```

## How to fix it?

Need to check the value of the parameters on the backend code.

On this case a check on the string `twitter` or whatever and if is different, don't do the redirection

## References

https://www.httpcs.com/fr/faille-open-redirect
