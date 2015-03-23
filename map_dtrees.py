#!/usr/bin/env python

import sys
import string
for line in sys.stdin:
	line = line.strip()
	words = line.split(',')
	# to calculate the initial entropy of the dataset
	print '%s\t%s\t%s\t%s' % (-1,-1,words[10],1)
	# -1,-1 distinguishes the class attribute from the rest of attributes
	for i in range(0,5):
                # to calculate the entropies of each non-class attribute
                # (attribute index, attribute name, class label, count)
		j = 2*i
		k = 2*i + 1
		if words[j] == '1':
			print "%s\t%s\t%s\t%s" % (j+1,'s=1',words[10],1) 
		if words[j] == '2':
			print "%s\t%s\t%s\t%s" % (j+1,'s=2',words[10],1)
		if words[j] == '3':
			print "%s\t%s\t%s\t%s" % (j+1,'s=3',words[10],1)
		if words[j] == '4':
			print "%s\t%s\t%s\t%s" % (j+1,'s=4',words[10],1)
		if words[k] == '1':
			print "%s\t%s\t%s\t%s" % (k+1,'c=1',words[10],1)
		if words[k] == '2':
			print "%s\t%s\t%s\t%s" % (k+1,'c=2',words[10],1)	
		if words[k] == '3':
			print "%s\t%s\t%s\t%s" % (k+1,'c=3',words[10],1)
		if words[k] == '4':
			print "%s\t%s\t%s\t%s" % (k+1,'c=4',words[10],1)
		if words[k] == '5':
			print "%s\t%s\t%s\t%s" % (k+1,'c=5',words[10],1)
		if words[k] == '6':
			print "%s\t%s\t%s\t%s" % (k+1,'c=6',words[10],1)	
		if words[k] == '7':
			print "%s\t%s\t%s\t%s" % (k+1,'c=7',words[10],1)
		if words[k] == '8':
			print "%s\t%s\t%s\t%s" % (k+1,'c=8',words[10],1)
		if words[k] == '9':
			print "%s\t%s\t%s\t%s" % (k+1,'c=9',words[10],1)
		if words[k] == '10':
			print "%s\t%s\t%s\t%s" % (k+1,'c=10',words[10],1)	
		if words[k] == '11':
			print "%s\t%s\t%s\t%s" % (k+1,'c=11',words[10],1)
		if words[k] == '12':
			print "%s\t%s\t%s\t%s" % (k+1,'c=12',words[10],1)
		if words[k] == '13':
			print "%s\t%s\t%s\t%s" % (k+1,'c=13',words[10],1)
	
		
