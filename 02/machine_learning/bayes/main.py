#!/usr/bin/python2.7

import sys
import util
import numpy as np

required_fields = util.required_fields
attr_n = util.attr_n

#################################
#      Main part goes here      #
#################################

if len(sys.argv) != 3:
    util.print_usage()
    exit()

data = util.read_data(sys.argv[1])
util.init(data)

c_cnt    = util.c_cnt
o_cnt    = util.o_cnt
simple_l = util.simple_l
ranged_l = util.ranged_l

# Learning
data = np.array(data)
np.random.shuffle(data)
data = data[:100]

for i in data:
    t = int(i[13])
    if t > 4:
        print "WTF"
        exit()
    if t > 0:
        t = 1

    for j in simple_l:
        val = int(i[j])
        if val == -9:
            continue

        if val < 0:
            print "WTF"
            exit()
        util.attr_sum[t][j] = util.attr_sum[t][j] + 1
        o_cnt[j][val][t] = o_cnt[j][val][t] + 1

    for j in ranged_l:
        if abs(float(i[j]) - 9.0) < 0.01:
            continue
        cat = util.categorize(float(i[j]), j)
        util.attr_sum[t][j] = util.attr_sum[t][j] + 1
        o_cnt[j][cat][t] = o_cnt[j][cat][t] + 1

    c_cnt[t] = c_cnt[t] + 1

total = 0
correct = 0
slack = 0
data = util.read_data(sys.argv[2])
for i in data:
    p_0 = 1. * c_cnt[0] / (c_cnt[0] + c_cnt[1])
    p_1 = 1. * c_cnt[1] / (c_cnt[0] + c_cnt[1])

    t = int(i[13])
    if t > 4:
        print "WTF"
        exit()
    if t > 0:
        t = 1

    for j in simple_l:
        val = int(i[j])
        if val == -9:
            continue

        if val < 0:
            print "WTF"
            exit()
        sm = util.attr_sum[0][j];
        if sm == 0:
            continue
        p_0 = p_0 * o_cnt[j][val][0] / sm

        sm = util.attr_sum[1][j];
        if sm == 0:
            continue

        p_1 = p_1 * o_cnt[j][val][1] / sm

    for j in ranged_l:
        if abs(float(i[j]) - 9.0) < 0.01:
            continue

        val = util.categorize(float(i[j]), j)

        sm = util.attr_sum[0][j];
        if sm == 0:
            continue

        p_0 = p_0 * o_cnt[j][val][0] / sm

        sm = util.attr_sum[1][j];
        if sm == 0:
            continue

        p_1 = p_1 * o_cnt[j][val][1] / sm

    #print p_0
    #print p_1
    #print "##########"
    if p_0 + p_1 < 0.0000000001:
        slack = slack + 1
    if (t == 0 and p_0 > p_1) or (t > 0 and p_1 > p_0):
        correct = correct + 1

    total = total + 1

print 1. * correct / total
print "Slack: " + str(slack) + " out of " + str(total)
