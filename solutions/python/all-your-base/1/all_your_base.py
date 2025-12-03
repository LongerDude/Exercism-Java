def rebase(input_base, digits, output_base):
    if not isinstance(input_base, int) or input_base < 2:
        raise ValueError("input base must be >= 2")
    if not isinstance(output_base, int) or output_base < 2:
        raise ValueError("output base must be >= 2")
    if not isinstance(digits, list):
        raise ValueError("digits must be a list")
    if any(not isinstance(d, int) or d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    result = 0
    new_digits = []
    for index, digit in enumerate(digits[::-1]):
        result += digit * (input_base ** index)
    if result == 0:
        return [0]
    while not result == 0:
        new_digits.insert(0, result % output_base)
        result = result // output_base
    return new_digits
        