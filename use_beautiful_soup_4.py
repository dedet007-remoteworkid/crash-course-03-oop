import requests
from bs4 import BeautifulSoup

url = 'https://tempointeraktif.com'
try:
    respond = requests.get(url)
    #print(respond.status_code)
    if respond.status_code == 200:
        print(f'Sucess, lisa = {respond.status_code}')
        soup = BeautifulSoup(respond.text, features="html.parser")
        print(f'Hasil pemanggilan {url}')
        print(f'Title: {soup.title.string}')
        #print(respond.text)
except Exception as e:
    print('ada error', e)
