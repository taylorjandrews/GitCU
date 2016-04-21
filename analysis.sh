#!/bin/bash
rm result-repo.csv
echo  "name,repos,forked_from,forks,watchers,stars,fav_lang,avg_size" >> result-repo.csv
for file in $(ls ./data/repos/); do
	python3 analysis-repos.py $file
done 