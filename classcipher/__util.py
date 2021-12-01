import numpy as np


class MathUtil():
    """ 数学运算工具类 """

    def gcd(x, y):
        """欧几里德算法"""
        while x > 0:
            x, y = y % x, x
        return y

    def extEuclid(a, b):
        """扩展欧几里德算法"""
        if b == 0:
            return a, b
        else:
            x, y = MathUtil.extEuclid(b, a % b)
            x, y = y, x - (a//b) * y
            return x, y

    def modInvElem(a:int, m=26):
        """求整数a关于1模m的乘法逆元"""
        if (np.gcd(a, m) !=1): return -1
        inva, _ = MathUtil.extEuclid(a, m)
        inva %= m
        return inva

    def modInvMatrix(A, m=26):
        """求矩阵A关于1模m的乘法逆元"""
        detA = np.linalg.det(A)
        invA = np.linalg.inv(A)
        Adjoint = detA * invA
 
        inv_detA = MathUtil.modInvElem(round(detA), m)
        cipher_invA = ((inv_detA % m) * Adjoint) % m
        cipher_invA = np.round(cipher_invA).astype(int)

        return cipher_invA


class TransAlgor():
    """ 变换算法工具类 """

    def affine(code, A, B, m=26):
        """仿射变换1模26算法"""
        return (A * code + B) % m

    def invAffine(code, invA, B, m=26):
        """仿射变换1模26逆算法"""
        return invA * (code - B) % m

    def polyalphabet(code:list, A, B, m=26) -> list:
        """多表代换1模26算法"""
        group_len = len(B)
        code = np.mat(code).reshape(group_len,1)

        C = ((np.dot(A, code) + B) % m).reshape(-1)
        C = C.tolist()[0]

        return C

    def invpolyalpha(code:list, invA, B, m=26) -> list:
        """多表代换1模26逆算法"""
        group_len = len(B)
        code = np.mat(code).reshape(group_len, 1)

        M = (np.dot(invA, (code - B)) % m).reshape(-1)
        M = M.tolist()[0]

        return M


class InitDeal():
    """ 键盘输入处理类 """

    def inputKey() -> list:
        """ 用户从键盘输入密钥 """
        keyA = [[*map(eval, input("\n请输入n阶密钥方阵A:\n").split())]]
        for _ in range(len(*keyA) - 1):
            keyA.append([*map(eval, input().split())])
        keyB = [*map(eval, input("\n请输入n维密钥向量B:\n").split())]
        key = [keyA, keyB]

        return key

    def keyProcess(inputkey):
        """ 输入密钥进行处理->逆元cipher_invA等密钥 """
        A, B = inputkey
        group_len = len(B)
        A = np.mat(A).reshape(group_len,group_len)
        B = np.mat(B).reshape(group_len,1)
        try: cipher_invA = MathUtil.modInvMatrix(A)
        except: return False
        keylist = [A, B, cipher_invA]

        return keylist
        
    def dealText(textstr, group_len):
        """ 将文本进行分组处理
            @textstr: 字符串文本
            @group_len: 分组长度
        """
        # 文本字符串去空格, 长度用z补全, 如"abcabc" 
        textstr = textstr.replace(" ", "")
        blank = len(textstr) % group_len
        if blank != 0:
            textstr = textstr + (group_len-blank) * "z"

        # 统一转换成小写0~25编码列表, 如[0,1,2,0,1,2]
        textlist = list(textstr.lower())
        codelist = [ord(i)-97 for i in textlist]

        # 将编码列表进行分组, 即编码子向量, 如[[0,1,2],[0,1,2]]
        codegroup = []
        for i in range(0, len(codelist), group_len):
            codegroup.append(codelist[i:i+group_len])

        return codegroup


class HerkCode():
    """ 自定义编码类 """

    def enCode(text):
        """ 53编码 by Herk
            @text: 待编码的字符串, 如"abc"
            @return: 对应的编码流, 即"010203"
        """
        pool = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        code = [(2-len(str(pool.index(i))))*'0'+str(pool.index(i)) for i in text]

        return ''.join(code)

    def deCode(code):
        """ 53解码 by Herk
            @code: 待解码的数字流, 如"010203"
            @return: 对应的字符串, 即为"abc"
        """
        pool = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        text = [pool[int(code[i:i+2])] for i in range(0, len(code), 2)]

        return ''.join(text)