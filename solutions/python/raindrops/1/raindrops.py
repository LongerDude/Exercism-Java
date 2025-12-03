def convert(number):
    word = ""
    sounds = ["Pling", "Plong", "Pland"]
    if number % 3 == 0:
        word += "Pling"
    if number % 5 == 0:
        word += "Plang"
    if number % 7 == 0:
        word += "Plong"
    if word:
        return word
    else : 
        return str(number)