from contact import *
from utils import *
class User :   # ✅⛔️
    def __init__(self,phone_number,username,pin):
        self.phone_number = phone_number
        self.username = username 
        self.pin = pin  
        self.contact = []


    @decorator_message("Your Contact")
    def show_contact(self) :
        for index,person in enumerate(self.contact,start=1) :
            print(f"{index} -{person.name}")

    def add_a_contact(self,data):
       self.contact.append(data)

    def remove_contact(self):
       pass

    def get_contact(self):
       pass

    def list_contacts(self):
       pass
    






