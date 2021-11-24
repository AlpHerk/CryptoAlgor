from fractions import Fraction


def isQuadricReside(a, p):
    """ 判断 a 是否为 素数p 的`平方剩余`
        ---------------------------
        * return 0 : a 被 p 整除
        * return 1 : a 是模 p 的平方剩余
        * return-1 : a 不是模 p 的平方剩余
    """
    legendre = (a**int((p - 1) / 2)) % p
    if legendre > 1: legendre -= p

    return legendre


def calcResideRoot(a, p):
    """ 求模 p 的平方剩余 a 的两个平方根
        ---------------------------
        即方程 x^2 = a mod p 的解 
        * retrun : 元组解(x1, x2)⛄
    """
    for i in range(1, p):
        if (i**2) % p == a:
            return (i, p - i)


def calcCongruence(a, p):
    """ 计算 a mod p 的同余正整数
        * a : 分数、负数等
        * p : 素数
        * retrun : 同余的正整数
    """
    if isinstance(a, int):
        # 若a为整数, 则直接得到正整数同余式
        return a % p

    if isinstance(Fraction(1, 2), Fraction):
        # 若a为分数, 则计算得到正整数同余式
        congren = (p + a.numerator) / a.denominator
        return int(congren)


