class ShiftCipher():
    """ 移位变换加密 """
    
    def __init__(self, inputkey=None):
        self.inputkey  = inputkey
        self.buildKey()

    def buildKey(self):
        if self.inputkey == None:
            self.inputkey = input("\n输入移位密钥: ")
        self.key = int(self.inputkey)

    def enCrypt(self, plaintext):
        codelist = []
        ciphertext = []

        for i in plaintext:
            codelist.append(ord(i))

        for i in codelist:
            if 65 <= i <= 90:
                i += self.key
                while i > 90: i -= 26
            elif 97 <= i <= 122:
                i += self.key
                while i > 122: i -= 26
            ciphertext.append(chr(i))

        return ''.join(ciphertext)

    def deCrypt(self, ciphertext):
        codelist = []
        plaintext = []

        for i in ciphertext:
            codelist.append(ord(i))

        for i in codelist:
            if 65 <= i <= 90:
                i -= self.key
                while i < 65: i += 26
            elif 97 <= i <= 122:
                i -= self.key
                while i < 97: i += 26
            plaintext.append(chr(i))
        
        return ''.join(plaintext)
        
      
if __name__ == '__main__':

    crypto = ShiftCipher()
    
    plaintext = input("输入明文: ")
    print("加密结果:", crypto.enCrypt(plaintext))

    ciphertext = input("输入密文: ")
    print("解密结果:", crypto.deCrypt(ciphertext))
