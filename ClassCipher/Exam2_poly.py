from classcipher.polyalphabet import *

keyA = [[11, 2, 19],
        [5, 23, 25],
        [20, 7, 17]]
keyB =  [ 0, 0,  0]

# 实例化加密对象, 并传入参数进行构建
key = [keyA, keyB]
plaintext  = "your pin no is four one two six"
ciphertext = "wgi fgj tmr lhh xth wbx zps brb"

crypto = PolyalphabetCipher(key)
print("密钥为:", key)
print("加密为:", crypto.enCrypt(plaintext))
print("解密为:", crypto.deCrypt(ciphertext))
