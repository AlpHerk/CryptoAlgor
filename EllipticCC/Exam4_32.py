from ellipticc import ECC

ellip = ECC(-2, -3, 7)
P = ellip.point(3, 2)

for i in range(2, 11):
    print(f"{i}P:", i * P)
