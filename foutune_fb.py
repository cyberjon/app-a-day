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
        if author_id != self.uid : 
            if message_object.text =='quote' :
                
                #new_msg =quotes[i]
                new_msg =subprocess.check_output(['fortune'])
                msg = Message(new_msg)
                self.send( msg , thread_id=thread_id, thread_type=thread_type)


client = EchoBot("<email>", "<password>")
client.listen()


