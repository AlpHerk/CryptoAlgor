import math

def gcd(x, y):
	""" 欧几里德算法 """
	while x > 0:
		x, y = y % x, x
	return y

def extEuclid(a, b):
	""" 扩展欧几里德算法 """
	if b == 0:
		return a, b
	else:
		x, y = extEuclid(b, a % b)
		x, y = y, x - (a//b) * y
		return x, y

def modInvElem(a, m):
	""" 求整数a关于1模m的乘法逆元 """
	if (gcd(a, m) !=1):
		return -1
	inva, _ = extEuclid(a, m)
	inva %= m
	return inva

def fastModExponent(a, m, n):
	""" 快速模指数算法
		@return: (a^m) mod n
	"""
	ans = 1
	a = a % n # 若a比n大则取模简化
	while m != 0:
		if m & 1: ans = (ans * a) % n
		m = m >> 1
		a = (a * a) % n
	return ans


def enCode(text):
	""" 53编码 by Herk
		@字符串:"abc" -> 编码流:"010203"
	"""
	pool = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code = [(2-len(str(pool.index(i))))*'0'+str(pool.index(i)) for i in text]

	return ''.join(code)

def deCode(code):
	""" 53解码 by Herk
		@编码流:"010203" -> 字符串:"abc"
	"""
	pool = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	text = [pool[int(code[i:i+2])%53] for i in range(0, len(code), 2)]

	return ''.join(text)

def divideGroup(code, glen=10):
	""" 对编码进行分组补全
		@code: 待分组的编码流
		@glen: 分组长度, 最后一组不足则右端补0
		@return: 编码流的分组列表
	"""
	group = [code[i:i+glen] for i in range(0, len(code), glen)]
	group[-1] = group[-1] + (glen - len(group[-1])) * '0'
	return group
