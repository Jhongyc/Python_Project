import hashlib,hmac
m=hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It is me")
print(m.hexdigest())
m.update(b"It is been a long time")
print(m.hexdigest())
print("-------------------")
s1=hashlib.sha1()
s1.update(b"Hello")
print(s1.hexdigest())
print('-----------------')
s2=hashlib.sha512()
s2.update(b"Hello")
print(s2.hexdigest())
print("*****************************")
h=hmac.new(b"Hello",b"It is me")
print(h.hexdigest())#十六进制
print(h.digest())#十进制



