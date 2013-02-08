#!/bin/bash

user=vicfn
password=notarealpassword
echo "Password:"
read password

curl -s -c cookie -k -L https://website --data-urlencode "username=vicfn&password=passwd&cookie=1&sublogin=Login"
