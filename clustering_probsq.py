import sys
import math
import random
import subprocess
import matplotlib.pyplot as plt
from scipy import spatial
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import pprint
from collections import Counter
import pickle
'''
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica
'''

x,y,z,w = [],[],[],[] #attribute lists
K = 7 #number of nearest neighbors
positions = [] #list of nearest neighbor positions
labels = [] #list of labels for each data point

def main():
	global labels,positions
	f = open('iris.data','r')
	for line in f:
		if line!='\n':
			arr = line.split(',')
			x.append(round(float(arr[0]),1))
			y.append(round(float(arr[1]),1))
			z.append(round(float(arr[2]),1))
			w.append(round(float(arr[3]),1))
	coordset = zip(z,w)
	coords = list(set(coordset))
	labels = [random.randint(1,3) for i in xrange(len(coords))] 
#	labels_org = [] 
#	labels_org = list(labels) #original labels list 
		

	tree = spatial.KDTree(coords) #constructing the Kd tree
	itr = 1
	prev_count = 0
	quit_count = 1
	clustering = []
	clustering_toplot = []

	for i in range(len(coords)):
			pos = tree.query(coords[i],k=K,p=2)[1] 
			positions.append(pos)

	while True:
		changecount = 0
		#labels = [random.randint(1,3) for i in xrange(len(coords))] 
		for i in range(len(coords)):
			prevlabel = labels[i]
			labels[i] = findMajorityLabel(positions[i]) #changing the point's label
			current = labels[i]
			if prevlabel!=current:
				changecount = changecount + 1 #tracking label changes in each iteration
		print 'iteration:',itr,changecount
		itr+=1
		if prev_count == changecount:
			quit_count+=1
			print 'quit ',quit_count
		else:
			quit_count = 1
		prev_count = changecount
		if quit_count == 5: #saturation threshold
			break

	#plotting clustered data
	cluster = dict()
	for l in range(len(labels)):
		cluster.setdefault(labels[l],[]).append(coords[l])
	colors = ['ro','bs','g^']
	i = 0
	fig, ax = plt.subplots()
	clusters = []
	output = open('data.pkl','wb')
	for key,value in cluster.iteritems():
		clusters.append(value)
		p,q = zip(*value)
		plt.plot(p, q, colors[i])
		for X, Y in zip(p,q):
			ax.annotate('{}'.format(key), fontsize = 6, fontstyle = 'oblique', xy=(X,Y),ha='right',textcoords='offset points')
		i = i+1
	pickle.dump(clusters,output)
	output.close()
	plt.show()
	
	#plotting original data
	'''org_data = dict()
	for l in range(len(labels_org)):
		org_data.setdefault(labels_org[l],[]).append(coords[l])
	colors = ['ro','bs','g^']
	i = 0
	fig1, ax1 = plt.subplots()
	for key,value in org_data.iteritems():
		p,q = zip(*value)
		plt.plot(p, q, colors[i])
		for X, Y in zip(p,q):
			ax1.annotate('{}'.format(key), fontsize = 6, fontstyle = 'oblique', xy=(X,Y),ha='right',textcoords='offset points')
		i = i+1
	plt.show()'''
		
def findMajorityLabel(pos):
	global labels
	labellist = []
	countnew,countsq = dict(),dict()
	for q in range(len(pos)):
		labellist.append(labels[pos[q]])
	countlist = Counter(labellist)
	for key,value in countlist.iteritems():
		countsq.update({key:value**2})
	total = sum(countsq.itervalues())
	for key,value in countsq.iteritems():
		countnew.update({key:(round((float(value)/total),3)*1000)})
	prob = random.randint(1,1000) #random float
	value_sum = 0
	for key,value in countnew.iteritems():
		value_sum =  value_sum + value
		if prob <= value_sum:
			return key	

	

if __name__== "__main__":
	main()
