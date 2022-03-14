import base64 as bs
jo = input("Input The Password :")
password=jo.encode()
encode=bs.b64encode(password)
print(encode)
decoded=bs.b64decode(password)
print(decoded)