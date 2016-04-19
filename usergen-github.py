import requests
import json
import pydash

def getPages():
    users = []

    print("Getting Smiths...") 
    smiths = []
    for page in range(0, 10):
        req_string = "https://api.github.com/search/users?page="+str(page)+"&q=smith&per_page=500"
        smiths.append(requests.get(req_string, headers = {'Authorization': 'token 6ca2047ccbab4ad1a2f472e35e2e659c8861bfb7'}).json())
    print("got Smiths")

    print("Getting Johnsons...") 
    johnsons = []
    for page in range(0, 10):
        req_string = "https://api.github.com/search/users?page="+str(page)+"&q=johnson&per_page=500"
        johnsons.append(requests.get(req_string, headers = {'Authorization': 'token 6ca2047ccbab4ad1a2f472e35e2e659c8861bfb7'}).json())
    print("got Johnsons")
    
    return (smiths, johnsons)


(smiths, johnsons) = getPages()

smithlogins = []
for page in smiths:
    pydash.for_each(page['items'], lambda x: smithlogins.append(x['login']))

johnsonlogins = []
for page in johnsons:
    pydash.for_each(page['items'], lambda x: johnsonlogins.append(x['login']))

logins = smithlogins + johnsonlogins
loginstr = "\n".join(logins)

resultfile = open('./data/github-users.csv', 'w')
resultfile.write(loginstr)
resultfile.close()
