from __table import *
import time

def permutate(bitstr, table):
    """ 通用置换运算
        * table : 置换盒
    """
    res = ""
    for i in table:   
        res += bitstr[i-1]
    
    return res

def leftShift(key, num):
    """ 子密钥LR: 左循环移位
        * key : 待移位的子密钥
        * num : 列表左移位位数
    """
    return key[num:] + key[0:num]

def XOR(str1, str2):
    """ 两比特串进行异或 """
    res = ""
    for i in range(0, len(str1)):
        xor = int(str1[i]) ^ int(str2[i])
        res += str(xor)
    return res

def Sbox(binstr):
    """ S盒置换: 48位->32位 """
    box = 0     # S盒的索引
    res = ""
    for i in range(0, len(binstr), 6):
        tmp = binstr[i:i+6]
        row = int(tmp[0] + tmp[5], 2)
        col = int(tmp[1:5], 2)

        num = bin(SBOX[box][16*row+col])[2:]
        num = '0' * (4-len(num)) + num #以0左补全4位

        res += num
        box += 1

    return res

def createSubKey(key64):
    """ 64位母密钥->16轮的48位子密钥列表
        * key64 : 输入的64位加密密钥
        * return : 16轮子密钥列表
    """
    subkey = []
    key56  = permutate(key64, PC_1)       # 64位密钥压缩置换
    C28b, D28b = key56[0:28], key56[28:]  # 56位密钥左右平分
    
    for i in range(16):
        C28b = leftShift(C28b, ROTATE[i]) # 子密钥左循环移位
        D28b = leftShift(D28b, ROTATE[i]) # 子密钥左循环移位
        subkey.append(permutate(C28b + D28b, PC_2))

    return subkey

def turnFunction(R32b, subkey):
    """ 轮结构中的F函数
        * R32b : F函数输入参数 32位的右明文
        * subkey : F函数输入参数 48位子密钥
    """
    R48b = permutate(R32b, E) # E盒扩展: 右明文32位->48位
    R48b = XOR(R48b, subkey)  # 两异或:  扩展流与子密钥异或
    R32b = Sbox(R48b)         # S盒压缩: 压缩48位->32位
    Fout = permutate(R32b, P) # P盒置换

    return Fout

def strToBit(plaintext):
    """ 字符串->二进制比特流 """
    binstr = ""
    for i in plaintext:
        oct = bin(ord((i)))[2:]        # 字符转二进制编码
        oct = (8-len(oct)) *'0' + oct  # 字符编码头部补全8位
        binstr += oct
    if len(binstr) % 64 != 0:
        blank = 64 - len(binstr) % 64  # 明文流尾部补全64位
        binstr = binstr + blank * '0'

    return binstr

def bitToStr(binstr):
    """ 比特流->字符串 """
    res = ""
    oct = int(len(binstr) / 8)

    for i in range(oct):
        bin = binstr[i:i+8]
        print(int(bin, 2))
        res += chr(int(bin, 16))
    
    return res

def hexToBit(hexstr):
    """ 十六进制字符串->二进制比特流(每字符4位) """
    binstr = ""
    decstr = [str(int(i, 16)) for i in hexstr]
    for i in decstr:
        octbin = bin(int(i, 10))[2:]
        binstr += (4-len(octbin)) * '0' + octbin
    return binstr

def bitToHex(bitstr):
    """ 二进制比特流->十六进制字符串 """
    bitlst = [bitstr[i:i+4] for i in range(0, len(bitstr), 4)]
    hexlst = [hex(int(i, 2))[2:].upper() for i in bitlst]

    return ''.join(hexlst)

def takeTime(func):
    """ 装饰器: 计算函数运行耗时"""
    def decorated(*args):
        startime = time.time()
        func(*args)
        endtime  = time.time()
        taketime = round((endtime - startime)*10**6)
        print(f"\n->运算耗时: {taketime} 微秒")
        return func(*args)
    return decorated