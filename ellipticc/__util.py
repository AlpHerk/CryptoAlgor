from fractions import Fraction

def gcd(x, y):
	""" 欧几里德算法 """
	while x > 0:
		x, y = y % x, x
	return y


def extEuclid(a, b):
    """ 扩展欧几里德算法 求同余式
        求 a*x +b*y = gcd(a,b) 解
    """
    if b == 0:
        return a, b
    else:
        x, y = extEuclid(b, a % b)
        x, y = y, x - (a//b) * y
        return x, y


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


def calcCongruence(n, p):
    """ 计算 a mod p 的同余正整数
        ----------------------
        * n : 分数、负数等
        * p : 素数
        * retrun : 同余的正整数
    """
    if isinstance(n, int):
        # 若a为整数, 则直接得到正整数同余式
        return n % p

    # 若n为分数b/a, 则计算得到正整数同余式
    # 即求不定 a*x + p*y = b 的解 x
    a, b = n.denominator, n.numerator
    coef = b  // gcd(a, p)
    x, _ = extEuclid(a, p)
    return (coef * x) % p


