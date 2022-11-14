def msg_mat(msg):
    msg_cp = msg
    end = len(msg_cp) % 3
    rem = 3 - end

    if end != 0:
        while rem != 0:
            msg_cp = msg_cp + 'z'
            rem = rem - 1
    # final length
    flen = len(msg_cp)
    i = 0
    msg_mtx = []

    while i != flen:
        msg_char = ''
        # check 3
        chk3 = 0
        while chk3 != 3:
            msg_char = msg_char + msg_cp[i + chk3]
            chk3 = chk3 + 1

        msg_mtx = msg_mtx + [msg_char]
        i = i + 3

    return msg_mtx


def key_mat(key):
    klen = len(key)
    j = 0
    key_mtx = []
    while klen > 0:
        key_char = ''
        k = 0
        while k != 3:
            key_char = key_char + key[j + k]
            k = k + 1

        key_mtx = key_mtx + [key_char]
        j = j + 3
        klen = klen - 3
    return key_mtx


def encryption_hc(msg, key):
    msg_mtx = msg_mat(msg)
    key_mtx = key_mat(key)

    msg_rows = len(msg_mtx)
    count = 0
    encrypted_msg = ''

    while count != msg_rows:
        key_ind = 0
        while key_ind != 3:
            temp = 0
            mul_sum = 0
            while temp != 3:
                key_char = ord(key_mtx[key_ind][temp]) % 97
                msg_char = ord(msg_mtx[count][temp]) % 97
                mul_sum = mul_sum + (msg_char * key_char)
                temp = temp + 1

            encrypted_msg = encrypted_msg + chr((mul_sum % 26) + 97)
            key_ind = key_ind + 1
        count = count + 1
    return encrypted_msg


message = input("Enter Text: ")
# Key value
key = "hillciphr"
encrypted_message = encryption_hc(message, key)
print("Original Text: " + message)
print("Cipher Text: " + encrypted_message)
