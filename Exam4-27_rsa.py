from rsacipher import RSA, enCode, deCode

mscode = enCode("please wait for me")
cicode = "0763222127199153452800748825533895624854"

crypto = RSA(71593, 77041, 1757316971)
cicode = crypto.encrypt(mscode)
mscode = crypto.decrypt(cicode)
messag = deCode(mscode)

print("密文编码流为:", cicode)
print("明文编码流为:", mscode)
print("解密后的明文:", messag)