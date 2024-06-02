#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """Number of subs"""
    headers = {"User-Agent": "Chrome/125.0.0.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, allow_redirects=False)
    try:
        data = r.json()
        return data['data']['subscribers']
    except Exception:
        return 0
