# Study-Cryptology
## 关于现代密码学的Python学习源码及实例

### ClassCipher  
    古典加密的Python块，即ClassCipher/lasscipher  
    __init__.py @初始化模块路径，以供其他文件导入模块  
    __util.py  @数学运算工具类、变换算法工具类、键盘输入处理类  
    caesar.py  @凯撒密码  
    shift.py   @移位密码  
    affine.py  @仿射变换  
    polyalphabet.py @多表代换  
    
    Exam, Exerc等.py文件 @《现代密码学第4版 杨波》的例题及习题  
      
### DesCipher  
    __tabel.py @储存关于各种置换表的全局变量  
    __util.py  @置换运算、编码操作等   
    des.py     @DES加解密核心  

### RsaCipher
    __util.py  @基本算法、编码操作等  
    rsa.py     @RSA加解密核心  
