from utils import * 
from storage import *
import getpass

class Authentication :
    def __init__(self):
        self.storage = Storage()

    def register(self):
        while True :
            number = input("set a phone number (q to quit)")
            if number == "":
                print("enter something 📛")
            elif number == "q" :
                print("try again later 📛")
                return None
            elif self.storage.user_data(number)  :
                print("you already have an account,go to log in page 📛")
            else :
                print("valid number ✅")
                break             
        while True :
                pin = getpass.getpass("set a pin using 4 digits (q to quit):")
                if pin == "q":
                    print("try again later 📛")
                    return None
                elif not pin.isdigit():
                    print("enter just digits 📛")
                elif pin == "":
                    print("enter something !📛")
                elif len(pin) != 4 :
                    print("enter a pin from 4 digits📛")
                else :   
                    hash_pin = hash_function(pin)
                    print("valid pin ✅")                                       
                    break
        while True :
            username = input("set a username (q to quit):")
            if username == "q":
                print("try again later 📛")
                return 
            elif username == "":
                print("enter something 📛")
            elif self.storage.check_if_username_exist(username) :
                print("username already exist, pick another one 📛")
            else :
                self.storage.add_user(number,username,hash_pin)
                print("account created ✅")
                return self.storage.user_data(number)

    def log_in(self):
        while True :
            number = input("verify your number (q to quit ):").strip()
            if number == "q":
                print("try again later !⛔️")
                return None
            elif number == "":
                print("enter something !⛔️")
            elif self.storage.user_data(number) is None:
                print("phone number not exist !⛔️")
            else :
                print("account found ✅")
                break
        password_attempt = 2
        user_data = self.storage.user_data(number)[0]
        split_pwd = user_data[3]   
        while True :
            pin = getpass.getpass("verify your pin (q to quit) :")
            if pin == "q":
                print("try again later !⛔️")
                return None
            elif pin == "":
                print("enter something !⛔️")
            elif verify_pin(pin,split_pwd) :
                print("correct pin ✅")
                print(f"Wecome Back {user_data[2]}")
                return user_data 
            elif password_attempt > 0 :
                print(f"incorrect pin, you still have {password_attempt} left ⛔️")
                password_attempt -= 1
            else :
                print("try again later ⛔️")
                break
            

