import string
from random import choice

password = list()
lower_char = list(string.ascii_lowercase)
upper_char = list(string.ascii_uppercase)
number_char = list(string.digits)
special_char = list("#@!()-")

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


def checking_loop(char_set, list_of_chars):
    """
    Function to check if at least 1 item exists from one list in another list
    parm:char_set, list_of_chars
    return: Bool
    """
    for x in list_of_chars:
        if x in char_set:
            return True
    return False


def what_to_check_for(char_set):
    """  
    Checks which character sets to check for in the password
    parm: char_set
    return: Bool, Bool, Bool
    """
    global upper_char, number_char, special_char
    check_for_special = checking_loop(char_set, special_char)
    check_for_number = checking_loop(char_set, number_char)
    check_for_capital = checking_loop(char_set, upper_char)
    return check_for_capital, check_for_number, check_for_special
    

def chars_represented(char_set, password):
    """ 
    Checks if all the selected character sets are in the password
    parm: char_set, passward
    return: Bool
    """
    global upper_char, number_char, special_char 
    captial, number, special = what_to_check_for(char_set)
    if captial == True:
        if checking_loop(upper_char, password) == False:
            return False
    if number == True:
        if checking_loop(number_char, password) == False:
            return False
    if special == True:
        if checking_loop(special_char, password) == False:
            return False
    return True


def create_superlist():
    """
    Creates a list of characters to be used for the password
    parm: None
    Return: list
    """
    super_list = list()
    global lower_char, upper_char, number_char, special_char
    
    has_capital = confirm("Must your password include uppercase letters")
    has_numbers = confirm("Must your password include numbers")
    has_special = confirm("Must your password include special characters(# @ ! ( ) -)")
    super_list += lower_char
    if has_capital == True:
        super_list += upper_char
    if has_numbers == True:
        super_list += number_char
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
    n = length
    while chars_represented(big_list, the_password) == False:
        the_password.clear()
        n = length
        while n > 0:
            the_password.append(choice(big_list))
            n -= 1
    return the_password
    

def success_message():
    """
    Displays to the stdout that a password has been created.
    Parm: None
    Return: None
    """
    print("Password was successfully created.")