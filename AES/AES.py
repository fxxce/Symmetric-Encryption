# https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture8.pdf
# http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html

def h2b(val):
    hex_val = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
               "4": "0100", "5": "0101", "6": "0110", "7": "0111",
               "8": "1000", "9": "1001", "a": "1010", "b": "1011",
               "c": "1100", "d": "1101", "e": "1110", "f": "1111"}
    m_len = len(val)
    final = ""
    for i in range(0, m_len):
        final = final + hex_val[val[i]]
    return final


def b2h(val):
    bin_val = {"0000": "0", "0001": "1", "0010": "2", "0011": "3",
               "0100": "4", "0101": "5", "0110": "6", "0111": "7",
               "1000": "8", "1001": "9", "1010": "a", "1011": "b",
               "1100": "c", "1101": "d", "1110": "e", "1111": "f"}
    m_len = len(val)
    lst = []
    final = ""
    count = 0
    i = 0
    while count != m_len:
        lst = lst + [val[count:count + 4]]
        final = final + bin_val[lst[i]]
        i = i + 1
        count = count + 4

    return final


def substitution_box(rc):
    hex_val = {"0": "0", "1": "1", "2": "2", "3": "3",
               "4": "4", "5": "5", "6": "6", "7": "7",
               "8": "8", "9": "9", "a": "10", "b": "11",
               "c": "12", "d": "13", "e": "14", "f": "15"}

    rijndael_s_box = [["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
                      ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
                      ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
                      ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
                      ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
                      ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
                      ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
                      ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
                      ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
                      ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
                      ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
                      ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
                      ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
                      ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
                      ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
                      ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]]

    substitution = rijndael_s_box[int(hex_val[rc[0]])][int(hex_val[rc[1]])]
    return substitution


def xor(left, right):
    final = ""
    l_len = len(left)
    for i in range(0, l_len):
        if left[i] == right[i]:
            final = final + '0'
        elif left[i] != right[i]:
            final = final + '1'
    return final


def col_to_row(val):
    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            col = col + [val[j][i]]
        row = row + [col]
    return row


def row_to_col(val):
    col = []
    for i in range(0, 4):
        row = []
        for j in range(0, 4):
            row = row + [val[j][i]]
        col = col + [row]
    return col


# it replaces every state element from its respective position in s-box
# row = first four bits or first value, and col = next four bits or next value
def substitute_byte(state):
    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            col = col + [substitution_box(state[i][j])]
        row = row + [col]
    return row


# circular left shift by row no. that is for row 0 shift by 0
# for row 1 shift by 1, for row 2 shift by 2 and for row 3 shift by 3
def shift_row(sub_bytes):
    state_array = []

    first = sub_bytes[0]
    state_array = state_array + [first]

    # row [1, 2, 3, 4] --> [2, 3, 4, 1]
    second = [sub_bytes[1][1]] + [sub_bytes[1][2]] + [sub_bytes[1][3]] + [sub_bytes[1][0]]
    state_array = state_array + [second]

    # row [1, 2, 3, 4] --> [3, 4, 1, 2]
    third = [sub_bytes[2][2]] + [sub_bytes[2][3]] + [sub_bytes[2][0]] + [sub_bytes[2][1]]
    state_array = state_array + [third]

    # row [1, 2, 3, 4] --> [4, 1, 2, 3]
    four = [sub_bytes[3][3]] + [sub_bytes[3][0]] + [sub_bytes[3][1]] + [sub_bytes[3][2]]
    state_array = state_array + [four]

    return state_array


# implementation of multiplication by 2 in galois field (0x02)
def multiply_by_02(inp):
    bin_val = h2b(inp[0]) + h2b(inp[1])
    final = ""
    if bin_val[0] == '1':
        # zero fill left shift
        bin_val = bin_val[1:len(bin_val)] + '0'
        # XORing the result with 0x1b
        final = xor(bin_val, h2b('1b'))
    elif bin_val[0] == '0':
        final = bin_val[1:len(bin_val)] + '0'

    return final


