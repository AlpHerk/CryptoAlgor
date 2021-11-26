# 现代密码学Python学习源码及实例
# 目录: 古典加密、DES加密、RSA加密、ECC加密


### [1.古典加密模块 ClassCipher][1]
> 文件名|文件简述
> --|--
> \_\_init\_\_.py|  初始化模块路径，导入子文件中的加解密类
> __util.py     |   数学运算类、变换算法类、键盘输入处理类
> caesar.py     |   凯撒密码
> shift.py      |   移位密码
> affine.py     |   仿射变换
> polyab.py     |   多表代换


---
### [2.DES加密模块 DesCipher][2]
> 文件名|文件简述
> --|--
> \_\_init\_\_.py|  初始化模块路径，导入子文件中的加解密类
> __table.py    |   储存关于各种置换表的全局变量  
> __util.py     |   置换运算、编码操作等   
> des.py        |   DES加解密核心  

> 例题实现于 des.py 的 __main__ 中


---
### [3.RSA加密模块 RsaCipher][3]
> 文件名|文件简述
> --|--
> \_\_init\_\_.py|  初始化模块路径，导入子文件中的加解密类
> __util.py     |   基本算法、编码操作等  
> rsa.py        |   RSA加解密核心  

> 例题实现于 rsa.py 的 __main__ 中


---
### [4.ECC加密模块 EllipCC][4]
> 文件名|文件简述
> --|--
> \_\_init\_\_.py|  初始化模块路径，导入子文件中的加解密类
> __util.py     |   求平方剩余、求同余式等  
> ecc.py        |   ECC椭圆曲线类 

> 例题实现于 ecc.py 的 __main__ 中  

**1.ecc.py与ecc2.py区别**  

    ecc.py 与 ecc2.py 都写了椭圆曲线加密的 类ECC()
    两者在功能作用上相同, 不过 ecc.py 用到了运算符重载
    即在 ecc.py 中, 对于椭圆点P, Q:
       你可以直接使用运算符 + - *, 对 P+Q、2*P、P*2 进行运算
       而在 ecc2.py中, 只能通过函数 add(P,Q)、mul(P,2)
    推荐使用 ecc.py, 不过 ecc.py 有点难理解, 先看简单的 ecc2.py

**2.幺元为什么取('O','O') ?**  

    因为('O', 'O')连坐标都不是, 自然不在曲线 y^3=x^3+ax+b上
    它只是一个符号, 写成('O', 'O')只是因为坐标(x,y)有两个分量
    仅仅是为了方便运算, 它只是一个符号
        
> Exam, Exerc等.py文件为《现代密码学第4版 杨波》例题及习题


[1]: https://blog.csdn.net/Alpherkin/article/details/121021025
[2]: https://blog.csdn.net/Alpherkin/article/details/121198150
[3]: https://blog.csdn.net/Alpherkin/article/details/121265516
[4]: https://blog.csdn.net/Alpherkin/article/details/121265516
