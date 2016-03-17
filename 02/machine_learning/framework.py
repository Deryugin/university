#!/bin/python2

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt
import linear_regression as lin_r
import util

c_res = 4

lim_list = [200, 2000, 20000]

util.load_data()

print "Training sample size " + str(lim_list)

train_lim = []

get_x = lin_r.get_x
test_x = lin_r.test_x

for c_res in [4, 8, 16]:
    pr = []
    e_in = []
    e_out = []

    img = resize(img, c_res)

    for train_lim in lim_list:
        l = min(train_lim, len(lbl_train_set))
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
