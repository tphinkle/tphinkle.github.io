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

<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/mnist_0.png" alt="MNIST zero" style="width:300px;" align="middle">
<img src="https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/hw_0.png" alt="Hand-written zero" style="width:300px;" align="middle">


### 1. Model training

Those that have used sklearn before will be familiar with this part. For those that aren't, training a model is as simple as creating a blank model `model` object, and then fitting the model to the training data using `model.fit(data)`.

Here's the code snippet to load in the entire MNIST data set and train it using a logistic regression model. I set `C=1e10` as an optional argument in the logistic regression constructor so that the model would be unregularized (perhaps a topic for another blog post).



### 3. Image processing

Now that we've seen what the raw image we're working with looks like, it's clear we'll have to process it in some way so that it more closely resembles the MNIST data. At the very least, we'll have to rescale it to the size of the MNIST digits since the model will expect that many features. The image processing will be conducted in a number of steps, and at each step I'll show a picture of the transformed image, a histogram of the pixel intensity in the transformed image, show a snippet of code containing the Python function used to perform that processing step, and finally explain my reasoning behind why that step was taken.

##### i. The raw image

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_i.png)

Couple things to point out. First, for whatever reason by default the image is rotated when loaded in via `numpy`. Second, while the image is actually RGB colored, you can see that it's primarily black and white. The histogram doesn't give us a ton of info here across the different color channels, aside from telling us that it's approximately 50-50 black/white. Interestingly, the most prominent picture in the image is *green*, whereas one would expect it to be red and blue due to the purple represented in the digits.

To load the image, I snapped the .jpg picture, downloaded it on my computer, and used a convenient function contained in the `matplotlib.pyplot` module. This loads the image in as a `numpy` array.

```
import matplotlib.pyplot as plt
raw_image_file_path = './custom_digits.jpg`
raw_image = plt.imread(raw_image_file_path)
```

##### ii. Convert to grayscale

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_ii.png)


This is a simple grayscale conversion created by averaging the intensity across RGB channels, necessary since the MNIST set is grayscale valued. We use the `np.mean()` function to do this.

```
import numpy as np
processed_image = np.mean(raw_image, axis=2)
```

##### iii. Rotation

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_iii.png)

Since the camera was loaded in turned at an angle, we have to rotate it by $90^{\circ}$. I didn't take the image with much care, so we can see that the picture itself isn't even aligned with the $x,y$ axes of the figure. In principle I could perform an additional rotation so the digits are perfectly vertically and horizontally aligned, but I think this should do a good enough job for now.

```
processed_image = np.rot90(processed_image, k=-1)
```

##### iv. Crop out the background

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_iv.png)

Next we have to get rid of all that background. This could be done in an eloquent way, but for now I'm achieving the cropping step by manually slicing the `numpy` array.

```
x0 = 100
x1 = 2180
y0 = 850
y1 = 3510
processed_image = processed_image[y0:y1,x0:x1]
```

##### v. Invert the grayscale values

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_v.png)

As we can see, in the MNIST set the digits themselves are whitish colors, while the background is pitch black. To adapt our image to this representation, we simply invert the grayscale values. This is easily achieved in `numpy`.

```
processed_image = 255 - processed_image
```

##### vi. Threshold the grayscale values



After inversion we're starting to get an image that more closely resembles the MNIST set, but we can see that the background in the inverted image isn't perfectly black. In order to make it so, we need to threshold the pixel intensities, basically by setting all pixels with intensity below the threshold value equal to zero (perfectly black). But, how do we choose the threshold? This is probably the first instance where the histogram is actually useful beyond just being informative. We can see two subpopulations in the histogram, a huge clustering of pixels at low intensity that corresponds to the background, and a much smaller sub population at higher intensities that corresponds to the letters. The goal is to move that entire mass of dark pixels to zero intensity. There are ways of being more exact about this, but I'm just going to do it by eyeballing the histogram in the previous step and setting the threshold based off of the gap between the populations of dark and light pixels. In this case, I went with 120.



Here's the code. Notice how easy this operation is in `numpy`.

```
threshold = 120
processed_image[processed_image < threshold] = 0.
```

Note: In the following histogram I neglect to include black pixels from now on, since they dominate the pixel intensities at this point and make it difficult to see the high-intensity pixel bins.

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_vi.png)

##### vii. Isolate the digits

So far the image processing steps have taken us to a point where the individual digits begin to look more and more like the MNIST digits, but we still need to isolate individuals. How do we do this? The method I use is a variation of the [flood fill algorithm](https://en.wikipedia.org/wiki/Flood_fill). You know that paint bucket tool that's in virtually every image manipulation software program? That thing uses flood fill. Basically, we are looking for non-black pixels, and every time two of these pixels touch sides, we group them together. We recursively add neighboring pixels into the cluster, until eventually we've scanned over the entire image. After flood fill, we have a list of clusters, where each cluster itself is a list of the indices of the pixels that belong to that cluster. Then, for each cluster I create a new numpy array for that cluster. All of the pixels in this array are black, except for the pixels that were included in that particular cluster which retain their intensity value.

To show how this works, I'm including a transformed version of the original image where cluster is assigned a random color. This demonstrates how neighboring pixels are indeed clustered correctly.

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_color.png)

The picture above indicates that the clusters were properly detected, and the following image shows the transformation that is performed on each cluster.

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/single_digit.png)

Now we're at the single digit level, and for the rest of the tutorial we'll be performing transformations on the individual images instead of the entire bulk image as we have up to this point.

As for the coding part, I'm 99% sure that somewhere out there in Python's scientific computing space there's a single-call flood fill function, but I've yet to find it. It's probably in `numpy`, `scipy`, `opencv2`, or maybe even in `matplotlib`. A quick google search didn't find it for me, so I just decided to implement it myself. It's not so tricky, but it's a recursive algorithm so you have to be a little careful to avoid having your code blow up ;) 

```
# List of clusters
# Each cluster is a list of pixel indices that belongs to that cluster
clusters = FloodFill(processed_image)

