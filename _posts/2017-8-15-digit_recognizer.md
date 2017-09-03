# Detecting *real* hand-written digits with machine learning

One of the first applications a novice machine learning student will encounter is the digit recognizer. It's a really cool application, and a good demonstration of how machine learning can have real world applications. I think the visual aspect really strikes a chord with people too; a lot of machine learning examples are about making abstract predictions that have little tangible meaning, but in this case the results are clearly visible. However cool the digit recognizer example is, one thing that could be improved is showing its real world implications. In the digit recognizer problem we build a model that *can* detect hand-written digits, but this idea is never realized with actual hand-written digits. Here's an example of a digit from the MNIST data set plotted as a grayscale matrix. For this particular data set, digits are represented as 28x28 single-byte grayscale values. The trouble is that they don't really resemble hand-written digits. Is there a way that we can use the models trained on MNIST data to accurately predict hand-written digits? It turns out that there is, and with only a little bit of image processing we can create a program that will detect our own hand-written digits, accurately and consistently.



I'll include the code, but here's the gist of it; it's really not all that complicated:

1. Train a logistic regression model on the MNIST data set using sklearn
2. Draw and import our own hand-written digits
3. Put the digits through a sufficiently general image processing pipeline that makes our digits more closely resemble digits from the MNIST set
4. Use our trained model to make predictions on the hand-written digits

##### 1. Model training

Those that have used sklearn before will be familiar with this part. For those that aren't, training a model is as simple as creating a blank model `model`, and then fittin the model to the training data using `model.fit(data)`.

Here's the code snippet to load in the entire MNIST data set and train it using a logistic regression model. I set `C=1e10` as an optional argument in the logistic regression constructor so that the model would be unregularized (perhaps a topic for another blog post).

##### 2. Generating and loading hand-written digits

For this part, I drew a random collection of digits using a pen on a clean sheet of white paper, snapped a photo with my cell phone's camera, and e-mailed myself the pictures. Easy peasy.

Here's the image that we'll be working with. The goal is to detect all of these digits.

##### 3. Image preprocessing

This is undeniably the most difficult and time-consuming part of the entire pipeline (although it isn't so bad with all of the convenient image processing functoins available in Python's scientific computing modules). This is actually a common thread that runs through a lot of machine learning problems: training and fitting models is seldom the most time-consuming and critical part of the entire analysis pipeline, even if it gets most of the attention. We'll start with the raw image shown above and I'll go through the preprocessing steps one-by-one, explaining each step and justifying my reasoning for why that step was performed.

##### 4. Testing the model!

Now that we've trained our model and preprocessed hte images, let's feed them into our model!

