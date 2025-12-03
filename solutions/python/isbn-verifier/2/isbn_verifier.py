def is_valid(isbn):
    #Validating1
    allowed_chars = "0123456789X- "
    for char in isbn:
        if char.upper() not in allowed_chars:
            return False 
    #Cleaning
    cleaned_isbn = [c.upper() for c in isbn if c.isdigit() or c.upper() == 'X']
    #Validating2
    if len(cleaned_isbn) == 10 and ('X' not in cleaned_isbn or cleaned_isbn[-1] == 'X') : 
        the_sum = 0
        count = 10
        for nmb in cleaned_isbn:
            if nmb == 'X':
                the_sum += 10 * count
            else : 
                the_sum += int(nmb) * count
                count -= 1
    #ISBN LOGIC
        if the_sum % 11 == 0:
            return True
        else: 
            return False
    else:
        return False
        
        
