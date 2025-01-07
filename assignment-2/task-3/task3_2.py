""" Program to calculate the factorial of a given integer """

def factorial(number:int) -> int :
    """
    Function to calculate the factorial of an integer.

    Args :
        number : Integer to calculate factorial.

    Returns :
        Factorial of the given integer.
    """

    fact:int = 1 

    for num in range(2,number+1):
        fact *= num

    return fact

def main() -> None:
    
    number:int = int(input("Enter a number : "))
    print(f"Factorial of {number} is {factorial(number)}")


if __name__ == "__main__" : 
    main()