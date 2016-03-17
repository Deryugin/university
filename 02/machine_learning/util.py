#!/bin/python2

import numpy as np

def resize(img, new_sz):
    res = [0.0] * new_sz * new_sz
    coef = (1. * new_sz / 28) * (1. * new_sz / 28)
    t = new_sz * (28 / new_sz)
    for i in range(0, t):
        for j in range(0, t):
            #print "#################"
            #print i
            #print j
            #print t
            #print len(img)
            res[new_sz * (i * new_sz / 28) + j * new_sz / 28] += 1. * img[i * 28 + j] * coef
    return res

labels_sig_sz = 8
images_sig_sz = 16

train_labels_fname  = "train-labels-idx1-ubyte"
train_images_fname  = "train-images-idx3-ubyte"
test_labels_fname   = "t10k-labels-idx1-ubyte"
test_images_fname   = "t10k-images-idx3-ubyte"

# TODO get it from input files
train_num   = 60000
test_num    = 10000

train_set   = []
test_set    = []

def get_label(n, labels):
    return ord(labels[labels_sig_sz + n])

def get_img(n, images):
    res = []
    for i in range(0, 28 * 28):
        res.append(ord(images[images_sig_sz + n * 28 * 28 + i]))
    return res


def load_data():
    fimages = open(train_images_fname)
    flabels = open(train_labels_fname)

    train_images = fimages.read()
    train_labels = flabels.read()

    fimages.close()
    flabels.close()

    fimages = open(test_images_fname)
    flabels = open(test_labels_fname)

    test_images = fimages.read()
    test_labels = flabels.read()

    fimages.close()
    flabels.close()

    for i in range(0, train_num):
        label = get_label(i, train_labels)

        if label != 1 and label != 5:
            continue

        train_set.append((label, get_img(i, train_images)))

    for i in range(0, test_num):
        label = get_label(i, test_labels)

        if label != 1 and label != 5:
            continue

        test_set.append((label, get_img(i, test_images)))

def train_sample(sz):
    np.random.shuffle(train_set)
    return train_set[:sz][:]

def test_sample(sz):
    np.random.shuffle(test_set)
    return test_set[:sz][:]
