#!/usr/bin/python2.7

import sys

max_val = []
min_val = []
required_fields = [2, 3, 8, 9, 11, 15, 18, 31, 37, 39, 40, 43, 50, 57]
attr_n = len(required_fields)
inf = 99999999.

simple_attr = [1, 2, 5, 6, 8, 10, 11, 12] # No need to break into intervals
ranged_attr = [0, 3, 4, 7, 9]             # Need to break into intervals

c_cnt = [0, 0]
o_cnt = []

attr_sum = [[],[]]

attr_max = 15

def get_val(record, attr):
    x = float(record[attr])
    if attr in simple_attr:
        return int(x)

    if x < min_val[attr] or abs(max_val[attr] - min_val[attr]) < 0.0001:
        return 0

    if x > max_val[attr]:
        return attr_max - 1

    return int((x - min_val[attr] - 1/inf) / (max_val[attr] - min_val[attr]) * attr_max)

def init(data):
    for i in range(0, attr_n):
        max_val.append(-inf)
        min_val.append(inf)

    for k in range(0, attr_n):
        o_cnt.append([])
        for j in range(0, max(100, attr_max)):
            o_cnt[k].append([0, 0])
            attr_sum[0].append(0)
            attr_sum[1].append(0)

    for i in data:
        for attr in ranged_attr:
            val = float(i[attr])
            if max_val[attr] < val:
                max_val[attr] = val
            if min_val[attr] > val:
                min_val[attr] = val

def print_usage():
    print "USAGE: " + sys.argv[0] + " [TRAIN_FILE TEST_FILE]"

def read_data(fname):
    fdata = open(fname)

    words = []

    for line in fdata:
        for word in line.split():
            words.append(word)

    res = []
    fields_total = 76

    for i in range(0, len(words) / fields_total):
        tmp = []
        for j in required_fields:
            tmp.append(words[i * fields_total + j])
        res.append(tmp)

    return res
