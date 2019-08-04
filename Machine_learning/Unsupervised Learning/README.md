# Unsupervised Learning

**Table of Contents**

[Introduction](#introduction)
| [Machine-learning](#machine-learning)
| [Busquedas](#Busquedas)
| [References](#Referencias)

---

## Introduction ##

In this section I'm going to explore the litterature of unsupervised learning, some examples and tutorials of its application.

According to [1] this approach tries to learn the structure of the data; in order to search the patterns we have different techniques, some of them are:

+ Dimensionality reduction

The idea of these algorithms is to reduce high-dimensional input data to a low-dimensional space, filtering out the features that are not relevant.

    + Linear Projection and noolinear dimensionality reduction are the two branches of dimensionality
    + Principal Component Analysis (knows as PCA) it allows us to get the most important features in explaining the variability among the instances in the data. From this we can have some techniques, such as mini batch _incremental PCA_, nonlinear _kernel PCA_, sparse _sparse PCA_.
    + Singular Value Decomposition (SVD) its objective is to reduce the rank of the original matrix of features to a small rank where the original matrix can be recreated using a linear combination of some of the vectors. 
    + Random Projection. This approach involves projecting points from high-dimensional space to a space of much lower dimensions where the salce of distances between the points is preserved.
    + Manifold learning. Sometimes we need to face nonlinear transformation of the data 
        - Isomap is one type of manifold learning approach. This technique learns the intrinsic geometry of the data manifold by estimating the _geodesic_ or _curved distance_ between each point and its neighbords rather than the Euclidean distance. 
   

##  References ##

+ [1] Hands-On Unsupervised Learning Using Python : How to Build Applied Machine Learning Solutions from Unlabeled Data. Ankur A. Patel

```
                    .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"
```
