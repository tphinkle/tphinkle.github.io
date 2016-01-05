---
layout: post
title: Data science monthly write-up--Kaggle digit recognition competition
use_math: true
---

#Introduction
In this post I'll write about my attempt at the [digit recognition Kaggle competition](https://www.kaggle.com). The goal is to accurately recognize single hand-written digits, which are provided as two-dimensional grayscale images. Each pixel element is an integer value in the range (0, 255).

Here's a two from that data set:

![a two](https://tphinkle.github.io/images/2015-12-27/two_gs_0.png)

To solve the challenge, I tried two different approaches. The first approach uses an algorithm called [dynamic time warping](https://en.wikipedia.org/wiki/Dynamic_time_warping) (DTW) and the second uses [soft-max regression](http://ufldl.stanford.edu/tutorial/supervised/SoftmaxRegression/), a generalization of logistic regression to allow for more than two classifications. In this post, I'll do my best to explain how each method works and describe how successful my implementations of each were in recognizing digits.

[Part 1: Dynamic time warping](https://tphinkle.github.io/)

##Part 1: Dynamic time warping

Dynamic time warping is an algorithm used to quantify how similar two signals are. The method is usually used to compare time-series data, and in fact, was developed in the 70's primarily for the purpose of speech recognition. The data doesn't have to be a time-series, though; actually, all that is required is that we are able to represent our data in some way as x-y data. For brevity and for historical reasons, I'll refer to the x-y representation of the data as a time series, even though it is not what we would traditionally view as a time-series.

Right now you may be scratching your head--how do we get a time-series out of our data type, a grayscale image with pixel values? First, I converted the grayscale representation of each character to a black/white representation; the digit still retains its identity as a black and white image. To create a time-series of the image, I "walked" around the digit, following its perimeter. By recording the row and column of our position in the matrix at each step in the walk, we get two different time series.

Here's what the representation change looks like:

![Digit representation change](https://tphinkle.github.io/images/2015-12-27/representation_transformation.png)

Remember, each character matrix is actually transformed into two time-series, one for the row values along the path and the other for the columns. Now that we have the representation transformation down, we need to quantitatively calculate the 'difference' between different characters' time series. 

The simplest way to quantify the difference between two time-series is via a simple time-aligned Euclidean distance metric. Simply put, we take the two time-series, align them on the time-axis, and sum the distance between every pair of aligned points in the data set.

$$
	\text{distance} = a + b
$$

Is this working?


$a+b=c$


LATEX:     distance = sum(all i) (ai-bi)

update3

 The more similar the two time series are, the lower their cumulative difference is. The following image shows a visualization of this difference. 

![No-warping Euclidean distance metric](https://tphinkle.github.io/images/2015-12-27/nowarp_distance_0.png)

Looking at the time-series representations of the two fives, we can see that they are similar, but not quite aligned in the time-axis. For example, a much better fit could be achieved if only we were allowed to just slightly shift the bottom most data points in the lower time-series to the left. DTW is an algorithm that allows for this type of 'warping' of hte time axis so as to minimize the cumulative distance between two time series.

The key behind dynamic time warping is to construct a matrix of the distance between *all* pairs of data points between the two time series. 

LATEX:     matrix_i,j = ai-bj for all i all j

Then, the proper time-warping alluded to above is given by the path for which the cumulative distance along that path is minimized. We call the cumulative distance along any particular path the *cost* of that path.

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

