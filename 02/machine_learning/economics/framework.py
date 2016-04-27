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

for i in range(0, len(raw_data)):
    x_vec = []
    y = []
    start = 20
    for j in range(start, len(raw_data[0]) - 1):
        cur_x = []
        for k in range(0, len(raw_data)):
            if (raw_data[k][j] == ".."):
                cur_x.append(0)
            else:
                cur_x.append(float(raw_data[k][j]))
        cur_x.append(1.)
        y.append(float(raw_data[i][j + 1]))
        x_vec.append(cur_x)

    edge = 5

    a = x_vec[:edge]
    a = np.array(a)
    aT = a.T
    x = np.array([np.linalg.pinv(aT.dot(a)).dot(aT).dot(np.array(y[:edge]))])

    for j in range(start + edge, len(raw_data[0]) - 1):
        correct = float(raw_data[i][j + 1])
        img = np.array([x_vec[j]])
        predicted = x.dot(img.T)

        print int(correct)
        print int(predicted)
        print "###"
    break
