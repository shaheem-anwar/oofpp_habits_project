# Habit Tracker Application

An application backend developed in Python used for daily and weekly habit tracking. This application is built with Object-Oriented and Functional Python Programming (OOFPP). It includes Flask web UI, Pytest module for the testing of the functionalities.

## Requirements

- Python 3.7+ (3.12.10)
- Flask (`pip install flask`)
- pytest (`pip install pytest`)

Other dependencies like json and datetime comes under standard python library.

## Installation

### Option A: Via GitHub

1. Clone the repository:

git clone https://github.com/shaheem-anwar/oofpp_habits_project.git


2. Go into the project folder:

terminal command - cd oofpp_habits_project


3. Install dependencies:

terminal command - pip install -r requirements.txt


### Option B: Via ZIP file

1. Extract the ZIP file

2. Open the terminal and navigate into the extracted folder:

terminal command - cd path/to/extracted/folder

3. Install dependencies:

 terminal command - pip install -r requirements.txt


## Running the App

- The application can be started by the command:

terminal command - python app.py

- In the terminal a link to the UI will be displayed which can be accessed by Ctrl + Clicking.

## Running the Tests


pytest test.py


## Project Structure

- `app.py` - Flask web UI
- `habits.py` - Habit class
- `storage.py` - Load/save JSON
- `analytics.py` - Streak & analysis functions
- `test.py` - Unit tests
- `habits.json` - Data storage
- `templates/` - HTML pages for Flask UI

## Features

- Creating and deleting habits
- Marking habits as completed
- Viewing habits list (full list and filtered list based on periodicity)
- Longest streak calculation for all the habits and of a specific habit
- Most struggled habit analysis

## Predefined Data

The application comes with pre-stored example data which can be used for exploring the application. There are 5 exemplar habits stored in the `habits.json`.
