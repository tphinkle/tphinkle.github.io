---
layout: post
title: Data science monthly write-up--Kaggle digit recognition competition
---

#Introduction
In this post I'll write about my attempt at the [digit recognition Kaggle competition](https://www.kaggle.com), using machine learning to recognize different digitalized hand written numbers. The goal is to accurately recognize hand-written digits, which have been digitally rendered as two-dimensional gray scale matrices. 

Here's a matrix-representation of one of the elemenets in the data set provided:

![a two](https://tphinkle.github.io/images/2015-12-27/two_gs_0.png)


This was my first foray into solving a data-sciency problem on my own (i.e., not as part of a class), so I didn't expect a great score starting out. In fact, the two methods I employed probably aren't the best for the job, and I didn't want to use any pre-existing packages. Of course, there are packages out there that could probably score me a 99% on the recognition test in just a few lines of my own code, but that's not the point. 

To solve the challenge, I tried two different solutions. The first solution uses an algorithm called [dynamic time warping](https://en.wikipedia.org/wiki/Dynamic_time_warping) and the second solution uses [soft-max regression](http://ufldl.stanford.edu/tutorial/supervised/SoftmaxRegression/), a generalization of logistic regression to allow for more than two classifications. I'll do my best to explain how each method works, summarize the code that I wrote to run the method, and finally discuss the results of each method.

[Part 1](https://tphinkle.github.io/)

##Part 1: Dynamic time warping

Dynamic time warping is an algorithm used to determine how similar two data sets are. The method is usually used to compare time-series data, and in fact, was developed in the 70's primarily for the purpose of speech recognition. The data doesn't have to be a time-series, though; actually, all that is required is that we are able to represent each data set as x-y data, or a set of pairs of data points. The x-coordinate should be viewed as the time dimension, and in this tutorial I will refer to the x-y representation as a time-series representation.

There is more than one way to convert the character's matrix representation to an x-y representation. First, I converted the grayscale representation of each character to a black/white representation. To convert to the x-y representation, I chose to find the lowest-left most point in the matrix, and "walk" around the character. Each step in the walk produces two data sets, with the x-values in both sets corresponding to that step in the walk, and the y-values the row and column of that particular data step.

Here's what the representation change looks like:

![Digit representation change](https://tphinkle.github.io/images/2015-12-27/representation_transformation.png)

Remember, each character matrix is actually converted to two x-y datasets, one for the row values along the path and the other for the columns. Now that we have the representation transformation down, we need to quantitatively calculate the 'difference' between different characters. This is where DTW comes in.

The simplest way to quantify the difference between two time-series is via a simple Euclidean distance metric. Basically, we take the two time-series, align them on the x-axis, and sum the differences between every two pairs of points in the data set. The following image shows a visualization of the difference. 

![No-warping Euclidean distance metric](https://tphinkle.github.io/images/2015-12-27/nowarp_distance_0.png)

Looking at the time-series representations of the two fives, we can see that they are similar. The Euclidean distance metric in the absence of warping however inflates the difference between the two series, however. For example, look at the bottom most interval of each plot. The two are similar, but because of a small phase-shift along the time axis, the distance at that interval is exaggerated. We would like to apply some transformation to the data that allows the time-axis to be more fluid, allowing for reasonable warping so that the best matching is determined between pairs. This is where dynamic time warping comes in.

The key behind dynamic time warping is to construct a matrix of the distance between all pairs of data points between the two time series. Then, the proper time-warping alluded to above is given by the path for which the cumulative distance along that path is minimized. We call the cumulative distance along any particular path the *cost* of that path.

Here's what the distance-matrix looks like for the two fives from above:

![Distance matrix](https://tphinkle.github.io/images/2015-12-27/distance_matrix_0.png)

There are a few requirements that the minimal cost path must satisfy. They are:

1. The beginning and end points of both series must match up. This means the past must path through the upper-left and lower-right corners of the above matrix. If the two time-series have m and n data points respectively, the path must pass through the points (0,0) and (m,n).
2. The path through the matrix must monotonically progress towards the end-point, i.e., if (i,j) is a point along the path, the subsequent step cannot be any of (i-1,j), (i,j-1), or (i-1,j-1).

We now know the purpose of the time warping and the requirements that the minimum cost path must satisfy, so how do we actually find that minimum path? As the name of the algorithm suggests, we solve for the minimum cost path *dynamically*. The key is this: the minimum cost path between points (0,0) and (i,j) must pass through (i-1,j), (i-1,j-1), or (i,j-1) (property 2 above). This means we can iteratively calculate the desired cost path at (m, n) by starting at (0, 0) and calculating the cost paths for (1,0), (0,1), (1,1), (2,1), ..., (m, n). 

Here's the algorithm for calculating the cost of the minimum cost path to (i, j):
```
for all (i,j) in mxn:


cost_{i,j} = distance(i, j) + minimum(cost_{i-1,j}, cost_{i-1, j-1}, cost_{i, j-1})
```

The "distance" then between the two time-series is given by cost_{m,n}. 

Finally, we can determine the mapping itself (the path through the distance and cost matrices) by starting at the end point (m,n) and 'descending' to (0,0) by stepping to the matrix element with the lowest cost. Below we have the distance matrix, cost matrix, and plots of the two time-series showing the warping that the algorithm has provided. Note the difference between the non-warping and warping plots.

![Full DTW solution](https://tphinkle.github.io/images/2015-12-27/all_plots.png)

The above algorithm described how to calculate the difference between two digits. The kaggle competition asked for us to determine which digit a digit was from the test set. To do this, I calculated the sum of the DTW distances between the given test digit and a set of k training samples for each digit. The determined character then is the minimum of those DTW distances.

Here are the results of the algorithm:

By the way, the above approach was the simplest application of DTW. Other flavors of DTW exist including Derivative DTW (DDTW) and Weighted DTW (WDTW). If you're interested in learning more about DTW, I suggest visiting [Keough's page](http://www.cs.ucr.edu/~eamonn/), who has done a lot of work on refining the method. In particular, I found [this paper](https://www.cs.rutgers.edu/~mlittman/courses/lightai03/DDTW-2001.pdf) helpful.







   






##Soft-max regression (~logistic regression)

