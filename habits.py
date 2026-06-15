from datetime import datetime
#define a Habit class 
class Habit:
    """The Habit Class is the main component of the Habit Tracker
    application which is the core blueprint of the habit objects which
    has the following components - Attributes & Methods """
    
    
    def __init__(self, name, periodicity):
        """constructor to initialize habit attributes (which is the blueprint of the habit object)"""
        self.name = name                    # habit name
        self.periodicity = periodicity      # "daily" or "weekly" periods
        self.created_at = datetime.now()    # when habit was created
        self.checks = []                    # list of completion timestamps

     
    def marked_already(self, now):
        """check if the habit is marked already for the current period"""

        #If no records are present in the list of checks, return False (Red flag)
        if len(self.checks) == 0:
            return False

        last_check = self.checks[-1]   # the last checked habit timestamp

        #check if the last checked habit timestamp is in the given period
        if self.periodicity == "daily":
            if last_check.date() == now.date(): 
                return True    # if its the same day, return True

        elif self.periodicity == "weekly":
            if last_check.isocalendar()[:2] == now.isocalendar()[:2]:  # Get the week number of last completion and the current date
                return True    # if its the same week, return True

        return False  
      
    
    def habit_complete(self):
        """defining a method to mark the habit as complete for the current period"""
        now = datetime.now()          # stores the current date in the variable "now"
        #prevent duplicate habit_check
        if self.marked_already(now):
            return False
        #adding the current timestamp to the checks list of the habit object
        self.checks.append(now)   #appends the current timestamp to the list of checks for the habit object
        return True # the green flag to the habit completion

 
