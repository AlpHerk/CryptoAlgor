from classcipher import PolyalphabetCipher

keyA = [[3, 13, 21, 9],
       [15, 10, 6, 25],
       [10, 17, 4,  8],
       [ 1, 23, 7,  2]]
keyB = [ 1, 21, 8, 17]

# 实例化加密对象, 并传入参数进行构建
inputkey = [keyA, keyB]
plaintext  = "please send me the book my credit card no is six one two one three eight six zero one six eight four nine seven zero two"
ciphertext = "nqxb btwb dcjj ijdt xdcf yfsg lygd moxn llgn hapc qzzq zcrg zezj uieb rrsg nemv qdje mxna ierp xakm yrby tqfm nemv fnwo"

crypto = PolyalphabetCipher(inputkey)
print("加密结果:", crypto.enCrypt(plaintext))
print("解密结果:", crypto.deCrypt(ciphertext))