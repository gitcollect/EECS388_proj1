__author__ = 'charlieoconor'
import hashlib
m = hashlib.sha1()
m.update("EECS 388 rul3z!")
print m.hexdigest()