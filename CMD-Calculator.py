# Program to illustrate a command-line calculator
import time

def simple_calculator():
    '''funtion to accept user input and do calculations using eval()
    num - a string variable to accept input from user
    '''

    num = input("enter number and operation: ")
    try:
        print(f"input: {num} \nresult: {eval(num)}")
    except ValueError:
        print("ValueError, enter only integer and operator")
    except SyntaxError:
        print("SyntaxError, invalid syntax")
    except NameError:
        print("NameError, enter a valid data!")


#  main function
if __name__ == '__main__':

    while True:
        print("""
    Welcome, what would you like to do?
    1. Simple calculator
    2. Quit
        """)

        choice = input("your choice: ")
        if int(choice) == 1:
            simple_calculator()
        else:
            print("See you later...")
            quit()

        time.sleep(2)
