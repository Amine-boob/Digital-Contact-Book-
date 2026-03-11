from utils import *
from user import *
from storage import *
import bcrypt
import getpass

class Authentication :
    def __init__(self):
        self.all_users = []
        self.storage = Storage()

    def all_numbers(self):
        if self.all_users :
            names = []
            for user in self.all_users :
                names.append(user.phone_number)
            return names
        else :
            return []
    
    def all_usernames(self):
        if self.all_users :
            usernames = []
            for user in self.all_users :
                usernames.append(user.username)
            return usernames
        else :
            return []

    def get_current_user(self,number) :
        for user in self.all_users :
            if user.phone_number == number :
                return user 
        return None 

    def register(self):
        while True :
            number = input("set a phone number (q to quit)")
            if number == "":
                print("enter something 📛")
            elif number == "q" :
                print("try again later 📛")
                return None
            elif number in self.all_numbers() :
                print("you already have an account,go to log in page 📛")
            else :
                print("valid pin ✅")
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
            elif username in self.all_usernames() :
                print("username already exist, pick another one 📛")
            else : 
                result = User(number,username,hash_pin)
                self.all_users.append(result)
                print("account created ✅")
                return result

    def log_in(self):
        while True :
            number = input("verify your number (q to quit ):")
            if number == "q":
                print("try again later !⛔️")
                return 
            elif number == "":
                print("enter something !⛔️")
            elif number not in self.all_numbers() :
                print("phone number not exist !⛔️")
            else :
                print("account found ✅")
                break
        passward_attempt = 2
        user_password = self.get_current_user(number).pin   #get the password from the database
        while True :
            pin = input("verify yor pin ")
            if pin == "q":
                print("try again later !⛔️")
                return 
            elif pin == "":
                print("enter something !⛔️")
            elif self.verify_pin(pin,user_password) :
                self.storage.add_data_to_file(self.all_users)
                print("correct pin ✅")
                break
            elif passward_attempt > 0 :
                print(f"incorrect pin, you still have {passward_attempt} left ⛔️")
            else :
                print("try again later ⛔️")
                break
            
            

    def log_out(self):
        pass

    def verify_pin(self,pin,hash_pin):
        if bcrypt.checkpw(pin.encode("utf-8"),hash_pin) :
            return True 
        else :
            return False


