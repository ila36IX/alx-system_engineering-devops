#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    u = "https://jsonplaceholder.typicode.com"
    todos_url = "{}/todos?userId={}".format(u, id)
    infos_url = "{}/users/{}".format(u, id)

    todos = requests.get(todos_url).json()
    infos = requests.get(infos_url).json()

    name = infos.get("name")
    all_todos = len(todos)
    comp_todos = list(filter(lambda t: t.get("completed"), todos))

    print("Employee {} is done with tasks({}/{}):".
          format(name, len(comp_todos), all_todos))
    for todo in comp_todos:
        print("\t {}".format(todo.get("title")))
