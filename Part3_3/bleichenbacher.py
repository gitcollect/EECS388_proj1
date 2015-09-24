import hashlib
import sys
from roots import _bitcount
from roots import *
import re

# figure out how to give it the correct public key
key = """-----BEGIN PUBLIC KEY-----
            MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAqdx4APInKl0oEsjp9OCL
            WPFGZe5SfLteAiFCmMNN354sl3sizqkSGQuPvbhxKkxZzckZyitA7zoFI01U/08M
            tsMqrVqENIrL/neHESjMUiZSaB8UZBYanR+6jVwRsGV5Hi0JnsA0do4Sb5d7KQFE
            LgnAdCffxfo9eKctEXM8NTVmHvmydpLNxLgVF/rWOEu8xSaDzgcNgbrZbkjUuF+L
            myS5gDE1JPIRhua5/Fl5BYHptB5duIPnw45ipS0VtexQ3k8j/2zyUiXqsKyxu9Qq
            0qIJRvtK+Np3ez6fa+ZgMw9MRYosWaLaPG0AxF9JSOvgbz1dZdFv8j4gIoYWAKPS
            rQIBAw==
            -----END PUBLIC KEY-----
      """


# the function to create a forged signature and return it
def forge_sig( message ):
    # Your code to forge a signature goes here.

    key = """MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAqdx4APInKl0oEsjp9OCL
            WPFGZe5SfLteAiFCmMNN354sl3sizqkSGQuPvbhxKkxZzckZyitA7zoFI01U/08M
            tsMqrVqENIrL/neHESjMUiZSaB8UZBYanR+6jVwRsGV5Hi0JnsA0do4Sb5d7KQFE
            LgnAdCffxfo9eKctEXM8NTVmHvmydpLNxLgVF/rWOEu8xSaDzgcNgbrZbkjUuF+L
            myS5gDE1JPIRhua5/Fl5BYHptB5duIPnw45ipS0VtexQ3k8j/2zyUiXqsKyxu9Qq
            0qIJRvtK+Np3ez6fa+ZgMw9MRYosWaLaPG0AxF9JSOvgbz1dZdFv8j4gIoYWAKPS
            rQIBAw=="""

    key = re.sub(r"\W", "", key)
    key = bytes_to_integer(key)

    # add the initial padding and such
    forged_signature = 0x0001FF003021300906052B0E03021A05000414

    hash_message = hashlib.sha1(message).hexdigest()

    #x = _bitcount( int(hash_message, 16))


    hash_bits = _bitcount( int(hash_message, 16))

    forged_signature = forged_signature << hash_bits
    forged_signature += int(hash_message, 16)
    forged_signature = forged_signature << 4
    forged_signature += 0xf
    forged_signature = forged_signature << ( 2048 - hash_bits - (38 * 4) - 4)

    #print forged_signature
    root = integer_nthroot(forged_signature, 3)
    print integer_to_base64(root[0])
    return integer_to_base64(root[0])

if __name__ == "__main__":
    message_in = sys.argv[1]
    print forge_sig( message_in )