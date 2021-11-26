from classcipher import AffineCipher

key = [7, 21]
messag = "security"
cipher = "vlxijh"

crypto = AffineCipher(key)
print("仿射变换密钥对为: 7 21")
print("security 加密为:", crypto.enCrypt(messag))
print("vlxijh   解密为:", crypto.deCrypt(cipher))
