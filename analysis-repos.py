import json
import pydash
import sys

def analysis(infile, outfile):
	openedfile = open("./data/repos/"+infile, "r")
	name = infile[11:-5]
	jsonstring = ""
	readfile = openedfile.readlines()
	for string in readfile:
		jsonstring += string
	data = json.loads(jsonstring)

	repos = len(data)
	sizes = pydash.chain(data).filter_(lambda x: x['size'] != None).pluck('size').value()
	avg_size = float(sum(sizes))/float(len(sizes))
	languages = pydash.chain(data).filter_(lambda x: x['language'] != None).sort_by('language').pluck('language').value()
	stars = pydash.chain(data).filter_(lambda x: x['stargazers_count'] != None).pluck('stargazers_count').sum().value()
	watchers = pydash.chain(data).filter_(lambda x: x['watchers'] != None).pluck('watchers').sum().value()
	forks = pydash.chain(data).filter_(lambda x: x['forks_count'] != None).pluck('forks_count').sum().value()
	forked_from= pydash.chain(data).pluck('fork').map_(lambda x: 1 if x else 0).sum().value()
	def most_common(lst):
	    return max(set(lst), key=lst.count)
	if languages:
		fav_lang = most_common(languages)
	else:
		fav_lang = "None"
	results = [str(name), str(repos), str(forked_from), str(forks), str(watchers), str(stars), fav_lang, str(avg_size)+'\n']
	results = ",".join(results)
	print(results)
	resultsfile.write(results)
	openedfile.close()

resultsfile = open('result-repo.csv', 'a') # or 'a' to add text instead of truncate
analysis(str(sys.argv[1]), resultsfile)
resultsfile.close()
