def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b >= c and b + c >= a and a + c >= b) and (a == b == c != 0) :  #If the 3 points form a triangle and the distance between each point is equal returns True, otherwise, False.
        return True
    else : 
        return False
        
def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2] 
    if (a + b >= c and b + c >= a and a + c >= b) and (a == b or b == c or c == a): #If the 3 points form a triangle and the distance between two point is equal returns True, otherwise, False.
         return True
    else :
         return False

    


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b >= c and b + c >= a and a + c >= b) and (a != b and b != c and c != a):  #If the 3 points form a triangle and the distance between each point is not equal returns True, otherwise, False.
         return True
    else :
         return False
