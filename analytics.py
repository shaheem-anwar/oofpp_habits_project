#importing necessary modules and classes
from datetime import timedelta
from storage import save_habits, load_habits


#defining the function for the most streak for a given habit
def longest_streak(habits, name):

    # if no habits are there then return 0
    if not habits:
        return 0
    
    #iterating through every habit object
    for h in habits:
        if h.name == name:      # if statement condition - if the habit name matches the given name
            if not h.checks:    # if no records then return 0
                return 0
            curr_streak = 1     #Intitializing the curr_streak variable
            max_streak = 1      #Intitializing the max_streak variable

            #if the periodicity is not daily or weekly, return 0 - crash handling
            if h.periodicity not in ("daily", "weekly"):
                return 0

            period_list = []
            # creating a list of dates from checks
            for c in h.checks:
                period_list.append(c.date())   #removing the time element from dattime object to extract only the dates
            period_list = sorted(period_list) 

            #iteration through the dates list to calculate the longest streak
            for i in range(len(period_list) - 1):
                current_period = period_list[i]
                next_period = period_list[i + 1]
                
                #Longest streak logic for daily habits
                if h.periodicity == "daily":
                    if (next_period - current_period).days == 1:
                        curr_streak += 1
                    else:
                        curr_streak = 1

                # Longest streak logic for weekly habits
                elif h.periodicity == "weekly":
                    if 7<=(next_period - current_period).days <14: # if difference is between 7 and 14 days, then it can be said that the habit was completed for the next week 
                        curr_streak += 1
                    else:
                        curr_streak = 1
                max_streak = max(curr_streak, max_streak)
            return max_streak    # return the longest streak 
    return 0  


#defining the longest streak from all the given habits
def longest_streak_all(habits):
    longest_streak_list = []   #initializing the longest streak list

    #iterating through each habit object from the list of habits
    for h in habits:
        if not h.checks:    #if there are no records in the checks, skip to the next habit
            continue
        #appending the longest streak with the habit name to the longest_streak_list as a tuple
        longest_streak_list.append((longest_streak(habits,h.name), h.name)) 
    
    # if no habits found, return an empty list - error handling
    if not longest_streak_list:
        return []
    longest_list = sorted(longest_streak_list,reverse=True)   # sorting it to get the longest streak among all the habits
    return longest_list

#Function for getting habits list
def all_habits_list(habits):
    # The logic is just to iterate through all the habits objects and appending its name to the list
    active_habits = []
    for h in habits:
        active_habits.append(h.name)
    return active_habits

#Function for habits list for the selected periodicity 
def habits_list(habits,periodicity):
    #The logic is to iterate through all the habits objects based on the condition of periodicity and appending h.name to the list
    habits_lists = []
    for h in habits:
        if h.periodicity==periodicity:
            habits_lists.append(h.name)
    return habits_lists

#function to identify the most struggled habit 
def most_struggled_habit(habits):
    # Handling error case when no habits are present
    if not habits:
        return 0, None
    
    longest_habit_list = []

    for h in habits:        #Iterating through every habit object 
        if not h.checks:    #error handling and skipping this iteration if "checks" is empty
            continue
        # Initializing variables and lists
        curr_struggle = 0
        max_struggle = 0
        check_list = []

        #Converting the checks from datetime to date
        for c in h.checks:
            check_list.append(c.date())
        check = sorted(check_list)    #sorting it to get the dates in order

        #Iterating through the dates list for longest streak calculation
        for i in range (0, len(check)-1):
            #Here the main logic is to find the difference between the current 
            #date and the next date, if the difference is more than 1 day for daily habits
            #or more than 7 days for weekly habits, then it can be concluded that the habit
            #was struggled for the number of days between the two dates
            current_period = check[i]
            next_period = check[i + 1]

            #Logic for daily habit's most struggled habit calculation
            if h.periodicity == "daily":
                if (next_period - current_period).days == 1:
                    curr_struggle = 0
                else:
                    curr_struggle = ((next_period - current_period).days - 1) 
            
            #Logic for weekly habit's most struggled habit calculation
            elif h.periodicity == "weekly":
                if 7 <= (next_period - current_period).days < 14: # if difference is between 7 and 14 days, then it can be said that the habit was struggled for 1 week
                    curr_struggle = 0
                else:
                    curr_struggle = ((next_period - current_period).days-1) // 7  #division by 7 to convert the days into weeks 

            max_struggle = max(max_struggle,curr_struggle)   # getting max struggle for the habit object      
        longest_habit_list.append((max_struggle,h.name))   # The final list for most struggled habit
                                                           # It has the max struggle number and habit name

    if not longest_habit_list:
        return 0, None

    longest_sorted= sorted(longest_habit_list, reverse=True)  # Sorting to get the most struggled habit
    max_value = longest_sorted[0][0]         
    most_struggled = longest_sorted[0][1]
    return max_value, most_struggled    #returning the most struggled habit and the number of struggles of that habit
