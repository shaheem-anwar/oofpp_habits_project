

""" This module uses Functional Programming - It is a type of programming paradigm in which 
the program is built using the functions which returns results
after processing some data. The habit tracker app takes input as habit data, 
calculate streaks/ statistics and return results  The functional
programming tools used here are: 
- map() - applies function to all the items of the list
- filter() - conditional filtering of items in a list
- lambda - used to write one-line functions without defining it seperately
- sorted() - sorts the lists
- next() - returns the next matching item from an iterating object
- max() - it is used to get highest value from the results"""

def longest_streak(habits, name):
    """defining the function for the most streak for a given habit"""

    # Find the habit from the name provided
    # next() returns the first matching habit from the given name.
    # If habit is not found returns None.
    habit = next((h for h in habits if h.name == name), None)

    # If habits markings (Checks) are not there then it returns 0
    if not habit or not habit.checks:
        return 0

    # creating a list of dates from checks
    #removing the time element from dattime object to extract only the dates    
    period_list = sorted(map(lambda c: c.date(), habit.checks))

    curr_streak = 1     #Intitializing the curr_streak variable
    max_streak = 1      #Intitializing the max_streak variable

    #iteration through the dates list to calculate the longest streak
    for i in range(len(period_list) - 1):
        current_period = period_list[i]
        next_period = period_list[i + 1]
                
        #Longest streak logic for daily habits
        if habit.periodicity == "daily":
            if (next_period - current_period).days == 1:
                curr_streak += 1
            else:
                curr_streak = 1

        # Longest streak logic for weekly habits
        elif habit.periodicity == "weekly":
            if 7<=(next_period - current_period).days <14: # if difference is between 7 and 14 days, then it can be said that the habit was completed for the next week 
                curr_streak += 1
            else:
                curr_streak = 1
        max_streak = max(curr_streak, max_streak)
    return max_streak    # return the longest streak 


def longest_streak_all(habits):
    """defining the longest streak from all the given habits"""

    longest_streak_list = list(
        map(lambda h: (longest_streak(habits, h.name), h.name),   # map() creates a tuple which returns- (longest streak (in numbers), habit name)
            filter(lambda h: h.checks, habits)))                 # The filter() filter out the habits withoit checks
    longest_streak_list = sorted(longest_streak_list, reverse = True) # sorting it to get the longest streak among all the habits in the first index
    
    return longest_streak_list

def all_habits_list(habits):
    """Function for getting habits list.
    The logic is just to iterate through all the habits objects and appending its name to the list"""

    active_habits = [h.name for h in habits]  #it iterates over all the habits data list and
                                                #returns a list of habit names

    return active_habits

def habits_list(habits,periodicity):
    """Function for habits list for the selected periodicity
    The logic is to iterate through all the habits objects based on the condition 
    of periodicity and appending h.name to the list"""

    #here lambda function 
    habits_lists = [h.name for h in filter(lambda h: h.periodicity == periodicity, habits)]
    return habits_lists

def most_struggled_habit(habits):
    """function to identify the most struggled habit"""
    
    # Handling error case when no habits are present
    if not habits:
        return 0, None
    
    longest_habit_list = []

    for h in habits:        #Iterating through every habit object 
        if not h.checks:    #error handling and skipping this iteration if "checks" is empty
            continue

        max_struggle = 0

        check = sorted(map(lambda c: c.date(), h.checks))  #Converting the checks from datetime to date and sorting it to get the dates in order

        #Iterating through the dates list for longest streak calculation
        for i in range(0, len(check)-1):
            #Here the main logic is to find the difference between the current 
            #date and the next date, if the difference is more than 1 day for daily habits
            #or more than 7 days for weekly habits, then it can be concluded that the habit
            #was struggled for the number of days between the two dates
            current_period = check[i]
            next_period = check[i + 1]

            #Logic for daily habit's most struggled habit calculation
            if h.periodicity == "daily":
                curr_struggle = 0 if (next_period - current_period).days == 1 else (next_period - current_period).days - 1
            
            #Logic for weekly habit's most struggled habit calculation
            elif h.periodicity == "weekly":
                # if difference is between 7 and 14 days, there is no struggle
                # the range of days (7-14 days) are given as a weekly habit can be completed at any time within a week
                # if difference exceeds 14 days, division by 7 converts the missed days into weeks
                curr_struggle = 0 if (next_period - current_period).days < 14 else ((next_period - current_period).days - 1) // 7

            max_struggle = max(max_struggle, curr_struggle)   # getting maximum struggle for the habit object      
        longest_habit_list.append((max_struggle, h.name))   # The final list of tuples with max struggle number and habit name

    if not longest_habit_list:
        return 0, None

    longest_sorted = sorted(longest_habit_list, reverse=True)  
    # Sorting to get the most struggled habit (if there's a tie between multiple habits, then 
    # the most struggled habit will be the one which appears first after sorting)
    max_value = longest_sorted[0][0]         
    most_struggled = longest_sorted[0][1]
    return max_value, most_struggled    #returning the most struggled habit and the number of struggles of that habit