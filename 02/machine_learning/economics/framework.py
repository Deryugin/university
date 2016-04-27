#!/bin/python2

import numpy as np
import cv
import cv2
import matplotlib.pyplot as plt
import util
import sys

raw_data = []

regions = ["ARB", "EAS", "EAP", "ECA", "EMU",
"ECS", "EUU", "HIC", "NOC", "OEC",
"HPC", "LDC", "LCN", "LAC", "MEA",
"OED", "PSS", "SSF", "SSA", "WLD"]

mvec_sz = 20
start = 20
edge = 10

def load_data():
    fdata = open("data")

    data = [line.rstrip('\n') for line in fdata]

    for line in data:
        if len(line) < 1:
            break

        words = line.split(' ')

        raw_data.append(words[1:])

    fdata.close()

load_data()
regions_cnt = len(regions)
years_cnt = len(raw_data[0])

def _mvec(pos):
    res = []
    for j in range(pos, pos + 2):
        for k in range(0, len(raw_data)):
            if (raw_data[k][j] == ".."):
                res.append(-1000000000.)
            else:
                res.append(float(raw_data[k][j]))
    return res

print "Learn from data up to " + str(1960 + start + edge + mvec_sz) + " year"
for i in range(0, len(raw_data)):
    x_vec = []
    y = []
    for j in range(start, len(raw_data[0]) - mvec_sz):
        cur_x = _mvec(j)
        cur_x.append(1.)
        y.append(float(raw_data[i][j + mvec_sz]))
        x_vec.append(cur_x)

    a = x_vec[:edge]
    a = np.array(a)
    aT = a.T
    x = np.array([np.linalg.pinv(aT.dot(a)).dot(aT).dot(np.array(y[:edge]))])
    for j in range(edge - 2, len(raw_data[0]) - mvec_sz - start):
        correct = float(raw_data[i][start + j + mvec_sz])
        img = np.array([x_vec[j]])
        predicted = x.dot(img.T)
        print "Year " + str(start + j + mvec_sz + 1960) + " prediction: " + str(float(1. * predicted/correct))
        #print int(correct)
        #print int(predicted)
        #print "###"

    print "################"
