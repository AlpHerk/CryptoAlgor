from classcipher import AffineCipher


def crackCipher():
    ciphertext = "edsgickxhuklzveqzvkxwkzukvcuh"
    for i in range(26):
        for j in range(26):

            crypto = AffineCipher([i, j])
            plaintext = crypto.deCrypt(ciphertext)

            if plaintext.startswith("if"):
                print(f"明文: {plaintext}")
                print(f"密钥: {i} {j}")
                return 

crackCipher()