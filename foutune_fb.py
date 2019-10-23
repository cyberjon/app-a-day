from fbchat import log, Client
from fbchat.models import *
import random
import subprocess

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        


        log.info(f'{message_object.text}')
 
        # If you're not the author, echo
        if  author_id != self.uid  and message_object.text.lower() !='yes' and  message_object.text.lower() !='no': 
            
            welcome = "Hi do want a quote Yes/No"
            welcome_msg =Message(welcome)
            self.send( welcome_msg , thread_id=thread_id, thread_type=thread_type)
        
            
        if message_object.text.lower() =='yes':
                
                #new_msg =quotes[i]
                new_msg =subprocess.check_output(['fortune'])
                msg = Message(new_msg)
                another = "Hi do want a quote Yes/No"
                another_msg =Message(another)

                self.send( msg , thread_id=thread_id, thread_type=thread_type)
                self.send(another_msg , thread_id=thread_id, thread_type=thread_type)
                
        if  message_object.text.lower() =='no':
                goodbye = "Goodbye"
                goodbye_msg =Message(goodbye)
                self.send(goodbye_msg , thread_id=thread_id, thread_type=thread_type)
                

username = input("Facebook user ID or e-mail:")
password = input("Enter in you Facebook Password:")

client = EchoBot(usename , password)
client.listen()


