def is_isogram(string):
    new_string = [char for char in string.lower() if char.isalpha()]
    return len(new_string) == len(set(new_string))
