import sys
from os.path import exists as file_exists

def xor(text, key):
    decrypted = []
    for i in range(0, len(text)):
        decrypted.append(text[i] ^ key[i % len(key)])
    return bytes(decrypted)

if len(sys.argv) == 4:
    key = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if file_exists(input_file):
        with open(input_file, "rb") as IN:
            with open(output_file, "w") as OUT:
                decrypted = xor(IN.read(), key.encode()).decode()
                OUT.write(decrypted)
    else:
        print(f"'{input_file}' doesn't exist!")
else:
	print("usage: $python3 decrypt.py <key> <input> <output.txt>")
