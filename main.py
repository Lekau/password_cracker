import cracker.cracker as crack
import creator.creator as create
import string
import sys
if __name__ == '__main__':
    print("Under Construction")
    create.welcome()
    my_file = open('hello.txt', "w")
    my_file.write(''.join(create.create_password()))
    
    create.success_message()