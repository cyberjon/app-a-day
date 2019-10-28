import sys
import requests
import bs4
import csv




url ='http://kildare.ie/countycouncil/Contact/'

#res = requests.get('https://en.wikipedia.org/wiki/'+''.join(sys.argv[1:]))
res = requests.get(url)
res.raise_for_status()

soup =bs4.BeautifulSoup(res.text, "html.parser")

#table = soup.find_all('table',class_='contacts')[1]
rows = soup.findAll("tr")

with open("test.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)
   
   


