

def caesar_encrypt(text, shift):
    result = ""  
    for char in text:
        
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        else:
            result += char
    
    return result


def caesar_decrypt(ciphertext, shift):
    result = ""
    
    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        
        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        
        else:
            result += char
    
    return result


if __name__ == "__main__":
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    encrypted = caesar_encrypt(text, shift)
    print("Encrypted Text:", encrypted)
    
    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Text:", decrypted)