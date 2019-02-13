#!/usr/bin/python3
''' contains recurse function'''
from requests import get


def recurse_help(subreddit, a, hot_list=[]):
    """help to recurse func"""
    qu = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    if not a:
        qu = qu + '?after=' + str(a)
    r = get(qu, headers={'User-Agent': 'Super Meat-Boy'},
            allow_redirects=False)
    if r.status_code == 200:
        ri = r.json()
        data = ri.get('data')
        a = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list += [child.get('data').get('title')]
        if a:
            return recurse_help(subreddit, a, hot_list)
        return hot_list
    return None


def recurse(subreddit, hot_list=[]):
    """ returns a list of the titles of the hot articles given"""
    a = ''
    return recurse_help(subreddit, a, hot_list)
