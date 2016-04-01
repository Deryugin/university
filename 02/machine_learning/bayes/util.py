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

cat_max = 1000

def categorize(x, cat):
    if x < mn[cat]:
        return 0

    if x > mx[cat]:
        return cat_max - 1

    '''
    step = 0
    tmp = 1. * mn[cat]
    while tmp < x:
        step = step + 1
        if step == cat_max - 1:
            return step
        tmp = tmp + (mx[cat] - mn[cat]) / cat_max

    return step
    '''

    return int((x - mn[cat] - 1/inf) / (mx[cat] - mn[cat]) * cat_max)

def init(data):
    for i in range(0, attr_n):
        mx.append(-inf)
        mn.append(inf)

    for k in range(0, attr_n):
        o_cnt.append([])
        for j in range(0, cat_max):
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
    print "USAGE: " + sys.argv[0] + " [DATA FILE]"

def read_data():
    fdata = open(sys.argv[1])

    words = []

    for line in fdata:
        for word in line.split():
            words.append(word)

    res = []
    fields_total = 90

    for i in range(0, len(words) / fields_total):
        tmp = []
        for j in required_fields:
            tmp.append(words[i * fields_total + j])
        res.append(tmp)

    return res
