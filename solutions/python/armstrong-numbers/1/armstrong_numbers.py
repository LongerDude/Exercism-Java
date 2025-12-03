def is_armstrong_number(number):
    res = [int(x) for x in str(number)]
    digits_length = len(res)
    New_Numbers = list(map(lambda x: x**digits_length, res))  
    sumofnumb = sum(New_Numbers)
    if number == sumofnumb:
        return True
    else: 
        return False
