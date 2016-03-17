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

get_x   = lin_r.get_x
test_x  = lin_r.test_x

for c_res in [4, 8, 16]:
    pr = []
    e_in = []
    e_out = []

    for sz in lim_list:
        t_set = util.train_sample(sz)
        l = len(t_set)
        for i in range(0, l):
            t_set[i] = (t_set[i][0], util.resize(t_set[i][1], c_res))
        x   = get_x(t_set)
        e_i = test_x(x, t_set)
        t_set = util.test_sample(sz)
        l = len(t_set)
        for i in range(0, l):
            t_set[i] = (t_set[i][0], util.resize(t_set[i][1], c_res))

        e_o = test_x(x, t_set)

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
