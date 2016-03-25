#!/bin/python2

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt
import math

def theta(s):
    if s > 64:
        return 1.
    if s < -64:
        return 0.
    return math.exp(s) / (1 + math.exp(s))

def get_x(train_sample):
    y = []

    N = len(train_sample)
    img_sz = len(train_sample[0][1])
    img2np = []
    up = []
    w = np.array([0.5]*img_sz)

    for i in range(0, N):
        label = train_sample[i][0]
        img = train_sample[i][1]

        if label == 1:
            y.append(-1.)
        else:
            y.append(1.)

        img2np.append(np.array(img))
        up.append(y[i] * img2np[i])

    for i in range(0, 10000):
        grad = np.array([0.] * img_sz)

        for j in range(0, N):
            exp_arg = y[j] * w.T.dot(img2np[j])
            if exp_arg < 64:
                down = 1. + math.exp(exp_arg)
                grad += up[j] / down

        grad *= -1. / N
        w -= 0.0003 * grad
        if np.linalg.norm(grad) < 0.0001 * img_sz:
            break

    return w

def test_x(x, test_sample):
    correct = 0

    N = len(test_sample)

    for i in range(0, N):
        label   = test_sample[i][0]
        img     = test_sample[i][1]
        img = np.array([img])
        res = theta(x.dot(img.T))

        if (label == 5 and res > 0.5) or (label == 1 and res <= 0.5):
            correct = correct + 1
    return 1. - 1. * correct / N
