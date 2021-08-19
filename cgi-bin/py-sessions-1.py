#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os, sys
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

if POST['name']:
    session['name'] = POST['name']

if POST['name']:
    namme = POST['name']
else:
    namme = "You do not have a name set"

print "<p><b>Name: </b>", namme, "</p>"

print "<a href='/py-cgiform.html'>CGI Form</a><br>"
print "<a href='/cgi-bin/py-sessions-2.py'>Session Page 2</a><br>"
print "<a href='/cgi-bin/py-destroy-session.py'>Destroy Session</a>"
print "</form>"
print "</body>"
print "</html>"

