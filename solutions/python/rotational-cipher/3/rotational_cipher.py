import string

def rotate(text, key):
    key = key % 26  #So it wont break if key input is beyond len(alphabet)
    rotated_lower = string.ascii_lowercase[key:] + string.ascii_lowercase[:key] #shifting mecanism using slicers, pushes initial slice to END.
    rotated_upper = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]

    translation_table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,rotated_lower + rotated_upper) #the mapping table for actual translation

    return text.translate(translation_table)