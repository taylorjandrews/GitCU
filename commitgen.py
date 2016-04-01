"""GitCU Data Mining Project Spring 2016
   Created by: Taylor Andrews
   Modified: 2016/03/31 

   Script to generate commits from repositories.
"""
import requests
import json
import csv
import os
from time import sleep

def get_commit_urls(data):
    """Given GitHub repository data for a user, fetch the commit urls.

    Args:
        data: a json file containing repository information.

    Returns:
        A list of commit urls to fetch more information about. 
    """
    commits = []

    for repo in data:
        if 'commits_url' in repo:
            commits.append(repo['commits_url'])

    return commits

def create_userdir(username):
    """Given a username, create a directory in the commits folder.

    Args:
        username: the name of a GitHub user.

    Returns:
        The name of the directory created by this method. 
    """
    dirname = './data/commits/' + username
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    return dirname + '/'

def fetch_commits(user, data):
    """Given a user and a list of their commits, fetch information about these commits.

    Args:
        user: the name of a GitHub user.
        data: list of GitHub commits.
    """
    dirname = create_userdir(user)

    for commit in data:
        url = commit.split('/')[5]
        print("Mining {}/{}...".format(user, url), end='', flush=True) 

        r = requests.get(commit.split('{')[0]).json()
        store_commit(dirname, url, r)

        sleep(60)
        print("finished!!!")


def store_commit(dirname, url, commit):
    """Given a specific directory, store commit information in that directory.    

    Args:
        dir: the name of a directory to store information in.
        url: part of the url of the commit to use as a filename.
        commit: the data corresponding to a specific GitHub commit.
    """
    filename = dirname + url + ".json"
    
    with open(filename, 'wb') as f:
        f.write(bytes(json.dumps(commit, indent=2), 'UTF-8'))

def main():
    for f in os.listdir('./data/repos'):
        with open('./data/repos/' + f, 'r') as repo:
            data = json.load(repo)	
            username = '-'.join(repo.name.split('-')[2:]).split('.')[0]
            commits = get_commit_urls(data)
            fetch_commits(username, commits)

if __name__ == '__main__':
    main()