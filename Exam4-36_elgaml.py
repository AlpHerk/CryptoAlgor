from ellipticc import ECC
import time


def takeTime(func):
    """ 装饰器: 计算函数运行耗时"""
    def decorated(*args):
        startime = time.time()
        func(*args)
        endtime  = time.time()
        taketime = round((endtime - startime)*10**3)
        print(f"->运算耗时: {taketime} 毫秒")
        return func
    return decorated


@takeTime
def Elgamal_exam436():
    # 利用ECC椭圆密码, 实现 Elgamma 加密
    # 公开椭圆曲线 ECC 的参数 Ep(a,b)、G
    # Alice 选择一整数私钥 Nk4
    # Alice 公开自己的公钥 PA=NA*G
    ellip = ECC(-1, 188, 751)
    G  = ellip.point(0, 376)
    PA = ellip.point(201, 5)

    # Bob 选择随机数 k, 对消息 PM 进行加密得到密文
    # Bob 发送密文 C = [(676, 558), (385, 328)]
    k  = 386
    PM = ellip.point(562, 201)
    C  = [k*G, PM + k*PA]

    print("\n密文为:", C)


@takeTime
def crackElgamal():
    """ 破解例题中 Alice 的私钥 """
    ellip = ECC(-1, 188, 751)
    PM = ellip.point(562, 201)
    C1 = ellip.point(676, 558)
    C2 = ellip.point(385, 328)

    for i in range(1, 1000):
        tmp = C2 - i*C1
        if tmp.point == PM.point:
            print("\nAlice选择的密钥为:", i)
            return i
    print("\n未破解成功, 请加大迭代次数")
    return 0


if __name__ == '__main__':

    Elgamal_exam436()
    crackElgamal()