#!/usr/bin/python3
"""
Export all getten users tasks from api to a json format.
"""
import json
import requests

if __name__ == "__main__":
    u = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users/".format(u)).json()

    json_list = {}
    for user in users:
        id = user.get("id")
        name = user.get("username")
        print(name)
        todos_url = "{}/todos?userId={}".format(u, id)

        todos = requests.get(todos_url).json()

        todos_list = [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": name
            } for t in todos
        ]
        json_list.update({str(id): todos_list})

    f = open("todo_all_employees.json", 'w')
    json.dump(json_list, f)
    f.close()
