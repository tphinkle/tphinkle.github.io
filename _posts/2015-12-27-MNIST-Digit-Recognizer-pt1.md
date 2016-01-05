---
layout: post
title: Data science monthly write-up--Kaggle digit recognition competition--Part 1
category: data science
---

##Part 1: Dynamic time warping

Dynamic time warping is an algorithm used to quantify how similar two signals are. The method is usually used to compare time-series data, and in fact, was developed in the 70's primarily for the purpose of speech recognition. The data doesn't have to be a time-series, though; actually, all that is required is that we are able to represent our data in some way as x-y data. For brevity and for historical reasons, I'll refer to the x-y representation of the data as a time series, even though it is not what we would traditionally view as a time-series.

Right now you may be scratching your head--how do we get a time-series out of our data type, a grayscale image with pixel values? There are any number of ways one could think about transforming the data, but this is how I did it. First, I converted the grayscale representation of each character to a black/white representation; the digits are still identifiable as black and white images. To create a time-series of the image, I "walked" around the digit, following its perimeter. By recording the row and column of our position in the matrix at each step in the walk, we get two different time series.

Here's what the representation change looks like:

![Digit representation change](https://tphinkle.github.io/images/2015-12-27/representation_transformation.png)

Remember, each character matrix is actually transformed into two time-series, one for the row values along the path and the other for the columns. Now that we have the representation transformation down, we need to quantitatively calculate the 'difference' between different characters' time series. 

The simplest way to quantify the difference between two time-series is via a simple time-aligned Euclidean distance metric. Simply put, we take the two time-series, align them on the time-axis, and sum the distance between every pair of aligned points in the data set.

$$ 
\begin{align*}
	& C = \sum_{i}^{m}\left(y_{1, i}^{2}-y_{2, i}^{2}\right) ^{1/2}
\end{align*}
$$


 The more similar the two time series are, the lower their cumulative difference is. The following image shows a visualization of this difference. 

![No-warping Euclidean distance metric](https://tphinkle.github.io/images/2015-12-27/nowarp_distance_0.png)

Looking at the time-series representations of the two fives, we can see that they are similar, but not quite aligned in the time-axis. For example, a much better fit could be achieved if only we were allowed to just slightly shift the bottom most data points in the lower time-series to the left. DTW is an algorithm that allows for this type of 'warping' of the time axis so as to minimize the cumulative distance between two time series. It also has the advantage that the time-series do not need to have the same number of data points.

We start with DTW by constructing a matrix of the distance between *all* pairs of data points between the two time series. 

$$ 
\begin{align*}
	& D_{i,j} = \left(y_{1, i}^{2}-y_{2, j}^{2}\right)^{1/2}
\end{align*}
$$

Here's what the distance-matrix looks like for the two fives from above:

![Distance matrix](https://tphinkle.github.io/images/2015-12-27/distance_matrix_0.png)

Our goal is to find a path through this matrix that has the lowest cumulative distance; this path corresponds to the time warping that gives the best match between the two time series. The cumulative distance along any particular path is called the *cost* of that path.

There are a few requirements that the minimal cost path must satisfy. They are:

1. The beginning and end points of both series must match up. This means the past must path through the upper-left and lower-right corners of the above matrix. If the two time-series have m and n data points respectively, the path must pass through the points (0,0) and (m-1,n-1).
2. The path through the matrix must monotonically progress towards the end-point, i.e., if (i,j) is a point along the path, the subsequent step cannot be any of (i-1,j), (i,j-1), or (i-1,j-1).
3. Optional constraints:
    -If we don't want to allow any extreme warping to happen (i.e., large time distance between matched data points) we can impose restrictions on where the warping path is allowed to go in the matrix. 
    -Similarly, we can impose a constraint on the maximum number of points a single point can be connected to.


We now know the purpose of the time warping and the requirements that the minimum cost path must satisfy, so how do we actually find that minimum path? As the name of the algorithm suggests, we solve for the minimum cost path *dynamically*. The key is this: the minimum cost path between points (0,0) and (i,j) must pass through (i-1,j), (i-1,j-1), or (i,j-1) (property 2 above). This means we can iteratively calculate the minimum cost to get to (m-1, n-1) by starting at (0, 0) and calculating the minimum costs for (1,0), (0,1), (1,1), (2,1), ..., (m-1, n-1). Note that this does not yield the path itself (we can calculate that after), but it does give us the cost of the optimal warping.

Here's the algorithm for calculating the cost of the minimum cost path to (i, j):

```python
cost_{i,j} = distance(i, j) + minimum(cost_{i-1,j}, cost_{i-1, j-1}, cost_{i, j-1})
```

The measure of how well the two signals match is then given by $cost_{m,n}$. 

Finally, we may want to look at what the optimal warp path actually looks like. The path is found by starting at the end point (m-1, n-1) and 'walking' to (0,0), at each step walking to the adjacent matrix element with the lowest minimum cost. Below we have the distance matrix, cost matrix, and plots of the two time-series showing the warping that the algorithm has provided. Note the difference between the non-warping and warping plots.

![Full DTW solution](https://tphinkle.github.io/images/2015-12-27/all_plots.png)

The above algorithm described how to calculate the difference between two digits. The kaggle competition asked for us to classify unknown digits from a test set. To do this, I calculated the sum of the DTW distances between the given test digit and a set of k training samples for each digit. The test digit is then classified by the k training samples with the lowest total (the best overall fit between all training examples).

Here are the results of the algorithm:

| Test digit          | Correct predictions | Total predictions | Ratio        |
| ------------------- |:-------------------:|:-----------------:|-------------:|
| 0                   |                     |                   |
| 1
| 2
| 3
| 4
| 5
| 6
| 7
| 8
| 9
| total

It took ____ hours to classify the above 100 digits using 100 training examples.

By the way, the above approach was the simplest application of DTW. Other flavors of DTW exist including Derivative DTW (DDTW) and Weighted DTW (WDTW). If you're interested in learning more about DTW, I suggest visiting [Prof. Keough's page](http://www.cs.ucr.edu/~eamonn/), who has done a lot of work on refining the method. In particular, I found [this paper](https://www.cs.rutgers.edu/~mlittman/courses/lightai03/DDTW-2001.pdf) helpful.