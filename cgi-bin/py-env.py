#!/usr/bin/env python
import os

print "Content-type: text/html"
print "Cache-Control: no-cache"
print

print "<HTML><HEAD><TITLE>Environment Variables</TITLE></HEAD><BODY><H1>Environment Variables</H1>"

for headername, headervalue in os.environ.iteritems():
   print "<p>{0} = {1}</p>".format(headername, headervalue)

print "</BODY></HTML>" 
