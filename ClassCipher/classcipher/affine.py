from __util import *


class AffineCipher():
    """ 仿射变换加密 """
    
    def __init__(self, inputkey=None):
        """ 密钥初始化构建
            @inputkey: 例如[1, 3]
            若密钥为空则从键盘输入
        """
        self.inputkey  = inputkey
        self.buildKey()

    def buildKey(self):
        """ 生成相关密钥数据 """
        if self.inputkey == None:
            tips = "输入一对密钥: "      # 例如输入: 1 3 
            self.inputkey = [*map(eval, input(tips).split())]
        self.A, self.B = self.inputkey # 处理输入密钥, 得到密钥a,b
        self.invA = MathUtil.modInvElem(self.A) # 计算密钥a的逆元

    def enCrypt(self, messag):
        """ 仿射变化加密
            @messag: 明文字符串
            @return: 密文字符串
        """
        codelist = []
        cipherlist = []

        for i in messag:
            codelist.append(ord(i))

        for i in codelist:
            if 65 <= i <= 90:
                i -= 65
                i = TransAlgor.affine(i, self.A, self.B) + 65
            elif 97 <= i <= 122:
                i -= 97
                i = TransAlgor.affine(i, self.A, self.B) + 97
            cipherlist.append(chr(i))

        ciphertext = ''.join(cipherlist)

        return ciphertext

    def deCrypt(self, cipher):
        """ 仿射变换解密
            @cipher: 密文字符串
            @return: 明文字符串
        """
        codelist = []
        plainlist = []

        for i in cipher:
            codelist.append(ord(i))

        for i in codelist:
            if 65 <= i <= 90:
                i -= 65
                i = TransAlgor.invAffine(i, self.invA, self.B) + 65
            elif 97 <= i <= 122:
                i -= 97
                i = TransAlgor.invAffine(i, self.invA, self.B) + 97
            plainlist.append(chr(i))

        plaintext = ''.join(plainlist)

        return plaintext


if __name__ == '__main__':

    crypto = AffineCipher()

    messag = input("输入明文: ")
    print("加密结果:", crypto.enCrypt(messag))

    cipher = input("输入密文: ")
    print("解密结果:", crypto.deCrypt(cipher))

