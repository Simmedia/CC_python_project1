import requests
import time

def is_site_up(url):
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            print(url, 'is is up!')
        elif (response.status_code == 404):
            print(url, 'not found!')

    except ConnectionError:
        print("You need an active internet connection")

    except:
        print('Invalid URL')


#  main function
if __name__ == '__main__':

    while True:
        print("""
Welcome, what would you like to do?
1. Check if site is up
2. Quit
        """)

        choice = input("Your choice: ")
        
        if (choice == '1'):
            url = input('Enter url starting with https:// or http:// : ')
            is_site_up(url)
        elif (choice == '2'):
            print("See you later...")
            exit()
        else:
            print("Choice invalid!")

        time.sleep(2)