# implementation of multiplication by 3 in galois field (0x03)
# example: 0x03 * num = (0x02 + 0x01) * num = num * 0x02 + 0x01 * num
def multiply_by_03(inp):
    mix = multiply_by_02(inp)
    # addition in galois field is xor
    final = xor(mix, h2b(inp))

    return final


# predefined matrix
#      ↓
# 02 03 01 01         s0.0 s0,1 s0,2 s0,3         s′0.0 s′0,1 s′0,2 s′0,3
# 01 02 03 01         s1.0 s1,1 s1,2 s1,3         s′1.0 s′1,1 s′1,2 s′1,3
# 01 01 02 03         s2.0 s2,1 s2,2 s2,3         s′2.0 s′2,1 s′2,2 s′2,3
# 03 01 01 02         s3.0 s3,1 s3,2 s3,3         s′3.0 s′3,1 s′3,2 s′3,3
#      ↑                       ↑                             ↑
#     row         x          column          =             Result      (Additions involved here are XOR)
# implementation of this is below

# s′0,j = (0x02 × s0,j) ⊗ (0x03 × s1,j ) ⊗ s2,j ⊗ s3,j
def row0(row):
    xor01 = xor(multiply_by_02(row[0]), multiply_by_03(row[1]))
    xor23 = xor(h2b(row[2]), h2b(row[3]))
    final_xor = xor(xor01, xor23)

    return b2h(final_xor)


# s′1,j = s0,j ⊗ (0x02 × s1,j) ⊗ (0x03 × s2,j) ⊗ s3,j
def row1(row):
    xor01 = xor(h2b(row[0]), multiply_by_02(row[1]))
    xor23 = xor(multiply_by_03(row[2]), h2b(row[3]))
    final_xor = xor(xor01, xor23)

    return b2h(final_xor)


# s′2,j = s0,j ⊗ s1,j ⊗ (0x02 × s2,j ) ⊗ (0x03 × s3,j)
def row2(row):
    xor01 = xor(h2b(row[0]), h2b(row[1]))
    xor23 = xor(multiply_by_02(row[2]), multiply_by_03(row[3]))
    final_xor = xor(xor01, xor23)

    return b2h(final_xor)


# s′3,j = (0x03 × s0,j) ⊗ s1,j ⊗ s2,j ⊗ (0x02 × s3,j)
def row3(row):
    xor01 = xor(multiply_by_03(row[0]), h2b(row[1]))
    xor23 = xor(multiply_by_02(row[3]), h2b(row[2]))
    final_xor = xor(xor01, xor23)

    return b2h(final_xor)


def mix_col(s_row):
    final_row = []
    for i in range(0, 4):
        tmp_row = [row0(s_row[i])] + [row1(s_row[i])] + [row2(s_row[i])] + [row3(s_row[i])]
        final_row = final_row + [tmp_row]

    return final_row


def key_expansion(s_key, rnd):
    keys = []

    # Rcon = 128 -> 10, 192 -> 8, 256 -> 7
    # Rcon =  [01, 02, 04, 08, 10, 20, 40, 80, 1b, 36]
    # Rcon(i) = [rc(i), 00(0x), 00(0x), 00(0x)]
    # Rcon = [["01", "00", "00", "00"], ["02", "00", "00", "00"], ["04", "00", "00", "00"], ["08", "00", "00", "00"],
    #         ["10", "00", "00", "00"], ["20", "00", "00", "00"], ["40", "00", "00", "00"], ["80", "00", "00", "00"],
    #         ["1b", "00", "00", "00"], ["36""00", "00", "00"]]

    for pos in range(0, 4):
        if pos == 0:
            first_col = []
            tmp = s_key[3]
            t_len = len(tmp)

            for i in range(1, t_len):
                first_col = first_col + [tmp[i]]
            first_col = first_col + [tmp[0]]
            col = []

            f_len = len(first_col)
            for i in range(0, f_len):
                col = col + [substitution_box(first_col[i])]

            tmp_key = []
            for i in range(0, 4):
                sub_key = xor(h2b(s_key[0][i]), h2b(rnd[i]))
                sub_key1 = xor(sub_key, h2b(col[i]))
                tmp_key = tmp_key + [str(b2h(sub_key1))]

            keys = keys + [tmp_key]

        elif pos > 0:
            first_col = []

            for i in range(0, 4):
                sub_key = xor(h2b(s_key[pos][i]), h2b(keys[pos - 1][i]))
                first_col = first_col + [str(b2h(sub_key))]

            keys = keys + [first_col]
    return keys


