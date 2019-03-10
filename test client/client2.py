#!/usr/bin/env python
#coding=utf8
 
import httplib
 
conn = None
url='www.google.com' 

try:
    conn = httplib.HTTPSConnection("a5wqxok61f.execute-api.us-east-2.amazonaws.com/test") 
    conn.request('GET', '/')
 
    response = conn.getresponse()
    print(response.status, response.reason)
#    print(response.read())
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()