# Turn the clusters of pixels into single digit images
digits = []
for cluster in clusters:

    # Create an empty numpy array that is as tall and wide as
    # the span of the pixels in this particular cluster
    digit = np.empty((np.max(cluster[:,0]), np.max(cluster[:,1])))

   

    # Set the intensity value of the pixels in the digit
    # to the intensity value of the pixels in the cluster.
    
    row_offset = np.min(cluster[:,0])
    column_offset = np.min(cluster[:,1])

    for pixel in cluster:
        digit[pixel[0] - row_offset, pixel[1] - column_offset] = processed_image[pixel[0], pixel[1]]
    
    digits.append(digit)
```

##### viii. Threshold digits based on pixel count

This step could have been performed in the previous step, but I decided to break it up. The general image processing pipeline we've gone through so far generally works, but on occasion you'll have errant small clusters that get picked up and recognized as digits. In this case, I had commas and periods on the page that have been put into clusters that I don't want to make predictions on. This filtering step may be complex depending on the 'noise', or undesired objects, in your own personal images. In this case, we filter out the undesired characters by simply applying a filter on the minimum number of pixels that a digit must have.

How do we choose the threshold? One easy way is to plot a histogram of the pixel counts of all the digits. There should be a large population with lots of pixels---those are the digits. On the other hand, 


##### viii. Pad the digits

Next, we see that the light pixels run all the way up to the border of the image, whereas in the MNIST set this never happens; usually there's a border of a few black pixels at least surrounding every image. What we have to do is 'pad' our digits, basically adding some amount of black space around them. Now, the * amount * of padding matters. I inserted random pads until I found something that qualitatively matched the appearance of the MNIST digits.

![Hand-written zero](https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/digits_viii.png)

Now for the code... Guess what? There's a `numpy` function that will do this for us in a single line of code! Who would have thought? Simply amazing. Anyways, here's the code!





### 4. Testing the model!

Now that we've trained our model and preprocessed hte images, let's feed them into our model!

