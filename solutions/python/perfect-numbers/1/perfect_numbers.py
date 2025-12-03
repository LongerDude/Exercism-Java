def classify(n):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    def aliquot_sum(n):
        return sum(i for i in range(1, n) if n % i == 0)
    if n > aliquot_sum(n):
        return 'deficient'
    if aliquot_sum(n) == n:
        return 'perfect'
    if n < aliquot_sum(n):
        return 'abundant'
   
    
