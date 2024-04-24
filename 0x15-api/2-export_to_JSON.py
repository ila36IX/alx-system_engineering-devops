#!/usr/bin/python3
"""
Export getten data from api to a json format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    u = "https://jsonplaceholder.typicode.com"
    todos_url = "{}/todos?userId={}".format(u, id)
    infos_url = "{}/users/{}".format(u, id)

    todos = requests.get(todos_url).json()
    infos = requests.get(infos_url).json()

    name = infos.get("username")

    f = open(f"{id}.json", 'w')

    todos_list = [
        {
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": name
        } for t in todos
    ]
    json_list = {str(id): todos_list}
    json.dump(json_list, f)

    f.close()
