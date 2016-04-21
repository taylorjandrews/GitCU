import sys
import csv
import numpy

def grab_index(attribute, openedfile):
	reader = csv.reader(openedfile)
	header = next(reader)
	index = 0
	for x in range(0, len(header)):
		if(header[x] == attribute):
			index = x
	return index

def grab_attribute_arrays(attribute):
	githubfile = open("./result-githubrepo.csv", "r")
	reader = csv.reader(githubfile)
	header = True
	index = grab_index(attribute, githubfile)
	gitgrabbed = []
	for row in reader:
		gitgrabbed.append(row[index])
	githubfile.close()
	
	cufile = open("./result-repo.csv", "r")
	reader = csv.reader(cufile)
	next(reader)
	cugrabbed = []
	for row in reader:
		cugrabbed.append(row[index])
	cufile.close()
	return (gitgrabbed, cugrabbed)
	
def bin(arr, ranges):
	results = {'0-25': 0, '25-50': 0, '50-75':0, "75-100":0}
	for x in arr:
		if(x < ranges['q1']):
			results['0-25'] = results['0-25'] + 1
		elif(x >= ranges['q1'] and x < ranges['q2']):
			results['25-50'] = results['25-50'] + 1
		elif(x >= ranges['q2'] and x < ranges['q3']):
			results['50-75'] = results['50-75'] + 1
		else:
			results['75-100'] = results['75-100'] + 1
	return results

def percentbins(bins, arr):
	bins['0-25'] = format(bins['0-25']/len(arr), '.2f')
	bins['25-50'] = format(bins['25-50']/len(arr), '.2f')
	bins['50-75'] = format(bins['50-75']/len(arr), '.2f')
	bins['75-100'] = format(bins['75-100']/len(arr), '.2f')
	return bins

def percenttranslator(untrans, ranges):
	if(untrans <= ranges['minval'] or untrans < ranges['q1']):
		return "0-25"
	elif(untrans >= ranges['q1'] and untrans < ranges['q2']):
		return "25-50"
	elif(untrans >= ranges['q2'] and untrans < ranges['q3']):
		return "50-75"
	else:
		return "75-100"

def getranges(arr):
	minval, q1, q2, q3, maxval = numpy.percentile(arr, [0, 25, 50, 75, 100])
	return {'minval': minval, 'q1': q1, 'q2': q2, 'q3': q3, 'maxval': maxval}

def translate():
	attributes = ['name','repos','forked_from','forks','watchers','stars','fav_lang','avg_size']
	translated = open("./result-repo-translated.csv", "w")
	untranslated = open("./result-repo.csv", "r")
	writer = csv.writer(translated)
	writer.writerow(attributes)
	reader = csv.reader(untranslated)
	next(reader)
	for row in reader:
		rowbuffer = []
		for attribute in attributes:
			header = open("./result-repo.csv", "r")
			index = grab_index(attribute, header)
			header.close()
			(gitattr, cuattr) = grab_attribute_arrays(attribute)
			if(attribute == 'name' or attribute == 'fav_lang'):
				rowbuffer.append(row[index])
			else:
				gitattr = list(map(float, gitattr))
				ranges = getranges(gitattr)
				rowbuffer.append(percenttranslator(float(row[index]), ranges) + " " + attribute)
		print(rowbuffer)
		writer.writerow(rowbuffer)

	translated.close()
	untranslated.close()
def show_percentiles(attribute):
	(gitresults, curesults) = grab_attribute_arrays(attribute) 
	gitresults = list(map(int, gitresults))
	curesults = list(map(int, curesults))
	ranges = getranges(gitresults)
	print(ranges)
	bins = bin(curesults, ranges)
	print("total number in percentiles", bins)
	percbins = percentbins(bins, curesults)
	print("percent of number in percentiles", percbins)

choice = "0"
while(choice != "3"):
	choice = input('press 1 to write new translation, 2 to search for the percentiles of an attribute, 3 to exit: ')
	if(choice == "1"):
		translate()
	elif(choice == "2"):
		attribute = input('attribute (repos, forked_from, forks, watchers, stars, avg_size): ')
		show_percentiles(attribute)
	elif(choice == "3"):
		exit(0)
	else:
		print("please input a correct option\n")