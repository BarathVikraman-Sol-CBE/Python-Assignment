""" Program to classify the number using conditional statements """

def classify_number(number:int) -> str:
    """
    Function to classify a number using conditional statements

    Args :
        number : an integer to classify.
    
    Returns :
        - zero : if number is zero.
        - positive : if number is positive.
        - negative : if number is negative.
    """

    if number < 0:
        return "negative"
    elif number == 0:
        return "zero"
    else:
        return "positive"


def main() -> None :

    print(classify_number(-1))
    print(classify_number(0))
    print(classify_number(1))


if __name__ == "__main__":
    main()