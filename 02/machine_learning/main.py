#!/usr/bin/python

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt

train_labels_fname="train-labels-idx1-ubyte"
train_images_fname="train-images-idx3-ubyte"
test_labels_fname="t10k-labels-idx1-ubyte"
test_images_fname="t10k-images-idx3-ubyte"

train_num = 60000
test_num = 10000

train_lim = []

labels_sig_sz = 8
images_sig_sz = 16

im_p = images_sig_sz
lb_p = labels_sig_sz

c_res = 4

labels=[]
images=[]

img_test_set = []
lbl_test_set = []
img_train_set = []
lbl_train_set = []

def resize(img, new_sz):
    res= [0.0] * new_sz * new_sz
    coef = 1. * new_sz / 28
    for i in range(0, new_sz * (28 / new_sz)):
        for j in range(0, new_sz * (28 / new_sz)):
            res[new_sz * (i * new_sz / 28) + j * new_sz / 28] += 1. * img[i * 28 + j] * coef * coef
    return res

def next_label(n):
    return ord(labels[labels_sig_sz + n])

def next_img(n):
    res = []
    for i in range(0, 28 * 28):
        res.append(ord(images[images_sig_sz + n * 28 * 28 + i]))
    return res

fimages = open(train_images_fname)
flabels = open(train_labels_fname)

images = fimages.read()
labels = flabels.read()

for i in range(0, train_num):
    label = next_label(i)

    if label != 1 and label != 5:
        continue

    img_train_set.append(next_img(i))
    lbl_train_set.append(label)

fimages = open(test_images_fname)
flabels = open(test_labels_fname)

images = fimages.read()
labels = flabels.read()

for i in range(0, test_num):
    label = next_label(i)

    if label != 1 and label != 5:
        continue

    img_test_set.append(next_img(i))
    lbl_test_set.append(label)

def get_x():
    global images
    global labels
    global train_lim
    global c_res

    fimages = open(train_images_fname)
    flabels = open(train_labels_fname)

    images = fimages.read()
    labels = flabels.read()

    y = []
    a = []

    for i in range(0, min(train_lim, len(lbl_train_set))):
        label = lbl_train_set[i]
        img = img_train_set[i]

        if label == 1:
            y.append(-1.)
        else:
            y.append(1.)
        img = resize(img, c_res)
        img.append(1.)
        a.append(img)

    a = np.array(a)
    y = np.array(y)

    x = np.array([np.linalg.pinv(a.T.dot(a)).dot(a.T).dot(y)])

    fimages.close()
    flabels.close()

    return x

def test_x(x):
    global images
    global labels
    global c_res
    global train_lim

    fimages = open(train_images_fname)
    flabels = open(train_labels_fname)

    images = fimages.read()
    labels = flabels.read()

    total = 0
    correct = 0

    for i in range(0, min(train_lim, len(lbl_train_set))):
        label = lbl_train_set[i]
        img = img_train_set[i]

        img = resize(img, c_res)

        img.append(1)
        img = np.array([img])
        res = x.dot(img.T)
        total = total + 1
        if (label == 5 and res > 0) or (label == 1 and res < 0):
            correct = correct + 1

    err_in = 1. * correct / total;

    fimages = open(test_images_fname)
    flabels = open(test_labels_fname)

    images = fimages.read()
    labels = flabels.read()

    total = 0
    correct = 0

    for i in range(0, len(lbl_test_set)):
        label = lbl_test_set[i]
        img = img_test_set[i]

        img = resize(img, c_res)

        img.append(1)
        img = np.array([img])
        res = x.dot(img.T)
        total = total + 1
        if (label == 5 and res > 0) or (label == 1 and res < 0):
            correct = correct + 1

    err_out = 1. * correct / total;
    return (err_in, err_out)

lim_list = [200, 2000, 20000]

print "Training sample size " + str(lim_list)

errors = []

for c_res in [4, 8, 16]:
    pr = []
    e_in = []
    e_out = []
    for train_lim in lim_list:
        (e_i, e_o) = test_x(get_x())
        e_in.append(e_i)
        e_out.append(e_o)
        pr.append(str(e_i) + "/" + str(e_o))

    t = np.array(lim_list)
    s = np.array(e_in)
    plt.plot(t, s)

    plt.xlabel(str(c_res) + "x" + str(c_res))
    plt.ylabel('Err_In')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

    s = np.array(e_out)
    plt.plot(t, s)

    plt.xlabel(str(c_res) + "x" + str(c_res))
    plt.ylabel('Err_Out')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

    print str(c_res) + "x" + str(c_res) + ": " + str(pr)
