#!/usr/bin/python3
"""Data in the CSV format"""
import requests
from sys import argv

# Check if the script is being run as the main program
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1]))
    user_json = user.json()  # Send an HTTP GET request to retrieve a list of tasks (todos) for the same user

    tasks = requests.get(url + "todos?userId={}".format(argv[1]))
    tasks_json = tasks.json()

    completed = []
    for i in tasks_json:
        if i.get("completed") is True:
            completed.append(i.get("title"))

    # EMPLOYEE_NAME: name of the employee
    EMPLOYEE_NAME = user_json.get("name")
    NUMBER_OF_DONE_TASKS = len(completed)  # Number of completed tasks

    # Number of completed tasks (completed + non-completed tasks)
    TOTAL_NUMBER_OF_TASKS = len(tasks_json)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for TASK_TITLE in completed:
        print("\t {}".format(TASK_TITLE))
