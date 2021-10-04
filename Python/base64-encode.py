import base64
raw=input("string:")
raw = raw.encode("ascii")
enc = base64.b64encode(raw)
print(enc.decode("ascii"))