def add_round(plain_text, keys):
    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            tmp = xor(h2b(keys[i][j]), h2b(plain_text[i][j]))
            col = col + [b2h(tmp)]
        row = row + [col]

    return col_to_row(row)


# checking if entered text is of valid size, and adding fillers
def valid_block_size(msg):
    m_len = len(msg)
    final = msg
    if m_len > 32:
        print("Not a valid size block, Exceeding Block size!")
        final = final[0:32]
        print("After filler:", final)
        return final
    elif m_len % 32 != 0:
        print("Not a valid size block")
        for i in range(abs(32 - (m_len % 32))):
            final = final + "0"
        print("After filler:", final)
        return final
    else:
        print("Valid size block")
    return msg


def key_and_text_to_matrix(key_string):
    arr = [["00" for _ in range(4)] for _ in range(4)]
    row = 0
    col = 0
    for i in range(0, len(key_string), 2):
        if row < 4 and col < 4:
            if len(key_string[i:i + 2]) == 1:
                arr[row][col] = key_string[i:i + 2] + "0"
            else:
                arr[row][col] = key_string[i:i + 2]
            col = col + 1
            if col > 3:
                row = row + 1
                col = 0
    return arr


rnd_const = [["01", "00", "00", "00"], ["02", "00", "00", "00"], ["04", "00", "00", "00"], ["08", "00", "00", "00"],
             ["10", "00", "00", "00"], ["20", "00", "00", "00"], ["40", "00", "00", "00"], ["80", "00", "00", "00"],
             ["1b", "00", "00", "00"], ["36", "00", "00", "00"]]


def aes_encryption(plain_text, aes_key):
    add_round_key = add_round(plain_text, aes_key)
    sub_byte = substitute_byte(add_round_key)
    shift_rows = shift_row(sub_byte)
    mix_column = mix_col(row_to_col(shift_rows))
    add_round_key = add_round(mix_column, key_expansion(aes_key, rnd_const[0]))
    aes_key = key_expansion(aes_key, rnd_const[0])

    for i in range(1, 9):
        tmp_key = key_expansion(aes_key, rnd_const[i])
        aes_key = tmp_key
        sub_byte = substitute_byte(add_round_key)
        shift_rows = shift_row(sub_byte)
        mix_column = mix_col(row_to_col(shift_rows))
        add_round_key = add_round(mix_column, aes_key)

    sub_byte = substitute_byte(add_round_key)
    shift_rows = row_to_col(shift_row(sub_byte))
    tmp_key = key_expansion(aes_key, rnd_const[9])
    aes_key = tmp_key
    add_round_key = add_round(shift_rows, aes_key)

    cipher = ""
    for row in range(0, len(add_round_key)):
        for col in range(0, 4):
            cipher = cipher + add_round_key[col][row]
    return cipher


plaintext = input("Enter text: ")
valid_pt_block = valid_block_size(plaintext)
plaintext_matrix = key_and_text_to_matrix(plaintext)
print("Plaintext Block:", plaintext_matrix)
print("---------------------------------------------------------------------------------------------------------------")

key = input("Enter key: ")
valid_k_block = valid_block_size(key)
key_matrix = key_and_text_to_matrix(key)
print("Key Block:", key_matrix)
print("---------------------------------------------------------------------------------------------------------------")

cipher_text = aes_encryption(plaintext_matrix, key_matrix)
print("Encrypted Text: ", cipher_text)
print("---------------------------------------------------------------------------------------------------------------")
