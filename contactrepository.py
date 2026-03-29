import pathlib 
import sqlite3
import os

class ContactRepository :
    def __init__(self):
        self.path = pathlib.Path.home()
        self.path_to_db = os.path.join(self.path,"Contact Book.db")
    
    def add_contact(self,userid,name,phone,email,address,notes):
        with sqlite3.connect(self.path_to_db) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO contacts (userid,name,phone,email,address,notes) \
                      VALUES (?,?,?,?,?,?)",(userid,name,phone,email,address,notes))
            conn.commit()
            print(f"you successfully added {name} ✅")

    def check_if_the_contact_exist(self,name,userid):
        with sqlite3.connect(self.path_to_db) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM contacts WHERE name = ? AND userid = ?",(name,userid))
            data = c.fetchall()
        if data :
            return data
        else :
            return None 
        
    def delete_contact(self,name,userid):
        with sqlite3.connect(self.path_to_db) as conn :
            c = conn.cursor()
            c.execute("DELETE FROM contacts WHERE name = ? AND userid = ?" , (name,userid))
            conn.commit()

    def get_user_contacts(self,userid):
        with sqlite3.connect(self.path_to_db) as conn :
            c = conn.cursor()
            c.execute(f"SELECT * FROM contacts WHERE userid = ?",(userid,))
            data = c.fetchall()
        return data 

    def edit_contact(self,userid,name,new_name,new_phone,new_email,new_address,new_notes) :
        with sqlite3.connect(self.path_to_db) as conn :
            c = conn.cursor()
            c.execute(f"""UPDATE contacts SET 
                      name = ?,
                      phone = ?,
                        email = ? ,
                        address = ? ,
                        notes = ? 
                        WHERE userid = ? AND name = ? """,(new_name,new_phone,new_email,new_address,new_notes,userid,name))
            conn.commit()
    
    

    
    






    