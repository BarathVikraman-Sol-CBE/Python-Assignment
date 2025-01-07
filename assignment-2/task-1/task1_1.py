""" Program to reverse words in a string without changing the order of the words"""


def reverse_word(word:str) -> str:
    """
    Function to reverse a single word.

    Args :
        words : Word to be reversed.
    
    Returns :
        Reversed string of the word.
    """

    rev_word : str = ""
    length : int = len(word) -1
    while length >= 0 :
        rev_word += word[length]
        length -= 1
    return rev_word

def reverse_words(input_str:str) -> str :
    """
    Function to reverse words in the single maintaining their relative order.

    Args :
        input_str : String of word(s) to be reversed.
    
    Returns :
        Reversed string of words with relative order.
    """

    rev_str : str = ""
    length : int = len(input_str)
    start : int = 0
    end : int = 0
    while end < length :
        if input_str[end] == " ":
            rev_str += reverse_word(input_str[start:end]) + " " 
            start = end + 1
        end += 1
    rev_str += reverse_word(input_str[start:end]) # If there is no space in the string or there is only on word in the string
    return rev_str

    """Alternative Solution  Using Built-in methods
    rev_str : str = ""
    for word in input_str.split(" "):
        rev_str += word[::-1] + " " 
    return rev_str
    """

def main() -> None:

    user_input : str = input("Enter a string to reverse words : ")
    print("After reversing : ")
    print(reverse_words(user_input))


if __name__ == "__main__":
    main()