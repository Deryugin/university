#!/bin/python2

# Convert MNIST handwritten database to SVM-light format

import util

util.load_data()

data = util.train_sample(0xFFFFFFFF) + util.test_sample(0xFFFFFFF)

resolution_list = [4, 8, 16]
lim_list = [200, 2000, 20000]

for c_res in resolution_list:
    pr = []
    e_in = []
    e_out = []
    for sz in lim_list:
        t_set = util.train_sample(sz)
        l = len(t_set)
        f = open(str(c_res) + str(sz) + "vectors.dat","w")
        for i in range(0, l):
            t_set[i] = (t_set[i][0], util.resize(t_set[i][1], c_res))
            img = t_set[i]
            if img[0] == 1:
                f.write("-1 ")
            else:
                f.write("1 ")

            for k in range(0, len(img[1])):
                if (img[1][k] > 0):
                    f.write(str(k + 1) + ":" + str(img[1][k]) + " ")

            f.write("\n")

        f.close()
        f = open(str(c_res)+str(sz)+"test.dat","w")
        t_set = util.test_sample(sz)
        l = len(t_set)
        for i in range(0, l):
            t_set[i] = (t_set[i][0], util.resize(t_set[i][1], c_res))
            img = t_set[i]
            if img[0] == 1:
                f.write("-1 ")
            else:
                f.write("1 ")

            for k in range(0, len(img[1])):
                if (img[1][k] > 0):
                    f.write(str(k + 1) + ":" + str(img[1][k]) + " ")

            f.write("\n")
        f.close()
