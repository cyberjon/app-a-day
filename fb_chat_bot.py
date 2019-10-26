from fbchat import Client
from fbchat.models import *



username = input("Facebook user ID or e-mail:")
password = input("Enter in you Facebook Password:")
# login

client = Client(username, password)
users = list(client.fetchThreadList())

u=client.searchForUsers('lptcdojo')

print(u)

#for i in range(0,len(users)):
   # if users[i].name =='Lorcan Mac Hugh':
        
       # client.send(Message(text='This a test from my Facbook Bot'), thread_id=users[i].uid, thread_type=ThreadType.USER)
    

client.logout()