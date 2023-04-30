import sys
import requests as req

def greeting(greet_person):
    greeting_statement = f'Hello {greet_person}'
    return greeting_statement


if __name__ == "__main__":
    print("Start...")

    print("version: ", sys.version)
    print("loc: ", sys.executable)

    r = req.get('https://www.timeout.com/travel/oldest-cities-in-the-world')
    print(r.status_code)

    print(greeting('Tom'))

    name = input('Your name? ')
    print(greeting(name))

    

    





    
