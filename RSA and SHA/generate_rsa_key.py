from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time

def RSA_Key_generator(key_size):
	new_key = RSA.generate(key_size, e=255)

	#The private key in PEM format
	private_key = new_key.exportKey("PEM")

	#The public key in PEM Format
	public_key = new_key.publickey().exportKey("PEM")

	#print("the private key is {}".format(private_key))
	fd = open("private_key.pem", "wb")
	fd.write(private_key)
	fd.close()

	#print("The pyublic key is {}".format(public_key))
	fd = open("public_key.pem", "wb")
	fd.write(public_key)
	fd.close()

def rsa(filename):
	in_filename =filename
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
	    print(ciphertext)
	    
	    start2 = time.time()
	    message = cipher_d.decrypt(ciphertext)
	    end2 = time.time()
	    dec_time = dec_time + (end2-start2)
	    print(message)

	print('Encryption time {}'.format(enc_time))
	print("Decryption time {}".format(dec_time))

RSA_Key_generator(2048)
rsa('test_size_1mb')
rsa('test_size_1mb')

RSA_Key_generator(3072)
rsa('test_size_1kb')
rsa('test_size_1mb')	

