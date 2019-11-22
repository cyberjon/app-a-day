import requests
import wget
from bs4 import BeautifulSoup
#url = sys.argv[-1]
url = 'https://www.oireachtas.ie/en/members/tds/?tab=constituency&constituency=%2Fie%2Foireachtas%2Fhouse%2Fdail%2F32%2Fconstituency%2FKildare-South'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

for images in soup.find_all('img'):
    img=images['src']
    wget.download(img,out='/home/mach/')
    print(images['src'])