""" Program a function to return True if atleast two conditions are true"""

def evaluate_conditions(a:bool, b:bool, c:bool) -> bool :
    """
    Function to check atleast two conditions are true.

    Args :
        a : boolean value
        b : boolean value
        c : boolean value

    Returns :
        If any two values are true, returns True. Otherwise False. 
    """

    # return a+b+c >= 2
    return (a and b) or (b and c) or (a and c) 


def main() -> None:

    exp_1 : bool = input("Enter true or false : ") == "true"
    exp_2 : bool = input("Enter true or false : ") == "true"
    exp_3 : bool = input("Enter true or false : ") == "true"

    print(evaluate_conditions(exp_1,exp_2,exp_3))


if __name__ == "__main__":
    main()