from shift import ShiftCipher

class CaesarCipher(ShiftCipher):
    """ 凯撒密码是移位变换 key=3 时的特殊形式
        故此类只需继承ShiftCipher, 覆写key值
    """
    def __init__(self, inputkey = 3):
        self.inputkey = inputkey


if __name__ == '__main__':
    
    crypto = CaesarCipher()

    plaintext = input("输入明文: ")
    print("加密结果:", crypto.enCrypt(plaintext))

    ciphertext = input("输入密文: ")
    print("解密结果:", crypto.deCrypt(ciphertext))