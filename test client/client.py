#!/usr/bin/env python
#coding=utf8
 
import http.client
 
conn = None
url2='www.google.com' 

try:
    conn = http.client.HTTPSConnection("https:'/'/a5wqxok61f.execute-api.us-east-2.amazonaws.com/test") 
    conn.request('GET', '/')
 
    response = conn.getresponse()
    print(response.status, response.reason)
#    print(response.read())
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()


