def is_isogram(string):
    word_as_list = list(string.lower())
    review = ""
    for char in word_as_list:
        if char not in review :
            if char.isalnum():
                review += char
            else :
                continue
        else :
            return False
    return True