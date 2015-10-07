import re


def clean_string(user_input):
    """Remove all punctuation and white space from input string"""
    return re.sub(r'[^A-Za-z]', '', user_input.lower())


def palindrome_iterative(user_input):
    """Check if input matches forwards and backwards"""
    return user_input == user_input[::-1]


def palindrome_recursive(user_input):
    """Recursively check the input string if it is a palindrome"""
    if len(user_input) < 2:
        return True
    elif user_input[0] != user_input[-1]:
        return False
    else:
        return palindrome_recursive(user_input[1:-1])


user_input = input("Enter Stuff Here: ")
cleaned_input = clean_string(user_input)

if palindrome_iterative(cleaned_input) and palindrome_recursive(cleaned_input):
    print("{} is a palindrome".format(user_input))
else:
    print("{} is not a palindrome".format(user_input))
