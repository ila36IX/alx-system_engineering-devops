#!/usr/bin/python3
"""
Export getten data from api to a CSV format.
"""
import csv
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

    f = open(f"{id}.csv", 'w')
    c = csv.writer(f, quoting=csv.QUOTE_ALL)
    for todo in todos:
        c.writerow([id, name, todo.get("completed"), todo.get("title")])
    f.close()
