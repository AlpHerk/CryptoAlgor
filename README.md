# 关于现代密码学的Python学习源码及实例

### 古典加密模块 ClassCipher -> [CSDN详解][1]
 
    模块路径: ClassCipher/classcipher  
    __init__.py @初始化模块路径，以供其他文件导入模块  
    __util.py   @数学运算类、变换算法类、键盘输入处理类  
    caesar.py   @凯撒密码  
    shift.py    @移位密码  
    affine.py   @仿射变换  
    polyalphabet.py @多表代换  

    Exam, Exerc等.py文件为《现代密码学第4版 杨波》例题及习题  
      
### DES加密模块 DesCipher -> [CSDN详解][2]
    __table.py @储存关于各种置换表的全局变量  
    __util.py  @置换运算、编码操作等   
    des.py     @DES加解密核心  
    例题实现在 des.py 的 __main__ 中

### RSA加密模块 RsaCipher -> [CSDN详解][3]
    __util.py  @基本算法、编码操作等  
    rsa.py     @RSA加解密核心  
    例题实现在 rsa.py 的 __main__ 中


[1]: https://blog.csdn.net/Alpherkin/article/details/121021025
[2]: https://blog.csdn.net/Alpherkin/article/details/121198150
[3]: https://blog.csdn.net/Alpherkin/article/details/121265516
