def h2b(msg):
    hex_val = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
               "4": "0100", "5": "0101", "6": "0110", "7": "0111",
               "8": "1000", "9": "1001", "A": "1010", "B": "1011",
               "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    m_len = len(msg)
    final = ""
    for i in range(0, m_len):
        final = final + hex_val[msg[i]]
    return final


def b2h(msg):
    bin_val = {"0000": "0", "0001": "1", "0010": "2", "0011": "3",
               "0100": "4", "0101": "5", "0110": "6", "0111": "7",
               "1000": "8", "1001": "9", "1010": "A", "1011": "B",
               "1100": "C", "1101": "D", "1110": "E", "1111": "F"}
    final = ""
    m_len = len(msg)

    for i in range(0, m_len, 4):
        tmp = ""
        tmp = tmp + msg[i: i + 4]
        final = final + bin_val[tmp]

    return final


def init_perm(msg):
    ip_transposition = [58, 50, 42, 34, 26, 18, 10, 2,
                        60, 52, 44, 36, 28, 20, 12, 4,
                        62, 54, 46, 38, 30, 22, 14, 6,
                        64, 56, 48, 40, 32, 24, 16, 8,
                        57, 49, 41, 33, 25, 17, 9, 1,
                        59, 51, 43, 35, 27, 19, 11, 3,
                        61, 53, 45, 37, 29, 21, 13, 5,
                        63, 55, 47, 39, 31, 23, 15, 7]

    bin_val = h2b(msg)
    ip_len = len(ip_transposition)
    final = ""
    for i in range(0, ip_len):
        final = final + str(bin_val[ip_transposition[i] - 1])

    hex_val = b2h(final)
    print("----------------------------------------------------------------------------------")
    print("Initial permutation:", hex_val)
    return hex_val


def expansion_perm(msg):
    expan_perm = [32, 1, 2, 3, 4, 5,
                  4, 5, 6, 7, 8, 9,
                  8, 9, 10, 11, 12, 13,
                  12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25,
                  24, 25, 26, 27, 28, 29,
                  28, 29, 30, 31, 32, 1]

    tmp = msg
    final = ""
    ep_len = len(expan_perm)
    for i in range(0, ep_len):
        final = final + tmp[expan_perm[i] - 1]
    return final


def xor(left, right):
    final = ""
    l_len = len(left)
    for i in range(0, l_len):
        if left[i] == right[i]:
            final = final + '0'
        elif left[i] != right[i]:
            final = final + '1'
    return final


def rounds(round_val):
    s = []
    if round_val == 1:
        s = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    elif round_val == 2:
        s = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    elif round_val == 3:
        s = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    elif round_val == 4:
        s = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    elif round_val == 5:
        s = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    elif round_val == 6:
        s = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    elif round_val == 7:
        s = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    elif round_val == 8:
        s = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    return s


def substitution_box(val):
    dec_val = {"0000": "0", "0001": "1", "0010": "2", "0011": "3",
               "0100": "4", "0101": "5", "0110": "6", "0111": "7",
               "1000": "8", "1001": "9", "1010": "10", "1011": "11",
               "1100": "12", "1101": "13", "1110": "14", "1111": "15"}

    hex_val = {"0": "0", "1": "1", "2": "2", "3": "3",
               "4": "4", "5": "5", "6": "6", "7": "7",
               "8": "8", "9": "9", "10": "A", "11": "B",
               "12": "C", "13": "D", "14": "E", "15": "F"}

    row = {"00": 0, "01": 1, "10": 2, "11": 3}

    final = ""
    count = 0
    round_no = 1
    lst = []
    for i in range(0, 8):
        lst = lst + [val[count:count + 6]]
        count = count + 6

    for round_val in range(0, 8):
        tmp = lst[round_val]
        row_binval = tmp[0] + tmp[5]
        s = rounds(round_no)
        row_val = int(row[row_binval])
        col_val = int(dec_val[tmp[1:5]])
        final = final + str(hex_val[str(s[row_val][col_val])])
        round_no = round_no + 1
    return h2b(final)


def permutation(msg):
    perm_tab = [16, 7, 20, 21, 29, 12, 28, 17,
                1, 15, 23, 26, 5, 18, 31, 10,
                2, 8, 24, 14, 32, 27, 3, 9,
                19, 13, 30, 6, 22, 11, 4, 25]

    final = ""
    pt_len = len(perm_tab)
    for i in range(0, pt_len):
        final = final + msg[perm_tab[i] - 1]
    return final


def key_perm_choice1(msg):
    pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

    final = ""
    bin_val = h2b(msg)
    pc1_len = len(pc1)
    for i in range(0, pc1_len):
        final = final + str(bin_val[pc1[i] - 1])

    print("Resultant 56 Bit key:", final)
    hex_val = b2h(final)
    return hex_val


def lc_shift(msg):
    #   round = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    bit_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    key = key_perm_choice1(msg)
    key = h2b(key)
    keys = []
    for i in range(0, 16):
        if bit_shift[i] == 1:
            # left circular shift
            left_val = key[0:28]
            right_val = key[28:56]
            left = left_val[1:] + left_val[0]
            right = right_val[1:] + right_val[0]
            final = left + right
            key = final
            keys = keys + [b2h(final)]
        if bit_shift[i] == 2:
            left_val = key[0:28]
            right_val = key[28:56]
            left = left_val[2:] + left_val[0] + left_val[1]
            right = right_val[2:] + right_val[0] + right_val[1]
            final = left + right
            key = final
            keys = keys + [b2h(final)]

    print("SubKeys:", keys[0:4])
    print("SubKeys:", keys[4:8])
    print("SubKeys:", keys[8:12])
    print("SubKeys:", keys[12:16])
    print("----------------------------------------------------------------------------------")
    return keys


