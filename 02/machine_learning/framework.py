#!/bin/python2

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt
import linear_regression as lin_r
import logistic_regression as log_r
import util
import sys

resolution_list = [4, 8, 16]
lim_list = [200, 2000, 20000]

if len(sys.argv) < 2:
    util.print_usage()
    exit()

if sys.argv[1] == "linear_regression":
    get_x   = lin_r.get_x
    test_x  = lin_r.test_x
elif sys.argv[1] == "logistic_regression":
    get_x   = log_r.get_x
    test_x  = log_r.test_x
else:
    util.print_usage();
    exit()

util.load_data()

res_ein     = []
res_eout    = []

for c_res in resolution_list:
    pr = []
    e_in = []
    e_out = []
    print "Image resolution: " + str(c_res) + "x" + str(c_res)
    for sz in lim_list:
        print "        Sample size: " + str(sz)
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

    res_ein.append(np.array(e_in))
    res_eout.append(np.array(e_out))

    print str(c_res) + "x" + str(c_res) + ": " + str(pr)

exit()

for i in range(0, len(t)):
    plt.plot(np.array(lim_list), res_ein[i])

    plt.xlabel(str(c_res) + "x" + str(c_res))
    plt.ylabel('Err_In')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

    plt.plot(np.array(lim_list), res_eout[i])

    plt.xlabel(str(c_res) + "x" + str(c_res))
    plt.ylabel('Err_Out')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()
