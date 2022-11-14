import numpy as np
import string
from sympy import Matrix


def hc_encrypt(msg, key):
    dimension = 3
    msg = msg.replace(" ", "")
    alphabets = string.ascii_lowercase
    encrypted_message = ""
    for index, i in enumerate(msg):
        values = []
        if index % dimension == 0:
            for j in range(0, dimension):
                if index + j < len(msg):
                    values.append([alphabets.index(msg[index + j])])
                else:
                    values.append([25])

            vector = np.matrix(values)
            vector = key * vector
            vector = vector % 26
            for j in range(0, dimension):
                encrypted_message = encrypted_message + alphabets[vector.item(j)]
    return encrypted_message


def hc_decrypt(msg, key):
    dimension = 3
    alphabet = string.ascii_lowercase
    decrypted_message = ""

    key = Matrix(key)
    key = key.inv_mod(26)
    key = key.tolist()

    for index, i in enumerate(msg):
        values = []
        if index % dimension == 0:
            for j in range(0, dimension):
                values.append([alphabet.index(msg[index + j])])
            vector = np.matrix(values)
            vector = key * vector
            vector = vector % 26
            for j in range(0, dimension):
                decrypted_message = decrypted_message + alphabet[vector.item(j)]
    return decrypted_message


message = input("Enter String: ").lower()
print("Original Message: ", message)
# key = hillciphr
key_matrix = np.matrix([[7, 8, 11], [11, 2, 8], [15, 7, 17]])
enc = hc_encrypt(message, key_matrix)
print("Encrypted Message: ", enc)
print("Decrypted Message: ", hc_decrypt(enc, key_matrix))