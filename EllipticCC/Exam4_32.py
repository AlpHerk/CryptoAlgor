from ellipticc import ECC

ellip = ECC(-2, -3, 7)
addP, P = (3, 2), (3, 2)

for i in range(2, 11):
    addP = ellip.add(addP, P)
    print(f"{i}P:", addP)
