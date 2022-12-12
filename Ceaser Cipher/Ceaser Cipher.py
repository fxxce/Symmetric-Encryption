import random


def cc_encryption(st, shift):
    res = ""
    space_substitute = ["@", "#", "$", ".", ";", "&", "*", "?", "~", ","]
    for i in st:
        if i == " ":
            res = res + space_substitute[random.randint(0, 9)]
        elif 48 <= ord(i) <= 57:
            res = res + chr((ord(i) + shift - 48) %10 + 48)
        elif i.isupper():
            res = res + chr((ord(i) + shift - 65) % 26 + 65)
        else:
            res = res + chr((ord(i) + shift - 97) % 26 + 97)
    return res


def cc_decryption(st, shift):
    res = ""
    space_substitute = ["@", "#", "$", ".", ";", "&", "*", "?", "~", ","]
    for i in st:
        if i in space_substitute:
            res = res + " "
        elif 48 <= ord(i) <= 57:
            res = res + chr((ord(i) - shift - 48) % 10 + 48)
        elif i.isupper():
            res = res + chr((ord(i) - shift - 65) % 26 + 65)
        else:
            res = res + chr((ord(i) - shift - 97) % 26 + 97)
    return res


string = input("Enter String: ")
move = int(input("Enter Shift Key: "))
encrypted = cc_encryption(string, move)
decrypted = cc_decryption(encrypted, move)
print("Original text: " + string)
print("Encrypted text: " + encrypted)
print("Decrypted text: " + decrypted)
