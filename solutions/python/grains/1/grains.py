def square(number):
    if number < 1 or number > 64:  
        raise ValueError("square must be between 1 and 64")
    
    grain_per_square = 1  
    for _ in range(1, number):  
        grain_per_square *= 2 
    
    return grain_per_square  

def total():
    total_squares = 64
    total = 0
    for i in range(total_squares):
        total += square(i+1)
    return total
        
