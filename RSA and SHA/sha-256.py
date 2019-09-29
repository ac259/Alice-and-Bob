from Crypto.Hash import SHA256,SHA512,SHA3_256
import time
import os

'''
we have to use python 3 to run this as there is a,
compatability issue with SHA3_256 being imported
'''

def hash(h,filename,hash_name):
	in_filename = filename
	print(in_filename)
	f = open(in_filename, 'rb')
	text = f.read()
	f.close()
	start = time.time()
	h.update(text)
	end = time.time()	
	print("time taken to hash using {} is:{}".format(hash_name,(end-start)))
	return

h_256= SHA256.new()
h_512 = SHA512.new()	
h_3_256 = SHA3_256.new()
hash_objects = h_256,h_512,h_3_256
filelist = 'test_size_1kb','test_size_1mb'
hash_names = 'SHA-256','SHA-512','SHA3-256'

for file in filelist:
	for obj,name in zip(hash_objects,hash_names):
		hash(obj,file,name)

