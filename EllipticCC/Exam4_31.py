from ellipticc import ECC


ellip = ECC(1, 1, 23)
P, Q  = (3, 10), (9, 7)
addPQ = ellip.add(P, Q)
add2P = ellip.add(P, P)

print("P+Q:", addPQ)
print("P+P:", add2P)