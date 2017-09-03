# Detecting *real* hand-written digits with machine learning

One of the first applications a novice machine learning student will encounter is the digit recognizer. It's a really cool application, and a good demonstration of how machine learning can have real world applications. I think the visual aspect really strikes a chord with people too; a lot of machine learning examples are about making abstract predictions that have little tangible meaning, but in this case the results are clearly visible. However cool the digit recognizer example is, one thing that could be improved is showing its real world implications. In the digit recognizer problem we build a model that *can* detect hand-written digits, but this idea is never realized with actual hand-written digits. Here's an example of a digit from the MNIST data set plotted as a grayscale matrix. For this particular data set, digits are represented as 28x28 single-byte grayscale values. The trouble is that they don't really resemble hand-written digits.

Is there a way that we can use the models trained on MNIST data to accurately predict hand-written digits? It turns out that there is, and with only a little bit of image processing we can create a program that will detect our own hand-written digits, accurately and consistently.



I'll include the code, but here's the gist of it; it's really not all that complicated:

1. Train a logistic regression model on the MNIST data set using sklearn
2. Draw and import our own hand-written digits
3. Put the digits through a sufficiently general image processing pipeline that makes our digits more closely resemble digits from the MNIST set
4. Use our trained model to make predictions on the hand-written digits

### 0. The data set

Here's a picture of the raw image I'll be using. It's not a particular good picture, I quickly wrote down some digits using a marker I had lying around on a white sheet of paper, and snapped a quick overhead shot of the paper with my camera.

<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/custom_digits_2.jpg" alt="Hand-written digits" style="width:800px;" align="middle">

Here are two examples of single digits, on the left from the MNIST set and on the right, one of the zoomed in digits from the above picture. The goal is to make use of the thousands of the digits in the MNIST set to train a model to predict digits that start off looking like the hand-written digit on the right.

<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/MNIST_0.png" alt="MNIST zero" style="width:300px;" align="middle">
<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/hw_0.png" alt="Hand-written zero" style="width:300px;" align="middle">


### 1. Model training

Those that have used sklearn before will be familiar with this part. For those that aren't, training a model is as simple as creating a blank model `model` object, and then fitting the model to the training data using `model.fit(data)`.

Here's the code snippet to load in the entire MNIST data set and train it using a logistic regression model. I set `C=1e10` as an optional argument in the logistic regression constructor so that the model would be unregularized (perhaps a topic for another blog post).



### 3. Image processing

Now that we've seen what the raw image we're working with looks like, it's clear we'll have to process it in some way so that it more closely resembles the MNIST data. At the very least, we'll have to rescale it to the size of the MNIST digits since the model will expect that many features. The image processing will be conducted in a number of steps, and at each step I'll show a picture of the transformed image, a histogram of the pixel intensity in the transformed image, show a snippet of code containing the Python function used to perform that processing step, and finally explain my reasoning behind why that step was taken.

##### i. The raw image

<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_i.png" alt="Hand-written zero" style="width:300px;" align="middle">

Couple things to point out. First, for whatever reason by default the image is rotated when loaded in via `numpy`. Second, while the image is actually RGB colored, you can see that it's primarily black and white. The histogram doesn't give us a ton of info here across the different color channels, aside from telling us that it's approximately 50-50 black/white. Interestingly, the most prominent picture in the image is *green*, whereas one would expect it to be red and blue due to the purple represented in the digits.

To load the image, I snapped the .jpg picture, downloaded it on my computer, and used a convenient function contained in the `matplotlib.pyplot` module:

```
import matplotlib.pyplot as plt
raw_image_file_path = './custom_digits.jpg`
raw_image = plt.imread(raw_image_file_path)
```

##### ii. Black-white conversion

<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_ii.png" alt="Hand-written zero" style="width:300px;" align="middle">






### 4. Testing the model!

Now that we've trained our model and preprocessed hte images, let's feed them into our model!

