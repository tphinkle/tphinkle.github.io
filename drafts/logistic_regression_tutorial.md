---
layout: post
title: Data science monthly write-up--Kaggle digit recognition competition--Part 2
category: data science
comments: True
---

#Logistic regression

This post originally started out as a write-up of my attempt at solving the Kaggle MNIST digit recognizer challenge using soft-max regression (you can find my other attempt in a blog post [here](https://tphinkle.github.io/MNIST-Digit-Recognizer/)). While writing it up, I wasn't sure about how much detail I wanted to go into. It sort of started turning into a full-blown logistic regression tutorial, so I decided to split it up and give it its own blog post.

###Logistic regression
Suppose we're given the digit data, but with only 0's and 1's. How do we teach the computer to classify one of the digits? I can think of an easy way: count the number of loops in the character! Here's the solution in pseudo-code:

~~~~~~~ python
loops = count_loops(test_digit)
if loops == 1:
	test_digit.classification = 0
else:
	test_digit.classification = 1
~~~~~~~

This method is actually pretty good, but there's a problem. Looking at the data set it appears that there are some zeros that violate our little law:

![a zero-loop zero](https://tphinkle.github.io/images/2015-12-27/zero_bw_0.png)
![a two-loop zero](https://tphinkle.github.io/images/2015-12-27/zero_bw_1.png)


We could also imagine some cases where the test digit looks practically like a 1 save for some small connection that creates a loop, and thus registers as a 0 to our algorithm.

So, while a good indicator of classification, it's not perfect. The next natural step to improve our classification method is to introduce another "feature" that might separate 1's from 0's. Character width seems like a meaningful feature; 1's tend to be skinny while 0's are a little fatter. As before, we could come up with some simple algorithm for classifying characters:

~~~~~~~~ python
width = measure_width(test_digit)
if width > width_threshold:
	test_digit.classification = 0
else:
	test_digit.classification = 1
~~~~~~~~

Just like last time, most of the digits would fall in line and classify correctly with this algorithm, but others don't:

![a fat one](https://tphinkle.github.io/images/2015-12-27/one_bw_0.png)

So it looks like there is no single feature that always separates 1's from 0's, but rather some features we believe correlate to varying degrees with a character's classification. For example, we're almost certain that if a digit has one loop and is fat, it's a 0. But what about a fat digit without any loops? How do we predict whether the digit is a 0 or a 1, and can we quantify the degree of certainty we have in our prediction? This is the essence of logistic regression: given a set of measured features we can calculate the probability that the object with those features has one classification or another. Along the way, the logistic regression algorithm will also reveal which features are most meaningful in making classification predictions. For example, the digit's height would not be a very meaningful feature since all digits have around the same height. If we used height as an input feature, logistic regression would give it less weight than other, more meaningful features.





