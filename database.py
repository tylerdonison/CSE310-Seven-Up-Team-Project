"""This class will be responsible for handling the database, in storing player, 
date played, and score."""

import pandas as pd
from datetime import date

class Database():
    def __init__(self):
        self.stats = {"Initials": [], "Date": [], "Score": []} #feel free to add more.
        self.data = pd.DataFrame(self.stats)
    
    def add_player(initials, score):
        date = date.today()
        new_data = [initials, date, score] #this needs to match the stats dictionary as to merge it with the dataframe
        self.data.loc[len(data.index)] = new_data
