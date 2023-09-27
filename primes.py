"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    """for num in range(2, number_of_primes + 2):
          for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            list.append(num)
            """
    count = 1
    while len(list) < number_of_primes:
        count += 1
        isPrime = True
        for num in range(2, count):
            if count % num == 0:
                isPrime = False
                break

        if isPrime:
            list.append(count)


    return list
