
# **Image Clustering Using Convnets Transfer Learning and K-Means++**

### Motivation behind using Convnets Transfer Learning for Image feature Extraction
-  Image Clustering using simple KMeans does'nt yield good results. Simply flattening the image and passing it to KMeans doesn't preseve image features.<br>
-  Instead, Convolutional Neural Networks preserves important characteristics of an image, as its biologically inspired by the architecture that is present in human/animal brains.<br>
-  Convolutional Neural Network layers detects pixels, edges, text, parts, objects in the image, thereby preserving all the important features of an image.

### Transfer Learning

-  Core idea is instead of building a Convolutional Neural Network from scratch to solve our task, what if we can reuse existing trained models like VGG16, AlexNet architectures.
-  Keras actually has VGG16 trained on ImageNet dataset, which is the one of the largest object classification dataset.

## Project Description<br>

-  Input Dataset -> My Google Photos captured on my mobile cam<br>
-  Output -> Cluster of similar Images<br>

### Algorithms used<br>

-  Keras Model of the VGG16 network, trained on Imagenet dataset is used to extract feature vectors of the images.
-  Optimal K for KMeans is determined using Elbow method
-  These feature vectors of images are used to form clusters using KMeans++


### Packages Required

-  Python       <br>Programming language
-  Opencv (cv2) <br>TO read and write the images
-  Numpy        <br>To perform operations on image arrays
-  Keras        <br>To load the pretrained Imagenet model weights and extract image feature vectors
-  Matplotlib   <br>To plot the image clusters as a graph
-  os           <br>To read and write the files from directories

### Results : Similar Images are clustered together

#### Cluster 5
<img src='cluster_5.jpg' alt="Cluster of images formed after code execution" title="5th Cluster" />

#### Cluster 1
<img src='cluster_1.jpg' />

#### Cluster 7

<img src='cluster_7.jpg' alt='7th cluster of images formed' title="7th Cluster"/>

#### Acknowledgement

-  Inspired from https://github.com/elcorto/imagecluster/tree/master/imagecluster
