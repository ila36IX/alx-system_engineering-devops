#!/usr/bin/python3
"""
count
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def page_hots(subreddit, hot_list, after_query=""):
    """Get host posts in one page"""
    base_url = "https://www.reddit.com"
    endpoint = base_url + "/r/{}/hot.json".format(subreddit)
    payload = {'after': after_query}
    r = requests.get(
        endpoint,
        allow_redirects=False,
        params=payload,
        headers={**headers}
    )
    if r.status_code != 200:
        return None
    r = r.json()
    after = r.get('data').get('after')
    hot_posts = r.get('data').get('children')
    for post in hot_posts:
        hot_list.append(post.get('data').get('title'))
        print('-', post.get('data').get('title'))
    return after


def recurse(subreddit, hot_list=[]):
    """Get all the hot posts"""
    if type(subreddit) is list:
        subreddit, after = subreddit[0], subreddit[1]
        # print("{)", subreddit, after)
        after = page_hots(subreddit, hot_list, after)
    else:
        after = page_hots(subreddit, hot_list)
    if after:
        recurse([subreddit, after], hot_list)
    return hot_list
