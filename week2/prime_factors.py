def prime_factors(n):
    """
    Find all prime factors of a given number.

    Args:
        n (int): The number to factorize.

    Returns:
        list: A list of prime factors of n.
    """
    # checking if the number is an integer
    if not isinstance(n, int):
        raise ValueError(f"The number has to be integer, but {n} provided")

    factors = []
    # Handle the factor of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Handle odd factors from 3 upwards
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 2, it must be prime
    if n > 2:
        factors.append(n)

    return factors
