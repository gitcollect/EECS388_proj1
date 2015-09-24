from bleichenbacher import *
import httplib
import urllib
import urlparse

__author__ = 'charlieoconor'

url = "http://eecs388.org/project1/"
parsed_url = urlparse.urlparse(url)


from_account = "eecs388"
to_account = "coconor"
amount = 1000

to_sign = from_account + "+" + to_account + "+" + str(amount)

request_body ={
    "from_account" : from_account,
    "to_account" : to_account,
    "amount" : str(amount),
    "signature" : forge_sig(to_sign)
}

#header = ""

conn = httplib.HTTPConnection(parsed_url.hostname, parsed_url.port)
conn.request("POST", parsed_url.path, urllib.urlencode( request_body ))

print conn.getresponse().read()