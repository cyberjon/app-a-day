import sys
import requests
import bs4
import csv
import pandas



url ='https://www.oireachtas.ie/en/members/tds/?term=%2Fie%2Foireachtas%2Fhouse%2Fdail%2F32'

#res = requests.get('https://en.wikipedia.org/wiki/'+''.join(sys.argv[1:]))
res = requests.get(url)
res.raise_for_status()

soup =bs4.BeautifulSoup(res.text, "html.parser")

for i in soup.find_all("div", class_="c-member-list-item"):
   

  print(i.getText())
   
   


