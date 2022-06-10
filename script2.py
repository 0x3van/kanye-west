import os, json, requests
# use this for linux
os.system('clear')


def cum():
    try:
        os.system('clear')

        user_input = input('title sex: ')

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