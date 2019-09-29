from Crypto.Hash import SHA256,SHA512,SHA3_256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time
import os

'''
There is a ,compatability issue with SHA3_256 being imported
in Python 2.7, Python 3+ is usedto run.

'''

def hash(h,filename,hash_name):
	in_filename = filename
	print(in_filename)
	f = open(in_filename, 'rb')
	text = f.read()
	f.close()
	#h = SHA256.new()
	start = time.time()
	h.update(text)
	end = time.time()	
	#print (h.hexdigest())
	print("time taken to hash using {} is:{}".format(hash_name,(end-start)))
	return


def RSA_Key_generator(filename,key_size):
	key = RSA.generate(key_size)
	f = open(filename+str(key_size) +'_mykey.pem','wb')
	f.write(key.export_key('PEM'))
	f.close()

	f = open(filename+str(key_size) +'_mykey.pem','r')
	key = RSA.import_key(f.read())
	return

def rsa(filename,key_size):
	in_filename = filename
	f = open(in_filename, 'rb')
	text = f.read()
	result = ''
	enc_time = 0
	dec_time = 0
	f.close()
	encryptkey = RSA.importKey(open('public_key.pem').read())
	cipher_e = PKCS1_OAEP.new(encryptkey)
	decryptkey = RSA.importKey(open('private_key.pem').read())
	cipher_d = PKCS1_OAEP.new(decryptkey)
	BlockSizeForHex = 64
	for i in range(0,len(text),BlockSizeForHex):
	    block = text[i:i+BlockSizeForHex]
	    message = block

	    start1 = time.time()
	    ciphertext = cipher_e.encrypt(message)
	    end1 = time.time()
	    enc_time = enc_time + (end1-start1)
	    #print(ciphertext)
	    
	    start2 = time.time()
	    message = cipher_d.decrypt(ciphertext)
	    end2 = time.time()
	    dec_time = dec_time + (end2-start2)
	    #print(message)

	print('Encryption time of file {} using key size {}  is {}'.format(filename,key_size,enc_time))
	print("Decryption time of file {} using key size {} is {}".format(filename,key_size,dec_time))
	return


h_256= SHA256.new()
h_512 = SHA512.new()	
h_3_256 = SHA3_256.new()
hash_objects = h_256,h_512,h_3_256
filelist = 'test_size_1kb','test_size_1mb'
hash_names = 'SHA-256','SHA-512','SHA3-256'
RSA_key_list = 2048,3072

for file in filelist:
	for obj,name in zip(hash_objects,hash_names):
		hash(obj,file,name)

for key in RSA_key_list:
	for file in filelist:
		RSA_Key_generator(file,key)
		rsa(file,key)	
