from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import os
import time


in_filename = 'test_size_1kb','test_size_1mb'
for file in in_filename:
    f = open(file, 'rb')
    text = f.read() 
    verify_time = 0
    sign_time = 0 
    BlockSizeForHex = 64
    for i in range(0,len(text),BlockSizeForHex):
        block = text[i:i+BlockSizeForHex]
        message = block
        key = DSA.generate(3072)
        publickey = key.publickey() 
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        start1 = time.time()
        signature = signer.sign(hash_obj)
        end1 = time.time()
        sign_time = sign_time + (end1- start1)

        verifier = DSS.new(key, 'fips-186-3')
        try:
            start2 = time.time()
        	verifier.verify(hash_obj, signature)
            end2 = time.time()
            verify_time = verify_time + (end2-start2)
        	print("The message is authentic.")
        except ValueError:
        	print ("The message is not authentic.")
    print("Sign time is {} ".format(sign_time))
    print("verify time is {} ".format(verify_time))


