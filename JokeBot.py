import pyperclip
import pyautogui
from bs4 import BeautifulSoup
from time import sleep
import requests
import random

comps = []

def parse():
    url = 'https://4tob.ru/anekdots/tag/short'
    headers = {'User-Agent': '<insertYourHeaders>'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    plates = soup.find_all('div', class_ = 'q')


    for plate in plates:
        try:

            comps.append({
            'number': plate.find('div', class_='nomer').find('a').get_text(strip=True),
            'text': plate.find('div', class_ = 'text').get_text(strip=True)
            })
        except AttributeError:
            pass




parse()


def Bot():
    print('10 seconds to start.')
    sleep(10)

    while True:
        try:
            joke = random.randint(0,len(comps))
            pyautogui.press('t')
            sleep(1)
            pyperclip.copy(str(comps[joke]['number']) + ': ' + str(comps[joke]['text']))
            sleep(1)
            pyautogui.hotkey('command', 'v')
            pyautogui.press('Enter')
            sleep(60)
        except IndexError:
            pass

Bot()







