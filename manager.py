from utils import *
from authentication import *
from storage import *
from contactrepository import *

class ContactManager :
    def __init__(self):
        self.handlecontact = ContactRepository() 
        self.authentication = Authentication()
        self.storage = Storage()
        self.menu = ["Register",
                     "log in with your phone number",
                     "log out",
                     "show my contact",
                     "show more data about a specific contact ",
                     "add contact",
                     "delete contact",
                     "edit a contact ", 
                     "quit"
                    ]
        self.current_user = None
        
    @decorator_message("Menu")
    def print_menu(self):
        for index ,line in enumerate(self.menu,start=1) :
            print(f"{index}-{line}")
  
    def add_contact(self) :
        userid = self.current_user[0]
        name = helper_with_set_name(userid)
        number = get_data(input("enter the number :"))
        email = get_data(input("enter the email :"))
        address = get_data(input("enter the address :"))
        notes = get_data(input("enter your note about this person :"))
        self.handlecontact.add_contact(userid,name,number,email,address,notes)

    def input_contact_name(self): #to get the name if it exist in the database
        userid = self.current_user[0]
        while True :
            name = input("enter the name of this contact(q to quit):")
            contact_info = self.handlecontact.check_if_the_contact_exist(name,userid)
            if name == "q":
                print("try again later ⛔️")
                return None 
            elif contact_info :
                return name 
            else :
                print("you don't have this account ,check your input ⛔️")      

    def show_contact(self):
        userid = self.current_user[0]
        user_contact = self.handlecontact.get_user_contacts(userid)
        if user_contact :
            print("------ your contacts ------")
            for index,contact in enumerate(user_contact,start=1):
                print(f"{index}- {contact[2]}")
            print("---------------------------")
        else :
            print("you don't have any contact ⛔️")


    @decorator_message("Information")
    def get_more_detail_about_contact(self,name):
        userid = self.current_user[0]
        user_data = self.handlecontact.check_if_the_contact_exist(name,userid)[0]
        details = ["the name    :",
                   "the phone   :",
                   "the email   :",
                   "the address :",
                   "the note    :"]
        for index,message in enumerate(details,start=2) :
            print(f"{message}{user_data[index]}")

    @decorator_message("Old Information")
    def print_old_information(self) :
        pass
    def delete_contact(self,name):
        userid = self.current_user[0]
        self.handlecontact.delete_contact(name,userid)
    
    def edit_contact(self,name) :
        userid = self.current_user[0]
        user_data = self.handlecontact.check_if_the_contact_exist(name,userid)[0]
        name = user_data[2]
        phone = user_data[3]
        email =user_data[4]
        address = user_data[5]
        notes = user_data[6]
        self.print_contact_info(name)
        print("➖ press (enter) to skip and not edit ➖")
        new_name = helper_with_edit_name(name,userid)
        new_phone = helper_edit_func(input("enter the new phone :"),phone)
        new_email = helper_edit_func(input("enter the new email :"),email)
        new_address = helper_edit_func(input("enter the new address :"),address)
        new_notes = helper_edit_func(input("enter the new notes :"),notes)
        self.handlecontact.edit_contact(userid,name,new_name,new_phone,new_email,new_address,new_notes)
        print("information changed ✅")

    @decorator_message("Old Information")
    def print_contact_info(self,name) :
        userid = self.current_user[0]
        user_data = self.handlecontact.check_if_the_contact_exist(name,userid)[0]
        details = ["the name    :",
                   "the phone   :",
                   "the email   :",
                   "the address :",
                   "the note    :"]
        for index,message in enumerate(details,start=2) :
            print(f"{message}{user_data[index]}")
        

    def run(self):
        self.storage.connect_to_database()
        while True :
            self.print_menu()
            choice = input("enter your choice :")
            if choice == "1":
                data = self.authentication.register()
                if data :
                    self.current_user = data

            elif choice == "2":
                data = self.authentication.log_in()
                if data :
                    self.current_user = data

            elif choice == "3":
                if self.current_user == None :
                    print("you are already logged out ⛔️")
                else :
                    print("you successfully logged out ✅")
                    print(f"see you soon {self.current_user[2]}")
                    self.current_user = None 

            elif choice == "4":
                if self.current_user :
                    self.show_contact()
                else :
                    print("you must log in first ⛔️")    
            elif choice == "5":
                if self.current_user :
                    contact_name = self.input_contact_name()
                    if contact_name :
                        self.get_more_detail_about_contact(contact_name)
                    else :
                        pass
                else :
                    print("you must log in first ⛔️")

            elif choice == "6":
                if self.current_user :
                    self.add_contact()
                else :
                    print("you must log in first ⛔️")
            elif choice == "7":
                if self.current_user :
                    contact_name = self.input_contact_name()
                    if contact_name :
                        self.delete_contact(contact_name)
                    else :
                        pass
                else :
                    print("you must log in first ⛔️")
            elif choice == "8":
                if self.current_user :
                    contact_name = self.input_contact_name()
                    if contact_name :
                        self.edit_contact(contact_name)
                    else :
                        pass
                else :
                    print("you must log in first ⛔️")
            elif choice == "9" :
                print("See you later !")
                break
            else :
                print("invalid input !⛔️")

