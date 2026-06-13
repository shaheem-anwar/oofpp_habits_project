from flask import Flask, render_template, request
import habits
from storage import load_habits, save_habits
from analytics import all_habits_list, longest_streak, longest_streak_all, most_struggled_habit, habits_list
from habits import Habit
from datetime import datetime


"""This is the UI part of the application. The Flask is the selected framework for the UI. 
The Falsk is a lightweight web framework that allows to create web applications
 It provides an easy way to handle routing, templates, and UI."""

app = Flask(__name__)    # Creation of the Flask application instance

"""The main logic of the app.py is to define routes for different functions of the application
and rendering (or displaying) the HTML templates for the defined routes. 
The HTML displayed are stored in the templates folder.
the @app.route() is a decorator in Flask that links a URL to a function.
Whenever a user clicks on a link or form submission, the corresponding function is executed linked to that URL."""

@app.route("/")   # This is route for the Dashboard of the Habit Tracker application. 
def main():                 
    return render_template("habit.html")      

@app.route("/view_all_habits")   # This is the route for viewing all the habits
def view_all_habits():
    habits = load_habits()
    all_habits = all_habits_list(habits)
    return render_template("all_habits.html", all_habits=all_habits)


@app.route("/add_new_habit" , methods = ["GET", "POST"])   # This is the route for adding a new habit 
def add_new_habit():

    #Takes the input from the user for the habit name and periodicity 
    #and creates habit object and saves it to the storage
    if request.method == "POST":
        name = request.form.get("habit_name")
        periodicity = request.form.get("periodicity")
        habit = Habit(name, periodicity)
        habits = load_habits()
        habits.append(habit)
        save_habits(habits)
    return render_template("new_habit.html")

@app.route("/mark_habit", methods = ["GET", "POST"])    # This is the route for marking a habit as complete. 
def mark_habit():
    habits = load_habits()
    # takes the name of the habit from the user and marks it as completed 
    if request.method == "POST":
        name_habit = request.form.get("habit_name")
        for h in habits:
            if h.name == name_habit:
                h.habit_complete()
        save_habits(habits) #Then it saves the updated habit data
    return render_template("habit_complete.html", habits=habits)

@app.route("/delete_habit" , methods = ["GET", "POST"])  # This is the route for deleting habits

def delete_habit():
    habits = load_habits()
    #takes input as the name of the habit and then deletes the habit object from the JSON file
    if request.method == "POST":
        name_habit = request.form.get("habit_name")
        for h in habits:
            if h.name == name_habit:
                habits.remove(h)   #Deletes the selected habit object 
        save_habits(habits)
    return render_template("delete.html", habits = habits)

@app.route("/habit_by_periodicity", methods = ["GET", "POST"]) # This is the route for viewing habits by periodicity
def habit_by_periodicity():
    habits = load_habits()
    sel = []
    filtered = []
    if request.method == "POST":
        sel = request.form.get("periodicity")
        filtered = habits_list(habits, sel)
    return render_template("habit_list_periodicity.html", habits=habits, filtered= filtered)

@app.route("/longest_streak_all") # This is the route for viewing longest streaks among all habits
def longest_streak_all_ui():
    habits = load_habits()
    longest_streaks = longest_streak_all(habits)
    return render_template("longest_streak_all.html", longest_streaks=longest_streaks, habits=habits)

@app.route("/longest_streak_by_habit", methods=["GET", "POST"]) # This is the route for viewing longest streak from a given habit

def longest_streak_by_habit():
    habits = load_habits()
    longest_streak_by_habit = None
    name = None
    #takes the name of the habit from the user and calculates the streak
    if request.method == "POST":
        name = request.form.get("habit_name")
        longest_streak_by_habit = longest_streak(habits, name)
    return render_template(
        "longest_streak_specific.html",habits=habits, longest_streak_by_habit=longest_streak_by_habit, name= name )

@app.route("/most_struggles_habit") # This is the route for viewing the most struggled habit among all the habits

def most_struggled():
    habits = load_habits()
    struggled = most_struggled_habit(habits)
        
    return render_template("most_struggled.html", struggled = struggled)


# This is the route for exiting the application. It displays a greeting message set on the time of the day.
@app.route("/exit")
def exit():

    now = datetime.now().hour

    message = "Get back soon and don't break your streaks!"

    if 5 <= now < 12:
        greeting = "Good Morning ☀️"

    elif 12 <= now < 17:
        greeting = "Good Afternoon 🌤️"

    elif 17 <= now < 21:
        greeting = "Good Evening 🌇"

    else:
        greeting = "Good Night 🌙"

    return render_template(
        "exit.html",
        greeting=greeting,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
