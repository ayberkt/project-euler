import itertools
from operator import xor

cipher = open("cipher1.txt")
cipher_content = cipher.read()
chars = cipher_content.split(",")

char_codes = range(97, 122)
key_bin_codes = []

for char_tuple in list(itertools.combinations(char_codes, 3)):
    key = ""
    for char in char_tuple:
        key += bin(char)[2:]
    key_bin_codes.append(key * 2)


cipher_codes = []
total_length = 0
for char in chars:
    char_bin_code = bin(int(char))[2:]
    cipher_codes.append(char_bin_code)
    total_length += len(char_bin_code)

# print cipher_codes[:6]

total = 0

decipher_letter = ""
for key_bin in key_bin_codes:
    current_key_bin = key_bin
    for cipher_letter in cipher_codes[:7]:
        current_sub_key = current_key_bin[:len(cipher_letter)]
        current_key_bin = current_key_bin[:len(cipher_letter)]

        decipher_code = ""
        for i in range(len(cipher_letter)):
            decipher_code += str(xor(int(current_sub_key[i]), int(cipher_letter[i])))
        decipher_letter += chr(int(decipher_code, 2))
    print decipher_letter