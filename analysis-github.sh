#!/bin/bash
rm result-githubrepo.csv
echo  "name,repos,forked_from,forks,watchers,stars,fav_lang,avg_size" >> result-githubrepo.csv
for file in $(ls ./data/githubrepos/); do
	python3 analysis-githubrepos.py $file
done 