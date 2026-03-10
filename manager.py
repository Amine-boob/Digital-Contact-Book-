from admin import *
from utils import *



class ContactManager :
    def __init__(self):
        #self.admin = Admin()
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
  

    @decorator_message("ghhghghghghhghghghghgh")
    def print_menu(self):
        for index ,line in enumerate(self.menu,start=1) :
            print(f"{index}-{line}")

    def run(self):
        while True :
            self.print_menu()
            choice = input("enter your choice :")
            if choice == "1":
                pass
            elif choice == "2":
                pass
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

