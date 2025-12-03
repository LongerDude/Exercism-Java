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
    for digit in digits:
        result = result * input_base + digit

    if result == 0:
        return [0]
    while result > 0:
        result, remainder = divmod(result, output_base)
        new_digits.append(remainder)
    return new_digits[::-1]