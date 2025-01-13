""" Program to invert a dictionary by converting values into keys and keys into list of values """

from collections import defaultdict
from typing import Dict,Any,List


def invert_dict(input_dict:Dict[Any,Any]) -> Dict[Any,List[Any]] :
    """
    Function to invert the dictionary.
    
    Args :
        input_dict : dictionary with keys and values.

    Returns :
        Returns the inverted dictionary.
    """
    
    new_dict : Dict[Any,List[Any]] = {}

    for key,value in input_dict.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)

    return new_dict
    """ Alternative approach using defaultdict
    new_dict : Dict[Any,List[Any]] = defaultdict(list)
    for key,value in input_dict.items():
        new_dict[value].append(key)
    """

def main() -> None :
     
    dictionary  = {"a":1,"b":1,"C":2,"D":2}
    inverted_dict = invert_dict(dictionary)

    print(inverted_dict)


if __name__ == "__main__" : 
    main()