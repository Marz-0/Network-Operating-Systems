def caesar_cipher(text, shift, encrypt=True):
    """
    General Caesar cipher for encryption and decryption
    """
    if not encrypt:
        shift = 26 - shift
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset))
        else:
            result.append(char)
    return ''.join(result)

def encrypt(text, shift=3):
    """
    Caesar cipher encryption
    """
    return caesar_cipher(text, shift, encrypt=True)

def decrypt(text, shift=3):
    """
    Caesar cipher decryption
    """
    return caesar_cipher(text, shift, encrypt=False)