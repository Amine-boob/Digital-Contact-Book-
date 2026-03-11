from admin import *
from utils import *
from authentication import *
from storage import *

class ContactManager :
    def __init__(self):
        self.admin = Admin()
        self.authentication = Authentication()
        self.storage = Storage()
        self.menu = ["Rigister",
                     "log in with your phone number",
                     "log out",
                     "show my contact",
                     "search for a number by name",
                     "add contact",
                     "delete contact",
                     "quit"
                    ]
        global decorator_message
  

    @decorator_message("amine")
    def print_menu(self):
        for index ,line in enumerate(self.menu,start=1) :
            print(f"{index}-{line}")



    def run(self):
        # get data from the file if it exist :
        existing_data = self.storage.get_data_from_file()
        if existing_data :
            self.authentication.all_users = existing_data 
        
        current_user = None
         
        while True :
            self.print_menu()
            choice = input("enter your choice :")
            if choice == "1":
                data = self.authentication.register()
                if data :
                    current_user = data 
                    print("account created ")
            elif choice == "2":
                self.authentication.log_in()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                pass
            elif choice == "8":
                pass
            else :
                print("invlid choice !")

