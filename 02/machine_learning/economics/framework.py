#!/bin/python2

import numpy as np
import cv2
import matplotlib.pyplot as plt
import util
import sys

raw_data = []

regions = ["ARB", "EAS", "EAP", "ECA", "EMU",
"ECS", "EUU", "HIC", "NOC", "OEC",
"HPC", "LDC", "LCN", "LAC", "MEA",
"OED", "PSS", "SSF", "SSA", "WLD"]

year_learn_start = 1980
year_learn_end   = 2008
year_predict     = 5
learn_vec_sz     = 5

mvec_sz = learn_vec_sz
start   = year_learn_start - 1960
edge    = 1

def _to_float(val):
    if (val == ".."):
        return 0
    return float(val)

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
    for j in range(pos, pos + learn_vec_sz):
        for k in range(0, len(raw_data)):
            #print str(k) + ' ' + str(j)
            #print len(raw_data)
            #print len(raw_data[k])
            #print "####"
            res.append(_to_float(raw_data[k][j]))
    return res

res_x = []
for i in range(0, len(raw_data)):
    print i
    x_vec = []
    y = []
    for j in range(start, len(raw_data[0]) - mvec_sz - 1):
        cur_x = _mvec(j)
        cur_x.append(1.)
        y.append(_to_float(raw_data[i][j + mvec_sz + 1]))
        x_vec.append(cur_x)

    a = x_vec[:]
    a = np.array(a)
    aT = a.T
    x = np.array([np.linalg.pinv(aT.dot(a)).dot(aT).dot(np.array(y[:]))])
    res_x.append(x)


for i in range(0, year_predict):
    pos = year_learn_end - 1960 + i + 1
    inp = _mvec(pos - mvec_sz)
    inp.append(1.)
    inp = np.array(inp)
    inp = inp.T

    for j in range(0, len(raw_data)):
        val = res_x[j].dot(inp)
        if pos >= len(raw_data[j]):
            raw_data[j].append(val)
        else:
            raw_data[j][pos] = val

for j in range(0, len(raw_data)):
    for i in range(0, year_predict):
        pos = year_learn_end - 1960 + i + 1
        sys.stdout.write(str(int(raw_data[j][pos])) + ' ')
    print ''


'''

    #for j in range(edge - 2, len(raw_data[0]) - mvec_sz - start):
    for j in range(year_learn_end - mvec_sz, year_learn_end + 1):
        pos = j - 1960
        #print "pos is " + str(pos)
        #print pos + mvec_sz + 1
        #print len(raw_data[i])
        #print len(x_vec)
        #correct = _to_float(raw_data[i][pos + mvec_sz + 1])
        #img = np.array([x_vec[pos]])
        print "pos is " + str(pos)
        tmp = _mvec(pos)
        tmp.append(1.)
        img = np.array([tmp])
        predicted = x.dot(img.T)
        #if (pos >= len(raw_data[i])):
        raw_data[i].append(predicted)
        #print "Year " + str(start + j + mvec_sz + 1960) + "correct: " + str(float(correct)) +" prediction: " + str(float(1. * predicted/correct))
        #print int(correct)
        sys.stdout.write(str(predicted) + ' ')
        #print "###"

    print ''
'''
