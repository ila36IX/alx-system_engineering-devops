#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    base_url = "https://www.reddit.com"
    endpoint = base_url + "/r/{}/about.json".format(subreddit)
    r = requests.get(endpoint, allow_redirects=False)
    if r.status_code != 200:
        return 0
    response = r.json().get('data')
    num_subs = response.get('subscribers')
    return num_subs
