#!/bin/python2

# Convert MNIST handwritten database to SVM-light format

import util

util.load_data()

data = util.train_sample(0xFFFFFFFF) + util.test_sample(0xFFFFFFF)

f = open("vectors.dat","w")

for img in data:
    if img[0] == 1:
        f.write("-1 ")
    else:
        f.write("1 ")

    for k in range(0, len(img[1])):
        if (img[1][k] > 0):
            f.write(str(k) + ":" + str(img[1][k]) + " ")

    f.write("\n")
