# User agent and referer Copyright

On the bottom of the home page, we can see the copyright `© BornToSec` is a link

```html
<ul class="copyright">
	<a href="?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c">
        <li>&copy; BornToSec</li>
    </a>
</ul>
```

This link to to the page `e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`

On this page, we can see on the source code a big html comment with some instructions

```
<!--
Voila un peu de lecture :

...

<!--
You must cumming from : "https://www.nsa.gov/" to go to the next step
-->

Let's use this browser : "ft_bornToSec". It will help you a lot.

...

```

We need to have as referer the webiste `https://www.nsa.gov/` and as user-agent `ft_bornToSec`

Let's do it with a python script

The headers need to be 

```py
headers = {
    'User-Agent': 'ft_bornToSec',
    'Referer': 'https://www.nsa.gov/'
}
```

```
$ ./exploit.py 
 The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

## How to fix it?

It's not really a vulnerability but it was on old webserver. There was some vulnerabilities to inject some code on the User-Agent or Referer.

In general, be careful if in the backend, you do something different for specific User-Agent or Referer, or others headers attributes. It can be modified by the client like cookies etc.

Never execute something with the content of headers attributes. Never trust the client
