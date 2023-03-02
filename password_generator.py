import string
from secrets import SystemRandom

rand = SystemRandom()

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

def generate_password():
    pwd = letters + digits +  special_characters
    pwd_length = rand.randint(9, 15)
    generated_pwd = ''.join(rand.choices(pwd, k=pwd_length))
    return generated_pwd

while True:
    print("""
Welcome
1. Generate password
2. Exit
    """)
    choice = input("Your choice: ")
    if (choice == '1'):
        print("Password generated successfully:", generate_password())
    elif (choice == '2'):
        print("See you later...")
        exit()
    else:
        print("Enter valid option!")


    time.sleep(2)