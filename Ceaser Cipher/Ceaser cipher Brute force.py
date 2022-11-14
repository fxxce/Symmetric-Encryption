def cc_encryption(st, shift):
    res = ""
    for i in st:
        if i == " ":
            res = res + " "
        elif 48 <= ord(i) <= 57:
            res = res + chr((ord(i) + shift - 48) % 10 + 48)
        elif i.isupper():
            res = res + chr((ord(i) + shift - 65) % 26 + 65)
        else:
            res = res + chr((ord(i) + shift - 97) % 26 + 97)
    return res


def bruteforce_cryptanalysis(st, msg):
    for shift in range(0, 26):
        shift = shift + 1
        res = ""
        for i in st:
            if i == " ":
                res = res + " "
            elif 48 <= ord(i) <= 57:
                res = res + chr((ord(i) - shift - 48) % 10 + 48)
            elif i.isupper():
                res = res + chr((ord(i) - shift - 65) % 26 + 65)
            else:
                res = res + chr((ord(i) - shift - 97) % 26 + 97)
        print(f"Key: {shift}  -->  Decrypted Message: {res}")


string = input("Enter String: ")
move = int(input("Enter Shift Key: "))
encrypted = cc_encryption(string, move)

print("Original text: " + string)
print("Encrypted text: " + encrypted)
print("-----------------Brute Force Result----------------")
bruteforce_cryptanalysis(encrypted, string)
