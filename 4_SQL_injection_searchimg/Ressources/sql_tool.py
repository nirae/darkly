#! /usr/bin/env python3

string = """/var/www/backdoor.php"""
result = ''
for i in string:
    result += "%s," % ord(i)
result = result[:-1]
print(result)

