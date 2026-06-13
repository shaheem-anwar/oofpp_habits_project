from datetime import  datetime
from storage import save_habits, load_habits
from habits import Habit
from analytics import all_habits_list, habits_list, longest_streak, longest_streak_all, most_struggled_habit

"""test for core functions of the habit tracker application
Here Pytest framework is used to test the core functions of the application. 
Pytest is a popular testing framework in Python that 
allows to write simple test cases for code fucntions and classes
It helps in writing, organizing, and running tests."""


def test_no_multiple_daily_habit_marking():
    """The test for - 1. No multiple daily habit marking"""
    habit = Habit("Read", "daily")

    first_mark = habit.habit_complete()
    second_mark = habit.habit_complete()

    #assert statements are used to match the expected output with the original output 
    assert first_mark is True
    assert second_mark is False
    assert len(habit.checks) == 1


def test_no_multiple_weekly_habit_marking():
    """test for - 2. No multiple weekly habit marking"""
    habit = Habit("Swimming", "weekly")

    first_mark = habit.habit_complete()
    second_mark = habit.habit_complete()

    assert first_mark is True
    assert second_mark is False
    assert len(habit.checks) == 1


def test_longest_streak():
    """test for - 3. Longest streak calculation - specific habit"""
    habit = Habit("Exercise", "daily")
    habit.checks = [datetime(2026, 5, 1), datetime(2026, 5, 2), datetime(2026, 5, 3), datetime(2026, 5, 5)]
    assert longest_streak([habit], "Exercise") == 3


def test_longest_streak_all():
    """test for - 4. Longest streak calculation - all habits"""
    habit1 = Habit("Exercise", "daily") # Creating habits
    #adding checks for the habit
    habit1.checks = [
        datetime(2026, 5, 1),
        datetime(2026, 5, 2),
        datetime(2026, 5, 3),
        datetime(2026, 5, 5),
]

    habit2 = Habit("Read", "daily")
    habit2.checks = [
        datetime(2026, 5, 1),
        datetime(2026, 5, 3),
        datetime(2026, 5, 4),
    ]

    habit3 = Habit("Run", "daily")
    habit3.checks = [
        datetime(2026, 5, 1),
        datetime(2026, 5, 2),
        datetime(2026, 5, 4),
        datetime(2026, 5, 5),
    ]

    habits = [habit1, habit2, habit3]

    result = longest_streak_all(habits)
    assert result == [(3, "Exercise"), (2, "Run"), (2, "Read")]


def test_all_habits_list():
    """test for - 5. All habits list"""
    habit1 = Habit("Exercise", "daily")
    habit2 = Habit("Read", "weekly")
    habit3 = Habit("Run", "daily")
        
    habits = [habit1, habit2, habit3]
        
    result = all_habits_list(habits)
    assert result == ["Exercise", "Read", "Run"]


def test_habit_list():
    """test for - 6. Habits list - daily or weekly"""
    habit1 = Habit("Exercise", "daily")
    habit2 = Habit("Read", "weekly")
    habit3 = Habit("Run", "daily")
    
    habits = [habit1, habit2, habit3]
        
    result = habits_list(habits, "daily")
    assert result == ["Exercise", "Run"]

 
def test_most_struggled_habit():
    """test for - 7. Most struggled habit"""
    habit1 = Habit("Exercise", "daily")  #Creating habit for the test
    habit1.checks = [
        datetime(2026, 5, 1),
        datetime(2026, 5, 3),
        datetime(2026, 5, 4),
    ]

    habit2 = Habit("Read", "weekly")
    habit2.checks = [
        datetime(2026, 5, 1),
        datetime(2026, 5, 8),
    ]

    habit3 = Habit("Run", "daily")
    habit3.checks = [
        datetime(2026, 5, 1),
        datetime(2026, 5, 2),
        datetime(2026, 5, 4),
        datetime(2026, 5, 5),
    ]

    habits = [habit1, habit2, habit3]

    result = most_struggled_habit(habits)
    assert result == (1, "Run")
    

def test_save_load_habit():
    """test for - 8. Saving and loading habits from the storage
    Take snapshot of current habits data as to recover it after the test
    (the test deletes all the current data) """
    habit_snapshot = load_habits()

    # Here try-finally blocks are used to make sure even if the assertion fails,
    # the habits are succesfully loaded back.
    try:
        habit_1 = Habit("Riding", "daily")
        habit_1.created_at = datetime(2026, 5, 1)
        habit_1.checks = [datetime(2026, 5, 1), datetime(2026, 5, 2)]

        save_habits([habit_1])
        loaded_habits = load_habits()

        assert len(loaded_habits) == 1
        assert loaded_habits[0].name == "Riding"
        assert loaded_habits[0].periodicity == "daily"
        assert loaded_habits[0].created_at == habit_1.created_at
        assert loaded_habits[0].checks == habit_1.checks

        for h in loaded_habits:
            if h.name == "Riding":
                loaded_habits.remove(h)

    finally:
        # Restore snapshot even if test fails
        save_habits(habit_snapshot)         
