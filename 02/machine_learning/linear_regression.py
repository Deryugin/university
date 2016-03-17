#!/bin/python2

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt

def get_x(train_sample):
    y = []
    a = []

    for i in range(0, len(train_sample)):
        label   = train_sample[i][0]
        img     = train_sample[i][1]

        if label == 1:
            y.append(-1.)
        else:
            y.append(1.)
        img.append(1.)
        a.append(img)

    a = np.array(a)
    y = np.array(y)
    x = np.array([np.linalg.pinv(a.T.dot(a)).dot(a.T).dot(y)])

    return x

def test_x(x, test_sample):
    total = 0
    correct = 0

    for i in range(0, len(test_sample)):
        label   = test_sample[i][0]
        img     = test_sample[i][1]

        img.append(1)
        img = np.array([img])
        res = x.dot(img.T)
        total = total + 1
        if (label == 5 and res > 0) or (label == 1 and res < 0):
            correct = correct + 1

    return 1. * correct / total;
