"""
    EECS 388 project 1
    len_ext_attack.py

"""
import httplib, urlparse, sys, urllib
from pymd5 import md5, padding

__author__ = 'charlieoconor'

# put functions here


# this is needed if we want to use this as a lib at some point
if __name__ == "__main__" :

    # TODO get rid of this hard code for submit
    # only here to run in pyCharm with out error

    url = """http://eecs388.org/project1/api?token=a1913e8031748f7a5dbd070125bd1cd1&user=admin&command1=ListFiles&command2=NoOp"""

    if len( sys.argv ) > 1:
        url = sys.argv[1]

    print "Input URL:"
    print url

    # use quote to get rid of any special characters and put it in the right form
    urllib.quote( url )

    parsedUrl = urlparse.urlparse( url )



    #md5( state=url, count= )


    # Your code to modify url goes here


    conn = httplib.HTTPConnection(parsedUrl.hostname, parsedUrl.port)
    conn.request("GET", parsedUrl.path + "?" + parsedUrl.query )

    print "Connection response"
    print conn.getresponse().read()


