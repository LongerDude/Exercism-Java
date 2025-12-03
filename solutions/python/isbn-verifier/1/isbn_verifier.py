def is_valid(isbn):
    for char in isbn:
        if not (char.isdigit() or char.upper() == 'X' or char == '-' or char == ' '):
            return False
    cleaned_isbn = [c.upper() for c in isbn if c.isdigit() or c.upper() == 'X']
    if len(cleaned_isbn) == 10 and ('X' not in cleaned_isbn or cleaned_isbn[-1] == 'X') : 
        the_sum = 0
        count = 10
        for nmb in cleaned_isbn:
            if nmb == 'X':
                the_sum += 10 * count
            else : 
                the_sum += int(nmb) * count
                count -= 1
        if the_sum % 11 == 0:
            return True
        else: 
            return False
    else:
        return False
        
        
