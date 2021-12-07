import sys
from os.path import exists as file_exists

def xor_key(a, b):
    key = ""
    for i in range(30):
        key += chr(a[i] ^ b[i])
    for i in range(10, 16):
        if key[:i] == key[i:2*i]:
            return key[:i]
   
if len(sys.argv) == 3 and file_exists(sys.argv[1]) and file_exists(sys.argv[2]):
    txt_file = sys.argv[1]
    bin_file = sys.argv[2]
    with open(txt_file, "rb") as IN_TXT:
        with open(bin_file, "rb") as IN_BIN:
            key = xor_key(IN_TXT.read(30), IN_BIN.read(30))
            print(key)
else:
	print("usage: $python3 encrypt.py <text file> <binary file>")
