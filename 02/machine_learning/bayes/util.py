#!/usr/bin/python2.7

import sys

mx = []
mn = []
required_fields = [2, 3, 8, 9, 11, 15, 18, 31, 37, 39, 40, 43, 50, 57]
attr_n = len(required_fields)
inf = 99999999.

simple_l = [1, 2, 5, 6, 8, 10, 11, 12]
ranged_l = [0, 3, 4, 7, 9]

c_cnt = [0, 0]
o_cnt = []

attr_sum = [[],[]]

cat_max = 15

def categorize(x, cat):
    if cat in simple_l:
        return int(x)

    if x < mn[cat] or abs(mx[cat] - mn[cat]) < 0.0001:
        return 0

    if x > mx[cat]:
        return cat_max - 1

    return int((x - mn[cat] - 1/inf) / (mx[cat] - mn[cat]) * cat_max)

def init(data):
    for i in range(0, attr_n):
        mx.append(-inf)
        mn.append(inf)

    for k in range(0, attr_n):
        o_cnt.append([])
        for j in range(0, max(100, cat_max)):
            o_cnt[k].append([0, 0])
            attr_sum[0].append(0)
            attr_sum[1].append(0)

    for i in data:
        for j in ranged_l:
            val = float(i[j])
            if mx[j] < val:
                mx[j] = val
            if mn[j] > val:
                mn[j] = val

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
