from __util import *


class DES():
    """ DES 加解密 """
    
    def __init__(self, scrkey):
        self.scrkey = hexToBit(scrkey) # 初始化密钥 16进制字符->比特流

    def feistel(self, in64bit, flag):
        """ Feistel 网络结构算法
            @in64bit: 输入64位比特流
            @flag: 正向算法/反向算法
            单字符由8比特表示
        """
        bit64  = permutate(in64bit, IP)      # 初置换IP重排明文
        L32b, R32b = bit64[0:32], bit64[32:] # 64位明文左右平分
        
        subkey = createSubKey(self.scrkey)   # 生成所有的子密钥  
        if flag == 0: subkey = subkey[::-1]  # 解密用的逆子密钥

        for i in range(16):
            Fout = turnFunction(R32b, subkey[i])
            L32b, R32b = R32b, XOR(L32b, Fout)
        out64bit = permutate(R32b + L32b, IP_INV) # 左右交换 逆初始置换

        return out64bit

    @takeTime
    def encrypt(self, messag):
        """ DES加密
            @messag: 16进制明文字符串
            @return: 16进制密文字符串
        """
        mesbit = hexToBit(messag)
        cipbit = self.feistel(mesbit, 1)
        cipher = bitToHex(cipbit)

        return cipher

    @takeTime
    def decrypt(self, cipher):
        """ DES 解密
            @cipher: 16进制密文字符串
        """
        cipher = hexToBit(cipher)
        mesbit = self.feistel(cipher, 0)
        messag = bitToHex(mesbit)

        return messag


if __name__ == '__main__':

    scrkey = "133457799BBCDFF1" 
    messag = "0123456789ABCDEF"
    cipher = "85E813540F0AB405"

    crypto = DES(scrkey)
    print("16进制密文:", crypto.encrypt(messag))
    print("16进制明文:", crypto.decrypt(cipher))
    
    
    