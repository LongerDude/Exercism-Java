def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet.upper()
    encrypted_text = ''
    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]
        elif char in alphabet_upper:
            index = alphabet_upper.find(char)
            new_index = (index + key) % len(alphabet_upper)
            encrypted_text += alphabet_upper[new_index]
        else:
            encrypted_text += char
    return encrypted_text