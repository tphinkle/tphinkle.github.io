---
layout: post
title: Data science monthly write-up--MNIST digit recognition Kaggle competition
---

#Introduction
In this post I'll write about my attempt at the [digit recognition Kaggle competition](https://www.kaggle.com), using machine learning to recognize different digitalized hand written numbers. The goal is to accurately recognize hand-written digits, which have been digitally rendered as two-dimensional gray scale matrices. 

Here's a two:

![a two](https://github.com/tphinkle/tphinkle.github.io/blob/master/images/2015-27-12/two_gs_0.png)


This was my first foray into solving a data-sciency problem on my own (i.e., not as part of a class), so I didn't expect a great score starting out. In fact, the two methods I employed probably aren't the best for the job, and I didn't want to use any pre-existing packages. Of course, there are packages out there that could probably score me a 99% on the recognition test in just a few lines of my own code, but that's not the point. 

To solve the challenge, I tried two different solutions. The first solution uses an algorithm called [dynamic time warping](https://en.wikipedia.org/wiki/Dynamic_time_warping) and the second solution uses [soft-max regression](http://ufldl.stanford.edu/tutorial/supervised/SoftmaxRegression/), a generalization of logistic regression to allow for multiple classifications. I'll do my best to explain how each method works, summarize the code that I wrote to run the method, and finally discuss the results of each method.

#Dynamic time warping

Dynamic time warping is an algorithm used to determine how similar two data sets are. The method is usually used to compare time-series data, and in fact, was developed in the 70's primarily for the purpose of speech recognition. The data doesn't have to be a time-series, though; actually, all that is required is that we are able to represent each data set as x-y data, or a set of pairs of data points. The x-coordinate should be viewed as the time dimension.

There is more than one way to convert the character's matrix representation to an x-y representation. I chose to find the lowest-left most point in the matrix, and "walk" around the character. Each step in the walk produces two data sets, with the x-values in both sets corresponding to that step in the walk, and the y-values the row and column of that particular data step.

Here's what that transformation looks like:




#Soft-max regression (~logistic regression)

