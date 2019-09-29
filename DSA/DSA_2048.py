from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import os
import time
 
message = b"Hello"
key = DSA.generate(3072)
publickey = key.publickey() 
hash_obj = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)


verifier = DSS.new(key, 'fips-186-3')
try:
    verifier.verify(hash_obj, signature)
    print("The message is authentic.")
except ValueError:
    print ("The message is not authentic.")