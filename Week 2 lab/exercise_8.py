
#Exercise 7 - ceaser cipher

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

# Ask for user input
message = input("Enter the message: ")
key = int(input("Enter the shift key: "))
mode = input("Do you want to encrypt or decrypt? ").strip().lower()

# Print the result based on the mode
if mode == "encrypt":
    print("Encrypted:", caesar_cipher(message, key, "encrypt"))
elif mode == "decrypt":
    print("Decrypted:", caesar_cipher(message, key, "decrypt"))
else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

