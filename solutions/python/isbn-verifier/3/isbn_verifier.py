def is_valid(isbn):
    #Validating1
    allowed_chars = "0123456789X- "
    for char in isbn:
        if char.upper() not in allowed_chars:
            return False        
    #Cleaning
    cleaned_isbn = [c.upper() for c in isbn if c.isdigit() or c.upper() == 'X']
    #Validating2
    if not (len(cleaned_isbn) == 10 and ('X' not in cleaned_isbn or cleaned_isbn[-1] == 'X')) : 
        return False
    else :
        the_sum = 0
        for pos, ch in enumerate(cleaned_isbn):
          if ch == 'X':
                the_sum += 10 
          else : 
                the_sum += int(ch) * (10-pos)
    #ISBN LOGIC
        return the_sum % 11 == 0
        
        
