# Data-Mining
Contains programs related to small projects in Data Mining- modeling decision trees, implementing clustering on sample data, etc.
1. map_dtrees and reduce_dtrees builds a decision tree out of a training set of attributes and selects the attribute with the higest information gain; each attribute is iteratively chosen as the best test candidate along the path of the tree based on entropy values.
2. clustering_probsq is a naive approach to forming clusters of data points by initially assigning random labels to each point and then grouping points on successive iterations based on the probability of membership. Such a probability is calculated based on the labels of k nearest neighbors of a point.  
