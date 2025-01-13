""" Program to filter prime numbers from a list of integers """

from typing import List

def is_prime(num:int) -> bool :
    """
    Function to check whether a number is prime or not.

    Args :
        num : an integer to check whether it is prime.

    Returns :
        A boolean value indicating it is prime or not.
    """

    if num == 2 or num == 3 :
        return True

    if num < 2 or num % 3 == 0 or num % 2 == 0 :
        return False

    if num % 6 in (2,3,4,0) : 
        return False

    for factor in range(5,int(num**0.5)+1,2):
        if num % factor == 0 :
            return False
    
    return True
    
def filter_primes(numbers:List[int]) -> List[int] :
    """
    Function to filter prime numbers from list of integers.

    Args :
        numbers : List of integers.
    
    Returns :
        Returns a filtered list of integers with only prime numbers.
    """

    filtered_numbers : List[int] = []

    for number in numbers:
        if is_prime(number):
            filtered_numbers.append(number)
    return filtered_numbers
    
    """ Alternative approach
    filtered_numbers = [num for num in numbers if is_prime(num)]
    return filtered_numbers

    Built-in method
    return list(filter(is_prime,numbers))
    """

def main() -> None :

    numbers : List[int] = [num for num in range(10000)]

    filtered_nums : List[int] = filter_primes(numbers)

    print(filtered_nums)


if __name__ == "__main__" :
    main()