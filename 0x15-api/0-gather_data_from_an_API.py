#!/usr/bin/python3
import requests
from sys import argv

# Check if the script is being run as the main program
if __name__ == "__main":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + argv[1]).json()
    # Send an HTTP GET request to retrieve a list of tasks (todos) for the same user

    tasks = requests.get(url + "todos?userId=" + argv[1]).json()

    completed = []
    for i in tasks:
        if i.get("completed") is True:
            completed.append(i.get("title"))

    # "brahim"  # EMPLOYEE_NAME: name of the employee
    EMPLOYEE_NAME = user.get("name")
    NUMBER_OF_DONE_TASKS = len(completed)  # number of completed tasks

    # number of completed tasks [completed + non-completed] tasks
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    # TASK_TITLE = "task title"

    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for TASK_TITLE in completed:
        print(f"\t {TASK_TITLE}")

