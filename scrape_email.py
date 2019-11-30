import requests

from bs4 import BeautifulSoup
import csv
import PySimpleGUI as sg



layout=[
    [sg.Text('URL', size=(15, 1)), sg.InputText('')], 
    [sg.Submit(), sg.Cancel()] 
    
     


]

window = sg.Window('Simple web scraper').Layout(layout)         
button, values = window.Read()
url = values[0] 





response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
current_link = ''


with open('email.csv', mode='w') as link_file:
    link_writer= csv.writer(link_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    link_writer.writerow(['E-mail'])
    

    for link in soup.find_all('a'):
        current_link = link.get('href')

        if 'mailto:' in current_link:
            link_writer.writerow([current_link[7:]])
        

    

        

