from pymd5 import md5

m = "Use HMAC, not hashes"
h = md5()
h.update(m)
print h.hexdigest()

