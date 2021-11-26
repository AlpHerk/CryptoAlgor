from __util import *


class PolyalphabetCipher():
    """ 多表代换加密 """
    
    def __init__(self, inputkey=None):
        """ 实例化类时需要复写的属性 """
        self.inputkey  = inputkey
        self.buildKey()

    def buildKey(self):
        """ 实例化对象后 必须构建密钥 """
        if self.inputkey == None:
            self.inputkey = InitDeal.inputKey()
        key = InitDeal.keyProcess(self.inputkey)
        self.A, self.B, self.invA = key

    def enCrypt(self, plaintext):
        """ 加密算法 返回密文 """
        ciphertext = ""
        codegroup = InitDeal.dealText(plaintext, len(self.B))

        for group in codegroup:
            group = TransAlgor.polyalphabet(group, self.A, self.B)
            group = [chr(i+97) for i in group] # 密文编码->字母串列表
            group = ''.join(group)             # 字母串列表->密文串
            ciphertext = ciphertext + group + " "

        return ciphertext

    def deCrypt(self, ciphertext):
        """ 加密算法 返回明文 """
        plaintext = ""
        codegroup = InitDeal.dealText(ciphertext, len(self.B))

        for group in codegroup:
            group = TransAlgor.invpolyalpha(group, self.invA, self.B)
            group = [chr(i+97) for i in group] # 明文编码->字母串列表
            group = ''.join(group)             # 字母串列表->明文串
            plaintext = plaintext + group + " "

        return plaintext


if __name__ == '__main__':

    crypto = PolyalphabetCipher()

    plaintext = input("输入明文: ")
    print("加密结果:", crypto.enCrypt(plaintext))

    ciphertext = input("输入密文: ")
    print("解密结果:", crypto.deCrypt(ciphertext))