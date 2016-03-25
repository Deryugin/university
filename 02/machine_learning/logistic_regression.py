#!/bin/python2

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt
import math

def theta(s):
    if s > 100:
        return 1.
    if s < -100:
        return 0.
    return math.exp(s) / (1 + math.exp(s))

def get_x(train_sample):
    y = []
    a = []

    N = len(train_sample)
    img_sz = len(train_sample[0][1])
    img2np = []
    up = []
    w = np.array([1.]*img_sz)

    for i in range(0, N):
        label = train_sample[i][0]
        img = train_sample[i][1]

        if label == 1:
            y.append(-1.)
        else:
            y.append(1.)

        img2np.append(np.array(img))
        up.append(y[i] * img2np[i])

    for i in range(0, 1000):
        grad = np.array([0.] * img_sz)

        for j in range(0, N):
            up_l = up[j]
            exp_arg = y[j] * w.T.dot(img2np[j])
            if exp_arg > 100:
                up_l = 0
                down = 1
            else:
                down = 1. + math.exp(exp_arg)
            grad = grad + up_l / down

        grad = grad * (-1. / N)
        w = w - 0.01 * grad
        print np.linalg.norm(grad)
        if np.linalg.norm(grad) < 0.01 * img_sz:
            break

    return w

def test_x(x, test_sample):
    total = 0
    correct = 0

    l = len(test_sample)

    for i in range(0, l):
        label   = test_sample[i][0]
        img     = test_sample[i][1]
        img = img[:]
        img = np.array([img])
        res = theta(x.dot(img.T))

        if (label == 5 and res > 0.5) or (label == 1 and res <= 0.5):
            correct = correct + 1
    return 1. - 1. * correct / l;
