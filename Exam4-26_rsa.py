from rsacipher import RSA

crypto = RSA(7, 17, 5)
cicode = crypto.encrypt("0000000019")
mscode = crypto.decrypt("0000000066")

print("密文编码流为:", cicode)
print("明文编码流为:", mscode)
