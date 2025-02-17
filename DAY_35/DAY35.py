import argparse

def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift_amount) % 26) + 97)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext):
    decrypted_texts = []
    for shift in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                new_char = chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 - shift) % 26) + 97)
                decrypted += new_char
            else:
                decrypted += char
        decrypted_texts.append((shift, decrypted))
    return decrypted_texts

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt messages using Caesar Cipher.")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("text", help="Text to encrypt or decrypt")
    parser.add_argument("--shift", type=int, help="Shift value for encryption", default=3)

    args = parser.parse_args()

    if args.action == "encrypt":
        result = caesar_encrypt(args.text, args.shift)
        print("Encrypted:", result)
    elif args.action == "decrypt":
        decrypted_texts = caesar_decrypt(args.text)
        for shift, decrypted in decrypted_texts:
            print(f"Shift {shift}: {decrypted}")

if __name__ == "__main__":
    main()