#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    base_url = "https://www.reddit.com"
    endpoint = base_url + "/r/{}/about.json".format(subreddit)
    subs = None
    while subs is None:
        try:
            r = requests.get(endpoint, allow_redirects=False)
            if r.status_code in (301, 302):
                return 0
            response = r.json().get('data')
            subs = response.get('subscribers')
        except Exception as e:
            subs = None
    subs = response.get('subscribers')
    return subs
