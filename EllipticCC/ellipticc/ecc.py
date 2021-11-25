from fractions import Fraction
from __util import *

class ECC():
    """ 椭圆曲线密码体制 
        * 此`ECC类`用到运算符重载, 代码较复杂
        * 可以参看简化版的 `ECC类`: ecc2.py
        ----------------------
        实现椭圆曲线点的运算, 消息的加密等
        曲线方程: y^2 = x^3 + ax - b
        * a : Ep(a, b) 中的 a
        * b : Ep(a, b) 中的 b
        * p : GF(p), y^2 mod p 中的 p
    """
    def __init__(self, a, b, p):
        '''__class__表示设为类成员属性 以便内部类point访问'''
        if 4 * a**3 + 27 * b**2 == 0: 
            print("非法椭圆曲线，请重新输入")
        self.__class__.a, self.__class__.p = a, p
        self.__class__.Eset = self.genEset(a, b, p)

    @staticmethod
    def genEset(a, b, p):
        """ 生成椭圆曲线的坐标点集 Ep(a, b) 
            * return : 点集列表[(x1,y1), (x2,y2), ··· ]
        """
        Eset = ['O'] # 定义一个`点集Ep(a,b)`的加法幺元
        for x in range(0, p):
            val = (x**3 + a*x + b) % p  # 计算待开方的值
            if isQuadricReside(val, p) == 1:
                """若 val 是 p 的平方剩余, 则求平方剩余的根"""
                solution = calcResideRoot(val, p)
                Eset.append((x, solution[0]))
                Eset.append((x, solution[1]))
        return  Eset
    
    class point():
        """ Ep(a,b)中`坐标点(x, y)`实例化为`point对象`
            --------------------------------------
            实例化后的point对象可做 + - * 等运算
        """
        def __init__(self, *pnt):
            """ 获取实例对象ECC()中的 a, p, `坐标点pnt`
                * a, p : Ep(a, b) 中的 a, p
                * pnt : 椭圆曲线上的坐标点(x, y)
            """
            self.a, self.p = ECC.a, ECC.p
            self.pnt = pnt

        def __add__(self, other):
            """ 重载运算符`+`: 定义椭圆上点的加法
                * self : Point对象(x1, y1)
                * other: Point对象(x2, y2)
                * retrun : P + Q = (x3, y3)
            """
            a, p = self.a, self.p
            P, Q = self, other 
            try: (x1, y1), (x2, y2) = P.pnt, Q.pnt 
            except: pass
            
            if x1== x2 and y1 != y2: return EO  # P+Q=EO
            if P.pnt == EO.pnt: return Q        # EO+Q=Q
            if Q.pnt == EO.pnt: return P        # P+EO=P
            if P.pnt == Q.pnt: lamb = Fraction(3*x1**2+a, 2*y1)
            if P.pnt != Q.pnt: lamb = Fraction(y2-y1, x2-x1)
            lamb = calcCongruence(lamb, p)

            x3 = (lamb**2 - x1 -x2)
            x3 = calcCongruence(x3, p)
            y3 = (lamb * (x1 - x3) - y1)
            y3 = calcCongruence(y3, p)

            return ECC.point(x3, y3)

        def __mul__(self, coef):
            """ 重载运算符`*`: 椭圆上点的数乘 例如Point*3 """
            sums = self
            for _ in range(1, coef):
                sums += self
            return sums
        
        def __rmul__(self, other):
            """ 重载运算符`*`: 椭圆上点的数乘 例如3*Point """
            return self * other

        def __neg__(self):
            """ 重载运算符`-`: 椭圆上点的加法逆元 """
            x, y = (self.pnt[0], ECC.p - self.pnt[1])
            return ECC.point(x, y)

        def __repr__(self):
            """ 重载函数`print`: 打印对象point的点(x,y) """
            disp = self.pnt
            if len(disp) == 1: disp = self.pnt[0]
            return str(disp)


# 全局变量, 自定义加法幺元
EO = ECC(1,1,1).point('O') 


if __name__ == '__main__':

    ellip = ECC(1, 1, 23)   # 实例化一个Ep(a,b)对象
    P = ellip.point(3, 10)  # 实例化Ep(a,b)上的点对象
    Q = ellip.point(9, 7)   # 实例化Ep(a,b)上的点对象

    print("P+Q:", type(1))