"""GitCU Data Mining Project Spring 2016
   Created by: Taylor Andrews
   Modified: 2016/03/24 

   Script to generate a list of repositories from a list of 
   GitHub users.
"""
import requests
import json
import csv
from time import sleep
import pydash

def get_repositories(user):
	"""Given a GitHub user, query Github for corresponding repositories.

	Args:
		user: a user to scan the Github repositories of.

	Returns:
		A list of json data about Github repositories corresponding to the desired user. 
	"""
	print("Mining {}...".format(user), end='', flush=True) 
		
	req_string = "https://api.github.com/users/" + user + "/repos"
	r = requests.get(req_string, headers = {'Authorization': 'token 6ca2047ccbab4ad1a2f472e35e2e659c8861bfb7'}).json()

	print("finished!!!")

	return r

def store_repositories(user, data):
	"""Given a specific user and information about the repositories owned by that user,
	   store that data in a file.    

	Args:
		user: a specific user to record information about.
		data: json data about Github repositories.
	"""
	filename = "./data/githubrepos/github-user-" + user + ".json"
	
	with open(filename, 'wb') as f:
		f.write(bytes(json.dumps(data, indent=2), 'UTF-8'))

def main():
	user_list = []

	with open("./data/github-users.csv") as f:
		reader = csv.reader(f)
		# next(reader) # Skip the first line
		# header = True;
		for row in reader:
			# if(header):
				# header = False
			user_list.append(row[0])
				
	user_list = pydash.chain(user_list).uniq().sort().value()
	
	for user in user_list:
		repos = get_repositories(user)
		store_repositories(user, repos)

if __name__ == '__main__':
	main()