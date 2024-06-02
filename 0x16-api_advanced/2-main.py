#!/usr/bin/python3
"""
2-main
"""
import sys

# def test(i, l=[]):
#     if i < 10:
#         l.append(i)
#         test(i + 1, l)
#     return l
if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
