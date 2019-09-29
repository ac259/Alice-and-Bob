import base64
from Crypto.Cipher import AES
import os
import random
import time
import struct

BLOCK_SIZE = 16
#key = 'Computer secuirt'
key = os.urandom(BLOCK_SIZE)
#print(key).encode("hex")
print(key)

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    sum_time = 0
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                start = time.time()
                outfile.write(encryptor.encrypt(chunk))
                end = time.time()
                sum_time = sum_time + (end-start)
    print("Time taken to encrypt is {}".format(sum_time))

def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    sum_time = 0
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                start = time.time()
                outfile.write(decryptor.decrypt(chunk))
                end = time.time()
                sum_time = sum_time + (end-start)

            outfile.truncate(origsize)
    print("Time taken to decrypt is {}".format(sum_time))

encrypt_file(key,'test_size_1mb','encrypt_output_1mb')
decrypt_file(key,'encrypt_output_1mb','decrypted_output_1mb')
