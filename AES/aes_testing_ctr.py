import base64
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import random
import time
import struct

BLOCK_SIZE = 32
start = time.time()
key = os.urandom(BLOCK_SIZE)
end = time.time()
print("Time taken to generate key is {}".format(end -start))
print(key)

def aes_ctr(key, in_filename,output,encrypt = True):
    
    BlockSizeForHex = 32
    # Read file that contains plaintext / ciphertext #  
    f = open(in_filename, 'rb')
    text = f.read()
    f.close()

    encryptionKey = key
    iv = 'abcdef1234567890abcdef1234567890'
    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    counter = Counter.new(128, initial_value=int(iv,16))
    aes_ctr = AES.new(key, AES.MODE_CTR, counter = counter)
    result = b''
    sum_time = 0
    # Iterate over text #
    for i in range(0,len(text),BlockSizeForHex):

        # AES CTR operates on 16 bytes blocks #
        block = text[i:i+BlockSizeForHex]
        if encrypt:
            start = time.time()
            result += aes_ctr.encrypt(block)
            end = time.time()
            sum_time = sum_time + (end-start)
            
        else:
            start = time.time()
            result += aes_ctr.decrypt(block)
            end = time.time()
            sum_time = sum_time + (end-start)
            
    if output:
        f = open(output,'wb')
        f.write(result)
        f.close()
    if encrypt:
        print("Time taken to encrypt is {}".format(sum_time))
    else:
        print("Time taken to decrypt is {}".format(sum_time))

#e = True
#aes_ctr(key,'test_size_1kb','aes_ctr_encrypt',e)
e = False
#aes_ctr(key,'aes_ctr_encrypt','aes_ctr_decrypt',e)


def aes_cbc(key, in_filename,output,encrypt = True):
    
    BlockSizeForHex = 32
    # Read file that contains plaintext / ciphertext #  
    f = open(in_filename, 'rb')
    text = f.read()
    f.close()

    encryptionKey = key
    #iv = 'abcdef1234567890abcdef1234567890'
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    
    aes_cbc = AES.new(key, AES.MODE_CBC, iv)
    result = b''
    sum_time = 0
    # Iterate over text #
    for i in range(0,len(text),BlockSizeForHex):

        # AES CTR operates on 16 bytes blocks #
        block = text[i:i+BlockSizeForHex]
        if encrypt:
            start = time.time()
            result += aes_cbc.encrypt(block)
            end = time.time()
            sum_time = sum_time + (end-start)
            
        else:
            start = time.time()
            result += aes_cbc.decrypt(block)
            end = time.time()
            sum_time = sum_time + (end-start)
            
    if output:
        f = open(output,'wb')
        f.write(result)
        f.close()
    if encrypt:
        print("Time taken to encrypt is {}".format(sum_time))
    else:
        print("Time taken to decrypt is {}".format(sum_time))

aes_cbc(key,'test_size_1mb','encrypt_output_1mb',e)