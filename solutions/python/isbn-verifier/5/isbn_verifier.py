def is_valid(isbn):
    allowed_chars = "0123456789X- "

    for char in isbn:
        if char.upper() not in allowed_chars:
            return False

    cleaned_isbn = [c.upper() for c in isbn if c.isdigit() or c.upper() == 'X']

    if len(cleaned_isbn) != 10:
        return False
    if 'X' in cleaned_isbn[:-1]:
        return False

    if cleaned_isbn[-1] == 'X':
        cleaned_isbn[-1] = '10'
    
    the_sum = sum(int(ch) * (10 - pos) for pos, ch in enumerate(cleaned_isbn))

    return the_sum % 11 == 0
