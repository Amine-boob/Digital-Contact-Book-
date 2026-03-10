
import pathlib
import pickle
import os

class Storage :
    def __init__(self):
        self.path = pathlib.Path.home()
        self.path_to_db = os.path.join(self.path,"Contact Book.db")

    def get_data_from_file(self):
        try : 
            with open(self.path_to_db , "rb") as file :
                data = pickle.load(file)
                self.all_users = data
        except FileNotFoundError :
            with open(self.path_to_db ,"wb") as file :
                pickle.dump([],file)

    def add_data_to_file(self,data):
        with open(self.path_to_db ,"wb") as file :
            pickle.dump(data,file)

    def save_changes(self) :
        self.add_data_to_file()