def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True

    # Check for divisibility by 2 and 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # For larger numbers, check divisibility up to the square root of the number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True