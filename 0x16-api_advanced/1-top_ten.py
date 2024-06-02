#!/usr/bin/python3
"""
Top 10
"""
import requests


headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def top_ten(subreddit):
    base_url = "https://www.reddit.com"
    endpoint = base_url + "/r/{}/hot.json".format(subreddit)
    r = requests.get(endpoint, allow_redirects=False, headers=headers)
    if r.status_code != 200:
        print("None")
        return
    hot_posts = r.json().get('data').get('children')
    for post in hot_posts[:10]:
        print(post.get('data').get('title'))
