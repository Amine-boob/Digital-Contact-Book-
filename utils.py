from contactrepository import *
import bcrypt 
handlecontact  = ContactRepository()

def hash_function(pwd):
    byte_pwd = pwd.encode("utf-8")
    return bcrypt.hashpw(byte_pwd,bcrypt.gensalt(rounds=14))

def verify_pin(pin,hash_pin):
        if bcrypt.checkpw(pin.encode("utf-8"),hash_pin) :
            return True 
        else :
            return False


def decorator_message(message) :
    def add_decorator(func):
        def wrapper(*args,**kwargs):
            print(f"\n-------- {message} --------")
            result = func(*args,**kwargs)
            print(f"-" * (18 + len(message))+"\n")
            return result
        return wrapper
    return add_decorator


def get_data(data):
        if data :
            return data 
        else :
            return "-"

def helper_with_set_name(userid):
    while True :
        name = input("enter the name :")
        if name == "":
            print("you must enter the name of the contact ⛔️")
        elif handlecontact.check_if_the_contact_exist(name,userid) :
            print("this name already exist, choose another one ⛔️")
        else :
            return name

def helper_edit_func(new_value,old_value):
     if new_value == "" : #skip
        return  old_value
     else : 
        return  new_value 
          

def helper_with_edit_name(name,userid):
    while True :
        new_name = input("enter the new name :") 
        if new_name == "" :
            return name
        elif new_name == name :
            return new_name
        elif handlecontact.check_if_the_contact_exist(new_name,userid) :
            print("name already exist choose another one !")
        else :
            return new_name
