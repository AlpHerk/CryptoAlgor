import numpy as np
import time
from classcipher import PolyalphabetCipher
from itertools import product


def takeTime(func):
    """ 装饰器: 计算函数运行耗时"""
    def decorated(*args):
        startime = time.time()
        func(*args)
        endtime  = time.time()
        taketime = round(endtime - startime, 2)
        print(f"--解密总耗时: {taketime} s\n")
        return func
    return decorated


@takeTime
def crackCipher(keyA_list, keyB = [0, 0]):
    print("\n--开始破解密钥  ····")
    for keyA in keyA_list:
        ciphertext = ""
        keyA = np.mat(list(keyA)).reshape(2, 2)
        detA = np.round(np.linalg.det(keyA)).astype(int)

        if (detA > 0) and (np.gcd(detA, 26) == 1):
            crypto = PolyalphabetCipher([keyA, keyB])
            ciphertext = crypto.enCrypt("dont").replace(" ", "")
            print(f"\r--正在匹配密文: {ciphertext}", end='')

        if ciphertext == "elni":
            print(f"\n--密钥矩阵A为:\n {keyA}")
            return True


if __name__ == '__main__':

    # 生成一个密钥迭代器, 存储二阶方阵的所有组合, 用于暴力循环破解密钥
    keyA_list = product(list(range(26)), repeat=4)
    crackCipher(keyA_list)
