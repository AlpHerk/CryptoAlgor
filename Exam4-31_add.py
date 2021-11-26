from ellipticc import ECC

ellip = ECC(1, 1, 23)
P = ellip.point(3, 10)
Q = ellip.point(9, 7)

print("P + Q:", P + Q)
print("2 * P:", 2 * P)