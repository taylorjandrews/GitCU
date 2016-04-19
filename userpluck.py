import json
import pydash
import sys
resultsfile = open('github-names.csv', 'a')
openedfile = open("./data/users.json", "r")
jsonstring = ""
readfile = openedfile.readlines()
for string in readfile:
	jsonstring += string
data = json.loads(jsonstring)
results = pydash.pluck(data, 'login')
results = ",".join(results)
resultsfile.write(results)
openedfile.close()
resultsfile.close()