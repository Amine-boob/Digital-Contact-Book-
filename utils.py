import bcrypt 

def hash_function(self,pwd):
    byte_pwd = pwd.encode("utf-8")
    return bcrypt.hashpw(byte_pwd,bcrypt.gensalt(rounds=14))


def decorator_message(message) :
    def add_decorator(func):
        def wrapper(*args,**kwargs):
            print(f"-------- {message} --------")
            result = func(*args,**kwargs)
            print(F"-------------------"+"-"*len(message))
            return result
        return wrapper
    return add_decorator



