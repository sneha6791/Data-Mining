#!/usr/bin/env python

import sys
import string
import math

count = 0 #number of classes of each label
ind_count = 0 #number of class labels for each value of an attribute
t_count = 0 #total number of class labels
old_key = None 
old_key1 = None
old_key2 = None 
final = 0.0
entropy = 0.0
l1 = [] #list of counts of class occurrences
l2 = [] #list of entropies for each value of an attribute
l3 = [] #list of entropies of each attribute
l4 = [] #list of attribute labels
l5 = [] #sorted output from mapper


for item in sys.stdin:
	l5.append(item)
l5.sort()
for line in l5:
	(key2,key1,key,val) = line.split('\t',3)
	if old_key2 == '-1': 
		t_count = t_count + 1
	if old_key2 != key2:
		if old_key2:
			l1.append(count)
			weight = float(ind_count) / t_count
			for item in l1:
				e = (float(item)/ind_count)
				v = e*float(math.log(e))/math.log(2.0)
				l2.append(v)
			ans = sum(l2)
			temp = -1.0 * ans * weight 
			final = final + temp
			l4.append(old_key2)
			l3.append(final)
		final = 0.0
		l2 = []
		l1 = []
		count = 0
		ind_count = 0
		old_key1 = None
	old_key2 = key2
	try:
		if old_key1 != key1:
			if old_key1:
				l1.append(count)
				weight = float(ind_count) / t_count
				for item in l1:
					e = (float(item)/ind_count)
					v = e*float(math.log(e))/math.log(2.0)
					l2.append(v)
				ans = sum(l2)		
				temp = -1.0 * ans * weight 
				final = final + temp
			l2 = []
			l1 = []
			count = 0
			ind_count = 0
			old_key = None
		old_key1 = key1
		try:
			if old_key != key:
				if old_key:
					l1.append(count)
				count = 0
			old_key = key
	
			try:
				count = count + int(val)
			except:
				continue
			ind_count = ind_count + 1
		except:
			continue
	except:
		continue

l1.append(count)
weight = float(ind_count) / t_count
for item in l1:
	e = (float(item)/ind_count)
	v = e*float(math.log(e))/math.log(2.0)
	l2.append(v)
ans =sum(l2)
temp = -1.0 * ans * weight 
final = final + temp
l3.append(final)
l4.append(old_key2)
initial = float(l3[0])
print 'entropy of initial dataset',l3[0]
print 'attribute','\t','\t','information gain'
for i in range(0,len(l3)):
	l3[i] = initial - float(l3[i])
	if i!= 0:
		print l4[i],'\t','\t',l3[i]
maxgain = max(l3)
for j in range(0,len(l3)):
	if l3[j] == maxgain:
		print '\nSplitting Attribute:', l4[j], 'With the maximum information gain:', maxgain
		break
