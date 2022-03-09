import os, json, requests

os.system('cls')
# pop
os.system('title kanye west funny hilarios popbob gaming 69 generater 2014 wokring amongus')

def cum():
    try:
        os.system('cls')

        user_input = input('what very funny and hilariorus title??? : ')

        json_table = {
            'title': user_input
        }

        response = requests.post(
            'https://api.stemplayer.com/remixes',
            headers = {
                'Content-Type': 'application/json'
            },
            json = json_table
        )

        print(f'url: https://www.stemplayer.com/remix/{response.json()["data"]["id"]}\n')

        input()
        cum()
    except:
        cum()

cum()