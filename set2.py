def shift_letter(letter, shift):
    '''Shift Letter.'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        return " "

    index = 0
    while index < 26:
        if alphabet[index] == letter:
            return alphabet[(index + shift) % 26]
        index += 1

def caesar_cipher(message, shift):
    '''Caesar Cipher.'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in message:
        if char == " ":
            result += " "
        else:
            index = 0
            while index < 26:
                if alphabet[index] == char:
                    result += alphabet[(index + shift) % 26]
                    break
                index += 1
    return result

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        return " "

    shift = 0
    while shift < 26:
        if alphabet[shift] == letter_shift:
            return shift_letter(letter, shift)
        shift += 1

def vigenere_cipher(message, key):
    '''Vigenere Cipher.'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    key_index = 0
    key_length = len(key)

    for char in message:
        if char == " ":
            result += " "
        else:
            shift = 0
            while shift < 26:
                if alphabet[shift] == key[key_index % key_length]:
                    result += shift_letter(char, shift)
                    key_index += 1
                    break
                shift += 1
    return result

def scytale_cipher(message, shift):
    '''Scytale Cipher.'''
    while len(message) % shift != 0:
        message += "_"

    result = [""] * len(message)
    length = len(message)

    for i in range(length):
        new_position = (i // shift) + (length // shift) * (i % shift)
        result[new_position] = message[i]
    return "".join(result)

def scytale_decipher(message, shift):
    '''Scytale De-cipher.'''
    cols = len(message) // shift
    result = [""] * len(message)

    for i in range(len(message)):
        new_position = (i // cols) + shift * (i % cols)
        result[new_position] = message[i]
    return "".join(result)

# Test
print(shift_letter("A", 2))  # output: "C"
print(shift_letter("Z", 1))  # output: "A"
print(shift_letter("X", 5))  # output: "C"

print(caesar_cipher("HELLO WORLD", 3))  # output: "KHOOR ZRUOG"

print(shift_by_letter("A", "C"))  # output: "C"
print(shift_by_letter("B", "K"))  # output: "L"

print(vigenere_cipher("ATTACK AT DAWN", "KEY"))  # output: "KXVVSN KY ECJR"

print(scytale_cipher("INFORMATION_AGE", 3))  # output: "IMNNA_FTAOIGROE"
print(scytale_decipher("IMNNA_FTAOIGROE", 3))  # output: "INFORMATION_AGE"
