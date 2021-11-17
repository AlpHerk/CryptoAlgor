from classcipher.affine import *


key = [11, 23]
messag = "THE NATIONAL SECURITY AGENCY"
cipher = "YWP KXYHVKXO NPTJCHYB XLPKTB"

crypto = AffineCipher(key)
print("仿射变换密钥: 11 23")
print("加密为:", crypto.enCrypt(messag))
print("解密为:", crypto.deCrypt(cipher))