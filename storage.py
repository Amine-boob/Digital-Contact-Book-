import pathlib
import sqlite3 
import os

class Storage  :
    def __init__(self):
        self.path = pathlib.Path.home()
        self.path_to_db = os.path.join(self.path,"Contact Book.db")
    
    def connect_to_database(self):
        with sqlite3.connect(self.path_to_db) as conn :
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS users (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    phone_number TEXT UNIQUE,
                    username TEXT UNIQUE ,
                    pin TEXT
                    )""")
            conn.commit()
            c.execute("""CREATE TABLE IF NOT EXISTS contacts (
                        ID INTEGER PRIMARY KEY ,
                        userid INTEGER ,
                        name TEXT ,
                        phone TEXT ,
                        email TEXT ,
                        address TEXT ,
                        notes TEXT ,
                        FOREIGN KEY (userid) REFERENCES users (ID)
                        )""")
            conn.commit()
 
    def user_data(self,number) :
        try :
            with sqlite3.connect(self.path_to_db) as conn :
                c = conn.cursor()
                c.execute(f"SELECT * FROM users WHERE phone_number = ?",(number,))
                data = c.fetchall()   
            if data :
                return data 
            else :
                return None 
        except sqlite3.IntegrityError :
            print("name alreay exist !")
    
    def check_if_username_exist(self,username) :
        with sqlite3.connect(self.path_to_db) as conn : 
            c = conn.cursor()
            c.execute(f"SELECT * FROM users WHERE username = ?",(username,))
            data = c.fetchone()
        if data :
            return True
        else :
            return False 

    def add_user(self,phone_number,username,pin):
        with sqlite3.connect(self.path_to_db) as conn :
            c = conn.cursor()
            c.execute(f"INSERT INTO users (phone_number,username,pin) VALUES (?,?,?)",(phone_number,username,pin))
            conn.commit()
            
    
    


















