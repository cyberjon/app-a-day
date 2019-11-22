import requests
import wget
from bs4 import BeautifulSoup
import PySimpleGUI as sg

layout=[
    [sg.Text('URL', size=(15, 1)), sg.InputText('')], 
    [sg.Submit(), sg.Cancel()] 
     


]

window = sg.Window('Simple web scraper').Layout(layout)         
button, values = window.Read()

url = values[0]

#url = 'http://slav0nic.org.ua/static/books/python/'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
current_link = ''
for link in soup.find_all('a'):
    current_link = link.get('href')
    #if current_link.endswith('pdf'):
        #wget.download(url+current_link,out='/home/mach/')
    print(' ' + current_link)