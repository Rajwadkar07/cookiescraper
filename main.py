import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from telethon import TelegramClient
import os

num = 12602
api_id = 1015622
api_hash = '8bd892b1c3446a452c97700065350e52'
client = TelegramClient('anoni', api_id, api_hash)

while True:
    url = 'https://m.rttar.com/paste.php?id='+str(num)
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')

    if '-' in soup.title.text:
        print('Cookie Found', num,':', soup.title.text)
        data = soup.findAll('div', attrs={'class': 'panel-body'})

        with open(str(num)+' '+soup.title.text+'.txt', 'w+') as file:
            try:
                file.write(data[1].text.strip().replace('\n',''))
            except:
                print('Error on the host side. Sleeping for 60 seconds.')
                num += 1
                sleep(60)
                continue

        async def main():
            await client.send_file(-1001864302223, str(num)+' '+soup.title.text+'.txt')

        with client:
            client.loop.run_until_complete(main())

        os.remove(str(num)+' '+soup.title.text+'.txt')

        print('Cookie sent. Sleeping for 60 seconds...')
        sleep(60)
        num += 1
    else:
        print('No cookie found. Sleeping for 180 seconds...')
        sleep(180)
        num += 1
