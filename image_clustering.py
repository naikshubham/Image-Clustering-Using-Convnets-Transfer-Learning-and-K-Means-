# -*- coding: utf-8 -*-
"""image_clustering

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15EPK1b1ro69u9M0lj8hHRWDB9hwR-crQ

**Image Clustering Using Convnets Transfer Learning and K-Means**
"""

import cv2
import os
import numpy as np
from keras.models import load_model, Model
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
import matplotlib.image as mpimg
# %matplotlib inline

def get_model(layer='fc2'):
  """Keras Model of the VGG16 network, with the output layer set to `layer`.
    The default layer is the second-to-last fully connected layer 'fc2' of
    shape (4096,).
    Parameters
    ----------
    layer : str
        which layer to extract (must be of shape (None, X)), e.g. 'fc2', 'fc1'
        or 'flatten'
    """
    # base_model.summary():
    #     ....
    #     block5_conv4 (Conv2D)        (None, 15, 15, 512)       2359808
    #     _________________________________________________________________
    #     block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0
    #     _________________________________________________________________
    #     flatten (Flatten)            (None, 25088)             0
    #     _________________________________________________________________
    #     fc1 (Dense)                  (None, 4096)              102764544
    #     _________________________________________________________________
    #     fc2 (Dense)                  (None, 4096)              16781312
    #     _________________________________________________________________
    #     predictions (Dense)          (None, 1000)              4097000
    #
  base_model = VGG16(weights='imagenet', include_top=True)
  model = Model(inputs=base_model.input,
                outputs=base_model.get_layer(layer).output)
  return model

from google.colab import drive
drive.mount('/content/drive')

# path_1 = '/content/drive/My Drive/Google Photos/'
# dirs = [dirs for dirs in os.listdir(path_1)]
# all_pics = []
# count =0 
# for directory in dirs:
#   files = [file for file in os.listdir(path_1+directory+'/') if file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.PNG') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.JPEG')]
#   print(directory)
#   print('files written ->',count)
#   for file in files:
# #     print(file)
#     img = cv2.imread(path_1+directory+'/'+file)
#     cv2.imwrite(path_1+'All Pics/'+file, img)
#     count += 1

print(len([file for file in os.listdir('/content/drive/My Drive/Google Photos/All Pics/')]))

def get_files(path_to_files, size):
  fn_imgs = []
  files = [file for file in os.listdir(path_to_files)]
  for file in files:
      img = cv2.resize(cv2.imread(path_to_files+file), size)
  #         img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
      fn_imgs.append([file, img])
  return dict(fn_imgs)

# path_to_files = '/content/drive/My Drive/Google Photos/All Pics/'
# size = (224, 224, 3)

def feature_vector(img_arr, model):
  if img_arr.shape[2] == 1:
    img_arr = img_arr.repeat(3, axis=2)

  # (1, 224, 224, 3)
  arr4d = np.expand_dims(img_arr, axis=0)  
  arr4d_pp = preprocess_input(arr4d)
  return model.predict(arr4d_pp)[0,:]

def feature_vectors(imgs_dict, model):
  f_vect = {}
  for fn, img in imgs_dict.items():
    f_vect[fn] = feature_vector(img, model)
  return f_vect

# path_to_files = '/content/drive/My Drive/Google Photos/All Pics/'
# size = (224, 224)
imgs_dict = get_files(path_to_files = '/content/drive/My Drive/Google Photos/All Pics/',size = (224, 224))

# Create Keras NN model.
model = get_model()

# Feed images through the model and extract feature vectors.
img_feature_vector = feature_vectors(imgs_dict, model)

images = list(img_feature_vector.values())
fns = list(img_feature_vector.keys())
sum_of_squared_distances = []
K = range(1, 30)
for k in K:
  km = KMeans(n_clusters=k)
  km = km.fit(images)
  sum_of_squared_distances.append(km.inertia_)
plt.plot(K, sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

kmeans = KMeans(n_clusters=8, init='k-means++')
kmeans.fit(images)
y_kmeans = kmeans.predict(images)
file_names = list(imgs_dict.keys())

n_clusters = 8
cluster_path = '/content/drive/My Drive/Google Photos/'
path_to_files = '/content/drive/My Drive/Google Photos/All Pics/'

for c in range(0,n_clusters):
  if not os.path.exists(cluster_path+'cluster_'+str(c)):
    os.mkdir(cluster_path+'cluster_'+str(c))
    
for fn, cluster in zip(file_names, y_kmeans):
  image = cv2.imread(path_to_files+fn)
  cv2.imwrite(cluster_path+'cluster_'+str(cluster)+'/'+fn, image)

fig = plt.figure(figsize=(14, 14))

cluster_path = '/content/drive/My Drive/Google Photos/cluster_5/'
images = [file for file in os.listdir(cluster_path)]

for cnt, data in enumerate(images[1:30]):
#     print(data)
    y = fig.add_subplot(6, 5, cnt+1)
    img = mpimg.imread(cluster_path+data)
    y.imshow(img)
    plt.title('cluster_5')
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)

fig = plt.figure(figsize=(14, 14))

cluster_path = '/content/drive/My Drive/Google Photos/cluster_7/'
images = [file for file in os.listdir(cluster_path)]

for cnt, data in enumerate(images[1:30]):
#     print(data)
    y = fig.add_subplot(6, 5, cnt+1)
    img = mpimg.imread(cluster_path+data)
    y.imshow(img)
    plt.title('cluster_7')
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)