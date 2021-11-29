import sys
from os.path import exists as file_exists

def xor(text, key):
    encrypted = []
    for i in range(0, len(text)):
        encrypted.append(text[i] ^ key[i % len(key)])
    return bytes(encrypted)
   
if len(sys.argv) == 4:   
    key = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if file_exists(input_file) and input_file.lower().endswith(('.txt', '.in')):
        with open(input_file, "r") as IN:
            with open(output_file, "wb") as OUT:
                encrypted = xor(IN.read().encode(), key.encode())
                OUT.write(encrypted)
    else:
        print(f"'{input_file}' doesn't exist or is not a text file!")
else:
	print("usage: $python3 encrypt.py <key> <input.txt> <output>")
