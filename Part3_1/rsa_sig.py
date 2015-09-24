# n is the modulus from the key.
# You can just assign it as a hexadecimal literal--remember to start with 0x
# It will look something like:
n = 0x00d56d87ba372303f8cd4d970b11b592d2540dae48b67b5fe17b8363fff785132f4de7d0a5d323cfed2cef0f2f51750d96814bda1413aeefc4104dd059e49e435f
# e is the exponent from the key
e = 3

signature = int(open('sig').read().encode('hex'), 16)

x = pow(signature, e, n)

print "%0128x" % x



