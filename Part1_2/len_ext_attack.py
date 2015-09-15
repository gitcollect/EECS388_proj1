__doc__ = """
    EECS 388 project 1
    len_ext_attack.py
"""

import httplib, urlparse, sys, urllib
from pymd5 import md5, padding


def len_ext_attack( url, command_to_add, user_password_length):

    """

    :rtype : void
    """
    # Parse the URL and get the current session token
    parsedUrl = urlparse.urlparse( url )
    parameters = dict(urlparse.parse_qsl( parsedUrl.query ))

    # parse the command
    command_to_add = "&command" + str(len(parameters)) + "=" + command_to_add

    if "token" not in parameters:
        # if there isn't a token in the parameters quit the program
        print "There is no token in the url parameters"
        assert False

    #remove the session token from the current parameters
    session_token = parameters["token"]
    del parameters["token"]

    length_of_message_with_password = len(urllib.urlencode( parameters )) + user_password_length
    bits = (length_of_message_with_password + len(padding(length_of_message_with_password*8)))*8

    h = md5(state=session_token.decode("hex"), count=bits)
    #h.update(padding(length_of_message_with_password * 8 ))
    h.update( command_to_add )

    #build the query
    parameters_list = urlparse.parse_qsl( parsedUrl.query )

    query = "token=" + h.hexdigest()

    for x in range(1, len(parameters_list)):
        query += "&" + parameters_list[x][0] + "=" + parameters_list[x][1]

    query += urllib.quote( padding(length_of_message_with_password * 8 ) )
    query += command_to_add

    conn = httplib.HTTPConnection(parsedUrl.hostname, parsedUrl.port)
    print parsedUrl.path + "?" + query
    conn.request("GET", parsedUrl.path + "?" + query )
    print conn.getresponse().read()



if __name__ == "__main__":

    # sanitize the user input
    if len(sys.argv) < 2:
        print "Need input url"
        assert False

    url_in = sys.argv[1]
    print url_in
    len_ext_attack(url_in, "UnlockAllSafes", 8)
