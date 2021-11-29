from Crypto.Util import number
from __util import *


class RSA():
    """ RSA 加解密 """
    
    def __init__(self, p=None, q=None, e=None):
        """ 初始化公私钥
            @获取p, q, e生成公私钥
            @若为空则随机生成公私钥
        """
        self.p, self.q, self.e = p, q, e
        key = self.genParam()
        print("公钥为:", key[0])
        print("私钥为:", key[1])
    
    def genParam(self):
        """ 参数生成函数
            @生成公钥, 生成私钥
        """
        p, q, e = self.p, self.q, self.e
        if (p==None or q==None):
            __p = number.getPrime(10)
            __q = number.getPrime(10)
            phi = (__p-1) * (__q-1)
            self.e = phi - 1  # e比phi小1, 两者必定互素
        else:
            __p, __q, self.e = p, q, e
            phi = (__p-1) * (__q-1)
        self.n = __p * __q
        self.d = modInvElem(self.e, phi)
        return [self.e, self.n], [self.d, self.n]

    def cryptRSA(self, codes, flag):
        """ RSA算法
            @编码流A->编码流B
        """
        codeB = '' # 待返回的编码流B
        codelistA = divideGroup(codes, 10)  # 分组长度要小于 n
        if flag == 1: exponent = self.e     # RSA正向算法
        else: exponent = self.d             # RSA逆向算法
        for code in codelistA:
            leng = len(code)   # 传入编码流长度, return时补全不足
            code = fastModExponent(int(code), exponent, self.n)
            codeB += str(code).zfill(leng) #zfill:编码流左端补0
        return codeB

    def encrypt(self, messagcode):
        """ RSA加密算法
            @mscode: 明文编码流
            @return: 密文编码流
        """
        return self.cryptRSA(messagcode, 1)


    def decrypt(self, ciphercode):
        """ RSA解密算法
            @cipher: 密文编码流
            @return: 明文编码流
        """
        return self.cryptRSA(ciphercode, 0)


if __name__ == '__main__':

    mscode = enCode("please wait for me")
    cicode = "0763222127199153452800748825533895624854"

    crypto = RSA(71593, 77041, 1757316971)
    cicode = crypto.encrypt(mscode)
    mscode = crypto.decrypt(cicode)
    messag = deCode(mscode)

    print("密文编码流为:", cicode)
    print("明文编码流为:", mscode)
    print("解密后的明文:", messag)
