import bcrypt
class Authentication :
    def __init__(self):
        self.all_users = []
        self.current_user = ""   # User(..,..)

    def all_numbers(self):
        names = []
        for user in self.all_users :
            names.append(user.phone_number)
        return names
    
    def get_current_user(self,number) :
        for user in self.all_users :
            if user.phone_number == number :
                return user 
        return None 


    def register(self):
        pass

    def log_in(self):
        while True :
            number = input("verify your number (q to quit ):")
            if number == "q":
                print("try again later !⛔️")
                return 
            elif number == "":
                print("enter something !⛔️")
            elif number not in self.all_numbers :
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
        pass