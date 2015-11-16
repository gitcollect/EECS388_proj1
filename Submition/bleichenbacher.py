import hashlib
import sys
# why is bitcount protected
from roots import _bitcount
from roots import *

# the function to create a forged signature and return it
def forge_sig( message ):
    # add the initial padding and such
    forged_signature = 0x0001FF003021300906052B0E03021A05000414

    hash_message = hashlib.sha1(message).hexdigest()

    hash_bits = _bitcount(int(hash_message, 16))

    forged_signature = forged_signature << hash_bits
    forged_signature += int(hash_message, 16)
    forged_signature = forged_signature << 4
    forged_signature += 0xf
    forged_signature = forged_signature << ( 2048 - hash_bits - (38 * 4) - 4)

    root = integer_nthroot(forged_signature, 3)
    return integer_to_base64(root[0])

if __name__ == "__main__":
    message_in = sys.argv[1]
    print forge_sig( message_in )