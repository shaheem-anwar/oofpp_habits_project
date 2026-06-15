from habits import Habit
from datetime import datetime
import json

""" This is the Persistence Layer - It is the storage layer of the app 
which make sure that the habit data (habit objects) are stored and its 
retrieval after the application restarts."""

def save_habits(habits):
    """save habits to habits.json file"""
    data=[]

    #convert habit objects to dictionaries for JSON storage
    for h in habits:
        # Converting datetime objects to list of strings since JSON does not support datetime.datetime format
        check_list = [check.isoformat() for check in h.checks]  # appending the converted datetime string to the check_list

        #convert habit attributes to a dictionary format suitable for JSON
        data.append({
            "name": h.name, 
            "periodicity": h.periodicity,
            "created_at": h.created_at.isoformat(),
            "checks": check_list 
        })
    #write the list of habit dictionaries to a JSON file
    with open("habits.json", "w") as f:  #opening the JSON file in write mode
        json.dump(data, f,indent = 4)    # saving the data to the JSON file


def load_habits():
    """load habits from a habits.json file"""
    habits = []
    #Read the Json file and convert dictionaries back to Habit objects
    try:  # try-except method to handle case where no file exists
        #open the habits.json and load the data
        with open("habits.json", "r") as f:
            data = json.load(f)  # loading the data from the saved JSON file
            for i in data:       #iterating through each dictionary in the loaded data
                check_list = []
                for check in i["checks"]:
                    check_list.append(datetime.fromisoformat(check)) # datetime string converted back to datetime object 
                habit = Habit(i["name"], i["periodicity"])           # habit object creation using name and periodicity from the loaded data
                habit.created_at = datetime.fromisoformat(i["created_at"])  # converting the created_at string to datetime object
                habit.checks = check_list                                  # list of checks assigned to the habit object
                habits.append(habit)     # creation of habit objects from the loaded data
    #handle the case where the file does not exist (e.g., Running the program for the first time)

    except FileNotFoundError: # if no file exists pass and return an empty list
        pass

    #return the list of Habit objects after loading it from the JSON file
    return habits


                
        

