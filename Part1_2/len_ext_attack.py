__doc__ = """
    EECS 388 project 1
    len_ext_attack.py

"""

import httplib, urlparse, sys, urllib
from pymd5 import md5, padding

# put functions here

# this is needed if we want to use this as a lib at some point
if __name__ == "__main__":

    # the command we are trying run
    command_to_add = "UnlockAllSafes"
    user_password_length = 8

    # TODO get rid of this hard code for submit
    # only here to run in pyCharm with out error

    url = """http://eecs388.org/project1/api?token=a1913e8031748f7a5dbd070125bd1cd1&user=admin&command1=ListFiles&command2=NoOp"""

    if len( sys.argv ) > 1:
        url = sys.argv[1]

    print "Input URL:"
    print url

    # use quote to get rid of any special characters and put it in the right form
    #urllib.quote( url )

    # Parse the URL and get the current session token
    parsedUrl = urlparse.urlparse( url )
    parameters = dict(urlparse.parse_qsl( parsedUrl.query ))



    #
    if "token" in parameters:
        session_token = parameters["token"]
        del parameters["token"]
        print "Parameters are:"
        print parameters
    else:
        # if there isn't a token in the parameters quit the program
        print "There is no token in the url parameters"
        assert False

    length_of_message_with_password = len(urllib.urlencode( parameters )) + 8
    bits = length_of_message_with_password + len( padding(length_of_message_with_password*8)) * 8


    # TODO is the count the same as the length? I think so
    hash_object = md5(state=(session_token.decode("hex")), count=length_of_message_with_password)

    #hash_object.update( command_to_add )
    print hash_object.digest()

    #md5( state=url, count= )
    # Your code to modify url goes here

    conn = httplib.HTTPConnection(parsedUrl.hostname, parsedUrl.port)
    conn.request("GET", parsedUrl.path + "?" + parsedUrl.query )

    print "Connection response"
    print conn.getresponse().read()


