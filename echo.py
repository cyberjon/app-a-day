from fbchat import log, Client
from fbchat.models import *
import random


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        quotes = [
        '"Give her hell from us, Peeves.”',
        '“I solemnly swear that I am up to no good.”',
        '“It does not do to dwell on dreams and forget to live.”',
        '“Don’t let the Muggles get you down.”',
        '“Let us step into the night and pursue that flighty temptress, adventure.”',
        '“After all this time?” “Always.”',
        '“Of course it is happening inside your head, Harry, but why on Earth should that mean that it is not real?”',
        '“One can never have enough socks."',
        '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
        '“You’ll stay with me?” “Until the very end.”',
        '“Just because you have the emotional range of a teaspoon doesn’t mean we all have.”',
        '“What’s comin’ will come, an’ we’ll meet it when it does.”',
       '“You’re a wizard, Harry.”'
        ]


        #log.info(f'{message_object.text}')
 
        # If you're not the author, echo
        if author_id != self.uid : 
            if message_object.text =='accio' :
                i = random.randint(0,len(quotes))
                new_msg =quotes[i]
                
                msg = Message(new_msg)
                self.send( msg , thread_id=thread_id, thread_type=thread_type)

username = input("Facebook user ID or e-mail:")
password = input("Enter in you Facebook Password:")

client = EchoBot(usename , password)
client.listen()


