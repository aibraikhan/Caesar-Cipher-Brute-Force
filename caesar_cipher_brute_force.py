text = input("Напишите защифрованный текст на Английском языке: \n").upper()

for i in range(1, 26):
    shift = i

    decrypted = ""
    for char in text:
        if char.isalpha():
            dec = ((ord(char) - 65) - shift) % 26
            decrypted += chr(dec + 65)
        else:
            decrypted += char

    print(f"Сдвиг {i}: {decrypted}")