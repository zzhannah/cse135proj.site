#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os, sys
# s=requests.Session()
# setCookieUrl = 'https://cse135proj.site/cookies/set'
# getCookieUrl = 'https://cse135proj.site/cookies'
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Python Session Page 1</title>"
print "</head>"
print "<body>"
print "<h1 align='center'>Python Session Page 1</h1><hr>"

POST={}
args=sys.stdin.read().split('&')

for arg in args: 
    t=arg.split('=')
    if len(t)>1: k, v=arg.split('='); POST[k]=v


print "<p><b>Name: </b>", POST['name'], "</p>"

print "<a href='/php-cgiform.html>CGI Form</a><br />"
print "<a href='/cgi-bin/php-sessions-2.php'>Session Page 2</a><br />"
print "<form style='margin-top:30px' action='/cgi-bin/php-destroy-session.php' method='get'>"
print "<button type='submit'>Destroy Session</button>"
print "</form>"
print "</body>"
print "</html>"
