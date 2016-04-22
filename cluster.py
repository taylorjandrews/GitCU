from pylab import plot, show
from numpy import vstack, asarray
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq
import csv

def kmeanscluster(x, y, k=3):
	points = []
	for i in range(len(x)):
		points.append([x[i], y[i]])
	
	# Help from http://glowingpython.blogspot.com/2012/04/k-means-clustering-with-scipy.html
	data = asarray(points)
	centroids,_ = kmeans(data, k)
	idx,_ = vq(data,centroids)

	plot(data[idx==0,0],data[idx==0,1],'ob',
	     data[idx==1,0],data[idx==1,1],'or',
	     data[idx==2,0],data[idx==2,1],'oy')
	plot(centroids[:,0],centroids[:,1],'sg',markersize=15)
	show()

def main():
	x = 7
	y = 8
	repos = []
	size = []

	with open("./data/result-repo.csv") as f:
		reader = csv.reader(f)
		next(reader) # Skip the first line

		for row in reader:
			repos.append(float(row[x]))
			size.append(float(row[y]))

	kmeanscluster(repos, size)


	with open("./data/result-githubrepo.csv") as f:
		reader = csv.reader(f)
		next(reader) # Skip the first line

		for row in reader:
			repos.append(float(row[x]))
			size.append(float(row[1]))

	kmeanscluster(repos, size)

if __name__ == '__main__':
    main()