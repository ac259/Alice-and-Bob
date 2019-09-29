from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

message = "Hello"
key = DSA.generate(1024)
h = SHA.new(message).digest()
k = random.StrongRandom().randint(1,key.q-1)
sig = key.sign(h,k)


if key.verify(h,sig):
    print("OK")
else:
    print("Incorrect signature")

