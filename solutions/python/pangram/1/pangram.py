def is_pangram(sentence):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    found_letters = []
    for char in sentence.lower():
        if 'a' <= char <= 'z' and char not in found_letters:
            found_letters.append(char)
    return all(letter in found_letters for letter in alphabet_list)