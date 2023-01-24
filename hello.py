#!/usr/bin/env python3

import os
import json

print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent=2)) 
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>") 

#Modify your CGI script to report the values of the query parameters in the HTML.
#print(f"<p>HTTP_USER_AGENT = {os.environ['QUERY_STRING']}</p>") 
