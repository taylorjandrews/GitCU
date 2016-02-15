"""GitCU Data Mining Project Spring 2016
   Created by: Taylor Andrews
   Modified: 2016/02/11 

   Script to generate a list of Github users who have created repositories
   related to CU Boulder computer science courses. 
"""
import requests
import json
from time import sleep

def store_user_data(users):
    """Given a dictionary of Github users, write that information to a file.

    Args:
        users: a dictionary of Github users.
    """
    filename = "./data/gitCU-users.csv"
    
    with open(filename, 'ab') as f:
        f.write(bytes("Username, Frequency\n", 'UTF-8'))
        for user, freq in users.items():
            output = user + "," +  str(freq) + "\n"
            f.write(bytes(output, 'UTF-8'))

def store_class_data(class_name, data):
    """Given a specific class and data about Github repositories pertaining to that class,
       store that data in a file.    

    Args:
        class_name: a specific class to record information about.
        data: json data about Github repositories.
    """
    filename = "./data/classes/gitCU-" + class_name + ".json"
    
    with open(filename, 'wb') as f:
        f.write(bytes(json.dumps(data, indent=2), 'UTF-8'))

def generate_repositories(classes):
    """Given a list of classes, query Github for corresponding repositories.

    Note:
        This function will write repository data on a per-class basis to output files.

    Args:
        classes: a list of desired classes to scan Github repositories for.

    Returns:
        A list of json data about Github repositories corresponding to the desired classes. 
    """
    repos = []
    
    for c in classes:
        print("Mining CSCI{}...".format(c), end='', flush=True) 
        
        req_string = "https://api.github.com/search/repositories?q=csci+" + c + "&per_page=500"
        r = requests.get(req_string).json()
        store_class_data(c, r)
        repos.append(r)
        
        sleep(10)
        print("finished!!!")

    return repos

def retrieve_users(c):
    """Given json data about a Github repository retrieve the username of the user who 
       created that repository.

    Args:
        c: a class in json format.

    Returns:
        A list of users who created the mined Github repositories for a given class.
    """
    users=[]

    for item in c['items']:
        users.append(item['owner']['login'])

    return users

def record_users(users, user_dict):
    """Given a list of users, update how many of times these users appear in a dictionary.
       If they do not yet appear in the dictionary, add them..

    Args:
        users: a list of users.
        user_dict: a dictionary to collect usernames and frequencies.

    Returns:
        The updated user_dict.
    """
    for user in users:
        if user in user_dict:
            user_dict[user] += 1
        else:
            user_dict[user] = 1

    return user_dict

def main():
    class_list = ['1300', '2270', '2400', '3104', '3155', '3202', '3287', '3308', '3753', '4229', '4273', '4448', '4830']
    """class_list contains the following selected courses: 
        Computer Science 1: Starting Computing,
        Computer Science 2: Data Structures,
        Computer Systems,
        Algorithms,
        Principles of Programming Languages,
        Introduction to Artificial Intelligence,
        Database and Information Systems,
        Software Development Methods and Tools,
        Operating Systems,
        Computer Graphics,
        Network Systems,
        Object-Oriented Analysis and Design,
        Special Topics
    """
    
    user_dict = {}
    class_repos = generate_repositories(class_list)

    for c in class_repos:
        users = retrieve_users(c)
        user_dict = record_users(users, user_dict)

    store_user_data(user_dict)

if __name__ == '__main__':
    main()
