import string 
def rotate(text, key):
    alphabet = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    lst_encrypted_text = []
    
    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + key) % len(alphabet)
            lst_encrypted_text += alphabet[new_index]
        elif char in alphabet_upper:
            index = alphabet_upper.find(char)
            new_index = (index + key) % len(alphabet_upper)
            lst_encrypted_text += alphabet_upper[new_index]
        else:
            lst_encrypted_text += char
    return "".join(lst_encrypted_text)