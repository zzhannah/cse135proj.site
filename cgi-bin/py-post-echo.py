#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os, requests, sys

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>POST Message Body</title>"
print "</head>"
print "<body>"
print "<h1>POST Message Body</h1>"
POST={}
args = sys.stdin.read().split('&')
print args
print "<p>Message Body: </p>"
print "</body>"
print "</html>"
