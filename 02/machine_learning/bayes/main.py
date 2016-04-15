#!/usr/bin/python2.7

import sys
import util
import numpy as np

required_fields = util.required_fields
attr_n = util.attr_n

if len(sys.argv) != 3:
    util.print_usage()
    exit()

data = util.read_data(sys.argv[1])
util.init(data)

c_cnt    = util.c_cnt
o_cnt    = util.o_cnt
simple_attr = util.simple_attr
ranged_attr = util.ranged_attr

# Learning
data = np.array(data)
np.random.shuffle(data)
data = data[:100]

for record in data:
    t = int(record[13]) # 0   => Healthy
                        # 1-4 => Has heart disease
    if t > 4:
        print "Error"
        exit()
    if t > 0:
        t = 1

    for attr in simple_attr + ranged_attr:
        if abs(float(record[attr]) + 9.0) < 0.01:
            continue
        val = util.get_val(record, attr)
        util.attr_sum[t][attr] += 1
        o_cnt[attr][val][t] += 1

    c_cnt[t] += 1

total = 0
correct = 0
slack = 0
data = util.read_data(sys.argv[2])
for record in data:
    p = [1. * c_cnt[0] / (c_cnt[0] + c_cnt[1]),
            1. * c_cnt[1] / (c_cnt[0] + c_cnt[1])]
    t = int(record[13])
    if t > 4:
        print "Error"
        exit()
    if t > 0:
        t = 1

    for attr in simple_attr + ranged_attr:
        # If value equals -9 then the value is not
        # specified
        if abs(float(record[attr]) + 9.0) < 0.01:
            continue

        val = util.get_val(record, attr)

        for k in [0, 1]:
            sm = util.attr_sum[k][attr];
            if sm == 0:
                p[k] = p[k] * 0.5
            else:
                p[k] = p[k] * o_cnt[attr][val][k] / sm

    if p[t] > p[t - 1]:
        correct = correct + 1

    total = total + 1

print 1. * correct / total
