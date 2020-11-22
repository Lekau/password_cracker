import string
from random import choice
password = list()
def confirm(message):
    """
    Asks the user a question(message) for a y/N and return true if y is 
    inputted and False if n is inputted
    Parm: message
    Return:Bool
    """
    ans = ''
    while ans.isalpha() == False and ans.lower() != 'n' and ans.lower() != 'y':
        ans = input(message+" Y/n:")
        if ans.lower() != 'n' and ans.lower() != 'y':
            return confirm(message)
        continue
    if ans.lower() == 'y':
        return True
    else:
        return False
    
    
def welcome():
    """
    Displays a welcome message stating its creating a password.
    parm: None
    Return: None
    """
    print("Welcome to password cracker. We will create a password and crack it.")

def create_superlist():
    """
    Creates a list of characters to be used for the password
    parm: None
    Return: list
    """
    super_list = list()
    
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_char = list("#@!()-")
    
    has_capital = confirm("Must your password include uppercase letters")
    has_numbers = confirm("Must your password include numbers")
    has_special = confirm("Must your password include special characters(# @ ! ( ) -)")

    super_list += lower_chars
    if has_capital == True:
        super_list += upper_chars
    if has_numbers == True:
        super_list += numbers
    if has_special == True:
        super_list += special_char
    
    return super_list

def create_password():
    """
    Creates and returns a strring password based on the answers 
    from the input functions ran in it.
    oarm: None
    Return: String
    """
    print("Lets create a new password")
    the_password = list()
    length = 0
    while True:
        try:
            length = int(input("How long should the password be(4 - 20):"))
            if length >= 4 and length <= 20:
                break
            else:
                continue
        except ValueError:
            print("Please enter a number between 4 and 20")

    big_list = create_superlist()
    print(big_list)
    while length > 0:
        the_password.append(choice(big_list))
        length -= 1
    return the_password
    
def success_message():
    """
    Displays to the stdout that a password has been created.
    Parm: None
    Return: None
    """
    print("Password was successfully created.")