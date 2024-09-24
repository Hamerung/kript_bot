import time
import requests
from tg_bot import bot_token


API_URL = 'https://api.telegram.org/bot'
KOTIK = 'https://api.thecatapi.com/v1/images/search'
max_counter = 100

offset = -2
counter = 0
chat_id: int

while counter < max_counter:
    print('воть', counter)

    updt = requests.get(f'{API_URL}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updt['result']:
        for result in updt['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            text = result['message']['text']
            url_cat = requests.get(KOTIK).json()[0]['url']
            requests.get(f'{API_URL}{bot_token}/sendPhoto?chat_id={chat_id}&photo={url_cat}')
            # requests.get(f'{API_URL}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')
    
    time.sleep(1)
    counter += 1