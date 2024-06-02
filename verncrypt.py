import sys
import random

# Banner to be displayed
def display_banner():
    print("""\033[95m
    __   __   ______     ______     __   __     ______     ______     __  __     ______   ______  
    /\ \ / /  /\  ___\   /\  == \   /\ "-.\ \   /\  ___\   /\  == \   /\ \_\ \   /\  == \ /\__  _\ 
    \ \ \'/   \ \  __\   \ \  __<   \ \ \-.  \  \ \ \____  \ \  __<   \ \____ \  \ \  _-/ \/_/\ \/ 
    \ \__|    \ \_____\  \ \_\ \_\  \ \_\\"\_\  \ \_____\  \ \_\ \_\  \/\_____\  \ \_\      \ \_\ 
    \/_/      \/_____/   \/_/ /_/   \/_/ \/_/   \/_____/   \/_/ /_/   \/_____/   \/_/       \/_/ 
                                                                                                
    \033[0m
    """)

def print_instructions():
    instructions = """
\033[92m
Welcome to VernCrypt - A simple Vernam cipher encryption/decryption tool.

Usage:
    1. Encrypt a message:
       verncrypt  -e "your message"  "your key[optional]"
    
    2. Decrypt a message:
       verncrypt -d "your encrypted message"  "your key"

Note:
    - The key must be the same length as the message.
    - Use double quotes for messages and keys with spaces.
    - Works better for alphabetic messages.
\033[0m
"""
    print(instructions)

def assign_codes():
    codes = {chr(i + 97): i for i in range(26)}
    inv_codes = {i: chr(i + 97) for i in range(26)}
    return codes, inv_codes

def generate_key(length):
    return ''.join(chr(random.randint(97, 122)) for _ in range(length))

def encrypt(text, key, codes, inv_codes):
    encrypted_text = ''
    for i in range(len(text)):
        sample = (codes[text[i]] + codes[key[i]]) % 26
        encrypted_text += inv_codes[sample]
    return encrypted_text

def decrypt(cryptext, key, codes, inv_codes):
    decrypted_text = ''
    for i in range(len(cryptext)):
        sample = (codes[cryptext[i]] - codes[key[i]] + 26) % 26
        decrypted_text += inv_codes[sample]
    return decrypted_text

if __name__ == "__main__":
    display_banner()
    print_instructions()
    codes, inv_codes = assign_codes()

    input_configs = input("\033[95m > \033[0m").split()

    if len(input_configs) < 3:
        print("Usage: verncrypt -e/-d <message> <key>[optional]")
        sys.exit(1)

    option = input_configs[1]
    text = input_configs[2].lower()

    if option == "-e":
        if len(input_configs) not in [3, 4]:
            print("Usage: verncrypt -e <message> <key>[optional]")
            sys.exit(1)
        
        if len(input_configs) == 4:
            key = input_configs[3].lower()
        else:
            key = generate_key(len(text))
        
        if len(key) != len(text):
            print("Key length must be equal to the message length")
            sys.exit(1)
        
        encrypted_text = encrypt(text, key, codes, inv_codes)
        print(f"Encrypted Text: {encrypted_text}")
        print(f"Key: {key}")

    elif option == "-d":
        if len(input_configs) != 4:
            print("Usage: verncrypt -d <encrypted message> <key>")
            sys.exit(1)
        
        key = input_configs[3].lower()
        
        if len(key) != len(text):
            print("Key length must be equal to the encrypted message length")
            sys.exit(1)
        
        decrypted_text = decrypt(text, key, codes, inv_codes)
        print(f"Decrypted Text: {decrypted_text}")

    else:
        print("Invalid option. Use -e to encrypt or -d to decrypt.")
        sys.exit(1)