def lc_shift_dec(msg):
    #   round = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    bit_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    key = key_perm_choice1(msg)
    key = h2b(key)
    keys = []
    for i in range(0, 16):
        if bit_shift[i] == 1:
            # left circular shift
            left_val = key[0:28]
            right_val = key[28:56]
            left = left_val[1:] + left_val[0]
            right = right_val[1:] + right_val[0]
            final = left + right
            key = final
            keys = keys + [b2h(final)]
        if bit_shift[i] == 2:
            left_val = key[0:28]
            right_val = key[28:56]
            left = left_val[2:] + left_val[0] + left_val[1]
            right = right_val[2:] + right_val[0] + right_val[1]
            final = left + right
            key = final
            keys = keys + [b2h(final)]

    print("SubKeys:", keys[0:4])
    print("SubKeys:", keys[4:8])
    print("SubKeys:", keys[8:12])
    print("SubKeys:", keys[12:16])
    print("----------------------------------------------------------------------------------")
    return keys[::-1]


def key_gen_perm_choice2(msg):
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    bin_val = h2b(msg)
    pc2_len = len(pc2)
    final = ""
    for i in range(0, pc2_len):
        final = final + str(bin_val[pc2[i] - 1])
    hex_val = b2h(final)
    return hex_val


def final_perm(msg):
    inv_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]

    final = ""
    bin_val = h2b(msg)
    ip_len = len(inv_perm)
    for i in range(0, ip_len):
        final = final + str(bin_val[inv_perm[i] - 1])

    hex_val = b2h(final)
    return hex_val


def valid_msg_block_size(msg):
    m_len = len(msg)
    final = msg
    if m_len % 16 != 0:
        print("Not a valid size block")
        for i in range(abs(16 - (m_len % 16))):
            final = final + "0"
        print("After filler:", final)
        return final
    else:
        print("Valid size block")
    return msg


def valid_key_block_size(msg):
    m_len = len(msg)
    final = msg
    if m_len % 48 != 0:
        print("Not a valid size block")
        for i in range(abs(48 - (m_len % 48))):
            final = final + "0"
        print("After filler:", final)
        return final
    else:
        print("Valid size block")
    return msg


def des_encryption(plaintext, key):
    print("----------------------------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////////////////////////")
    print("************************************Encryption************************************")
    print("//////////////////////////////////////////////////////////////////////////////////")
    # initial perm
    ip = h2b(init_perm(plaintext))
    left = ip[0:32]
    right = ip[32:64]
    lst = []
    keys = lc_shift(key)
    for i in range(0, 16):
        subkey = h2b(key_gen_perm_choice2(keys[i]))
        encode = expansion_perm(right)
        # s box input
        xor_output = xor(encode, subkey)
        s_box_output = substitution_box(xor_output)
        permutation_output = permutation(s_box_output)
        # po = permutation_output
        po_and_left_xor = xor(permutation_output, left)
        final = right + po_and_left_xor
        left = right
        right = po_and_left_xor
        lst = lst + [b2h(final)]

    tmp = lst[len(lst) - 1]
    swap = tmp[8:16] + tmp[0:8]

    return final_perm(swap)


def des_decryption(ciphertext, key):
    print("//////////////////////////////////////////////////////////////////////////////////")
    print("************************************Decryption************************************")
    print("//////////////////////////////////////////////////////////////////////////////////")
    # initial perm
    ip = h2b(init_perm(ciphertext))
    left = ip[0:32]
    right = ip[32:64]
    lst = []
    keys = lc_shift_dec(key)
    for i in range(0, 16):
        subkey = h2b(key_gen_perm_choice2(keys[i]))
        encode = expansion_perm(right)
        # s box input
        xor_output = xor(encode, subkey)
        s_box_output = substitution_box(xor_output)
        permutation_output = permutation(s_box_output)
        # po = permutation_output
        po_and_left_xor = xor(permutation_output, left)
        final = right + po_and_left_xor
        left = right
        right = po_and_left_xor
        lst = lst + [b2h(final)]

    tmp = lst[len(lst) - 1]
    swap = tmp[8:16] + tmp[0:8]

    return final_perm(swap)


def format1(msg):
    case = True
    if msg.islower():
        case = False
    return case


def format2(cipher, msg_len, case):
    if not case:
        cipher = cipher.lower()
        cipher = cipher[0: msg_len]
    else:
        cipher = cipher[0:msg_len]
    return cipher


print("----------------------------------------------------------------------------------")
message = input("Enter message in Hexadecimal (0-9, A-F): ")

mlen = len(message)
message_case = format1(message)
message = valid_msg_block_size(message.upper())

print("----------------------------------------------------------------------------------")
des_key = input("Enter Key in Hexadecimal (0-9, A-F): ").upper()
des_key = valid_key_block_size(des_key)

key1 = des_key[0:16]
key2 = des_key[16:32]
key3 = des_key[32:]

# ciphertext = E.K3(D.K2(E.K1(plaintext)))
enc_key1 = des_encryption(message, key1)  # E.K1(message)
dec_key2 = des_decryption(enc_key1, key2)  # D.K2(enc_key2)
enc_key3 = des_encryption(dec_key2, key3)  # E.K3(dec_key3)

print("Encrypted message:", enc_key3)
print("----------------------------------------------------------------------------------")

# plaintext = D.K1(E.K2(D.K3(ciphertext)))
dec_key3 = des_decryption(enc_key3, key3)  # D.K3(ciphertext)
enc_key2 = des_encryption(dec_key3, key2)  # E.K2(dec_key3)
dec_key1 = des_decryption(enc_key2, key1)  # D.K1(enc_key2)

res = format2(dec_key1, mlen, message_case)
print("Decrypted message:", res)
print("----------------------------------------------------------------------------------")
