
from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.status = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self,message,sent_by_me):
        #words=['purity','nature','disaster']
        self.message=message
        #if message is sent then value of sent by me will be true
        self.sent_by_me = sent_by_me
        self.time = datetime.now()

#if any(i in message for i in words):
    #print('its urgent!')



spy=Spy()

#creating class object of friend to store
friend1=Spy()
friend2=Spy()
friend3=Spy()
friend4=Spy('rocky','ms',11,2.7)



friends=[friend1,friend2,friend3,friend4]

#C:\Users\LENOVO\PycharmProjects\spychat\imgs