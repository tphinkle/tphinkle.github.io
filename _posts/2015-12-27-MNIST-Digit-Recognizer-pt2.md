---
layout: post
title: Data science monthly write-up--Kaggle digit recognition competition--Part 2
category: data science
comments: True
---

##Part 2: Soft-max regression

As the introduction to this blog post stated, soft-max regression is a generalization of logistic regression, which begs the question of what logistic regression is. A quick explanation of logistic regression seems like a good starting point for this post, so here goes. I'll try to explain things in a general way and using the digit recognizer as a concrete example in parallel.

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

!(https://tphinkle.github.io/images/2015-12-27/zero_bw_0.png)[a zero-loop zero]
!(https://tphinkle.github.io/images/2015-12-27/zero_bw_1.png)[a two-loop zero]


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

!(https://tphinkle.github.io/images/2015-12-27/one_bw_0.png)[a fat one]

So it looks like there is no single feature that always separates 1's from 0's, but rather some features we believe correlate to varying degrees with a character's classification. For example, we're *pretty sure* that if a digit has one loop and is fat, it's a 0. But what about a fat digit without any loops? How do we predict whether the digit is a 0 or a 1, and can we quantify the degree of certainty we have in our prediction? This is the essence of logistic regression: given a set of measured features we can calculate the probability that the object with those features has one classification or another. Along the way, the logistic regression algorithm will also reveal which features are most meaningful in making classification predictions.





