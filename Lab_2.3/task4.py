def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('А') if char.isupper() else ord('а')
            new_char = chr((ord(char) - base + shift) % 32 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


def encrypt_file():
    try:
        with open('secret.txt', 'r', encoding='utf-8') as f:
            text = f.read()

        encrypted = caesar_cipher(text, 3)

        with open('encrypted.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted)

        print("Файл зашифрован: encrypted.txt")
        return encrypted

    except FileNotFoundError:
        print("Ошибка: secret.txt не найден")
        return None


def decrypt_file():
    try:
        with open('encrypted.txt', 'r', encoding='utf-8') as f:
            encrypted = f.read()

        decrypted = caesar_cipher(encrypted, -3)

        with open('decrypted.txt', 'w', encoding='utf-8') as f:
            f.write(decrypted)

        print("Файл расшифрован: decrypted.txt")
        return decrypted

    except FileNotFoundError:
        print("Ошибка: encrypted.txt не найден")
        return None

print (encrypt_file(), decrypt_file())