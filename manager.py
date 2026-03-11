from admin import *
from utils import *
from authentication import *
from storage import *
from contact import *


class ContactManager :
    def __init__(self):
        self.admin = UserManager()
        self.authentication = Authentication()
        self.storage = Storage()
        self.menu = ["Register",
                     "log in with your phone number",
                     "log out",
                     "show my contact",
                     "add contact",
                     "delete contact",
                     "edit a contant ",
                     "search for the information by name",
                     "quit"
                    ]
        self.current_user = None
        
    @decorator_message("menu")
    def print_menu(self):
        for index ,line in enumerate(self.menu,start=1) :
            print(f"{index}-{line}")

    
    def add_contact(self) :
        name = get_data(input("enter the name :"))
        number = get_data(input("enter the number :"))
        email = get_data(input("enter the email :"))
        address = get_data(input("enter the address :"))
        notes = get_data(input("enter your note about this person :"))
        self.current_user.add_a_contact(Contact(name,number,email,address,notes))
    
    def show_contact(self):
        if self.current_user.contact :
            self.current_user.show_contact()
        else :
            print("you don't have any contact ⛔️")



    def run(self):
        # get data from the file if it exist :
        existing_data = self.storage.get_data_from_file()
        if existing_data is not None :
            self.authentication.all_users = existing_data 
        
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
                    print(f"see you soon {self.current_user.username}")
                    self.current_user = None 

            elif choice == "4":
                if self.current_user :
                    self.show_contact()
                else :
                    print("you must log in first ⛔️")
                

            elif choice == "5":
                if self.current_user :
                    self.add_contact()
                else :
                    print("you must log in first ⛔️")

            elif choice == "6":
                pass
            elif choice == "7":
                pass
            elif choice == "8":
                pass
            elif choice == "9":
                pass
            else :
                print("invlid choice !⛔️")

