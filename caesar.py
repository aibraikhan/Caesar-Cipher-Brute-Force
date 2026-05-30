while True:
    shift = input("Выберите ключ между 1 и 25: ")
    try:
        val = int(shift)
        break
    except ValueError:
        print("Это не цифра!")

text = input("Напишите текст: ")

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char == ' ':
            result += ' '
        elif (char.isupper()):
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    
    return result

def decrypt(encrypted_text, shift):
    result = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]

        if char == ' ':  # Skip spaces
            result += ' '
        elif (char.isupper()):
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    
    return result

def brute_force(cipher):
    for key in range (1, 26):
        print(f"Ключ {key}: {decrypt(cipher, key)}")


enc = encrypt(text, val)

print("Cipher: " + enc + '\n')
brute_force(enc)

# print("Cipher: " + decrypt(enc, val))
