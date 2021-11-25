from fractions import Fraction
from __util import *
EO = 'O' # 全局变量, Ep(a,b)上的无穷远点O

class ECC():
    """ 椭圆曲线密码体制
        -------------
        实现椭圆曲线点的运算, 消息的加密等
        曲线方程: y^2 = x^3 + ax - b
        * a : Ep(a, b) 中的 a
        * b : Ep(a, b) 中的 b
        * p : GF(p), y^2 mod p 中的 p

    """
    def __init__(self, a, b, p):
        if 4*a**3 + 27*b**2 == 0: 
            print("非法椭圆曲线，请重新输入")
        self.a, self.b, self.p = a, b, p
        Eset = self.genEset(a, b, p)

    @staticmethod
    def genEset(a, b, p):
        """ 生成椭圆曲线的点集 Ep(a, b) 
            * return : 点集列表[(x1,y1), (x2,y2), ··· ]
        """
        Eset = ['O']
        for x in range(0, p):
            val = (x**3 + a*x + b) % p  # 计算待开方的值
            if isQuadricReside(val, p) == 1:
                """若 val 是 p 的平方剩余, 则求平方剩余的根"""
                solution = calcResideRoot(val, p)
                Eset.append((x, solution[0]))
                Eset.append((x, solution[1]))
        return  Eset
    
    def add(self, P, Q):
        """ 定义椭圆曲线上点的加法
            * P : 点p (x1, y1)
            * Q : 点q (x2, y2)
            * retrun : P + Q = (x3, y3)
        """
        a, p = self.a, self.p
        (x1, y1), (x2, y2) = P, Q
        if x1 == x2 and y1 != y2: return EO
        if P != Q: lamb = Fraction(y2-y1, x2-x1)
        if P == Q: lamb = Fraction(3*x1**2+a, 2*y1)
        lamb = calcCongruence(lamb, p)

        x3 = (lamb**2 - x1 -x2)
        x3 = calcCongruence(x3, p)
        y3 = (lamb * (x1 - x3) - y1)
        y3 = calcCongruence(y3, p)

        return (x3, y3)

    def mul(self, P, coef):
        """ 定义椭圆曲线上点的数乘
            * P : 点p (x1, y1)
            * coef : 数乘的系数
            * retrun : coef * P = (x3, y3)
        """
        sums = P
        for _ in range(1, coef):
            sums = self.add(sums, P)
        return sums


if __name__ == '__main__':
    
    ellip = ECC(1, 1, 23)
    P, Q  = (3, 10), (9, 7)
    print("P+Q:", ellip.add(P, Q))
    print("2*P:", ellip.mul(P, 2))
