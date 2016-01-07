---
layout: post
title: Data science monthly write-up--Kaggle digit recognition competition
category: data science
---

#Introduction
In this post I'll write about my attempt at the [digit recognition Kaggle competition](https://www.kaggle.com). The goal is to accurately recognize single hand-written digits, which are provided as two-dimensional grayscale images. Each pixel element is an integer value in the range (0, 255).

Here's a two from that data set:

![a two](https://tphinkle.github.io/images/2015-12-27/two_gs_0.png)

To solve the challenge, I tried two different approaches. The first approach uses an algorithm called [dynamic time warping](https://en.wikipedia.org/wiki/Dynamic_time_warping) (DTW) and the second uses [soft-max regression](http://ufldl.stanford.edu/tutorial/supervised/SoftmaxRegression/), a generalization of logistic regression to allow for more than two classifications. In this post, I'll do my best to explain how each method works and describe how successful each of my implementations was in recognizing digits.

[Part 1: Dynamic time warping](https://tphinkle.github.io/MNIST-Digit-Recognizer-pt1)
[Part 2: Softmax regression](https://tphinkle.github.io/MNIST-Digit-Recognizer-pt2)