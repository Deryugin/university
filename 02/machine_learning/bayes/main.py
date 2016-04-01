#!/usr/bin/python2.7

import sys

def print_usage():
    print "USAGE: " + sys.argv[0] + " [DATA FILE]"

required_fields = [2, 3, 8, 9, 11, 15, 18, 31, 37, 39, 40, 43, 50, 57]
attr_n = len(required_fields)

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

#################################
#      Main part goes here      #
#################################

if len(sys.argv) != 2:
    print_usage()
    exit()

data = read_data()
c_cnt = [0, 0]

o_cnt = []
for k in range(0, attr_n):
    o_cnt.append([])

    for j in range(0, 100):
        o_cnt[k].append([0, 0])

simple_l = [1, 2, 5, 6, 8, 10, 11, 12]
compl_l = [0, 3, 4, 7, 9]

# Learn from simple data

for i in data:
    t = int(i[13])
    if t > 4:
        print "WTF"
        exit()
    if t > 0:
        t = 1

    for j in simple_l:
        val = int(i[j])
        if val < 0:
            continue

        o_cnt[j][val][t] = o_cnt[j][val][t] + 1
    c_cnt[t] = c_cnt[t] + 1

# Group by intervals
inf = 99999999.
mx = []
mn = []
for i in range(0, attr_n):
    mx.append(-inf)
    mn.append(inf)

cat_max = 5

def categorize(x, cat):
    if x < mn[cat]:
        return 0

    if x > mx[cat]:
        return cat_max - 1

    step = 0
    tmp = 1. * mn[cat]
    while tmp < x:
        step = step + 1
        if step == cat_max - 1:
            return step
        tmp = tmp + (mx[cat] - mn[cat]) / cat_max

    return step

for i in data:
    for j in compl_l:
        val = float(i[j])
        if mx[j] < val:
            mx[j] = val
        if mn[j] > val:
            mn[j] = val

for i in data:
    t = int(i[13])
    if t > 4:
        print "WTF"
        exit()
    if t > 0:
        t = 1

    for j in compl_l:
        cat = categorize(float(i[j]), j)
        if cat < 0:
            print "WTF"
            exit()
        o_cnt[j][cat][t] = o_cnt[j][cat][t] + 1

total = 0
correct = 0

for i in data:
    p_0 = 1. * c_cnt[0] / (c_cnt[0] + c_cnt[1])
    p_1 = 1. * c_cnt[1] / (c_cnt[0] + c_cnt[1])

    for j in simple_l:
        val = int(i[j])

        #if val >= 0 and o_cnt[j][val][0] + o_cnt[j][val][1] == 0:
        #print val
        #if val >= 0 and o_cnt[j][val][int(i[13])] == 0:
        #    print "WTF 1"
        #    exit()

        sm = 0;
        for k in range(0, 100):
            sm += o_cnt[j][k][0]
        p_0 = p_0 * o_cnt[j][val][0] / sm

        sm = 0;
        for k in range(0, 100):
            sm += o_cnt[j][k][1]
        p_1 = p_1 * o_cnt[j][val][1] / sm

        p_1 = p_1 * 10000000
        p_0 = p_0 * 10000000


#        p_1 *= 100000000
#        p_0 *= 100000000
        #print p_0
        #print p_1
        #print "########"

    for j in compl_l:
        val = categorize(float(i[j]), j)
        sm = 0;

        if o_cnt[j][val][0] + o_cnt[j][val][1] == 0:
            print "WTF 2 "
            exit()

        for k in range(0, 100):
            sm += o_cnt[j][k][0]
        p_0 = p_0 * o_cnt[j][val][0] / sm

        sm = 0;
        for k in range(0, 100):
            sm += o_cnt[j][k][1]
        p_1 = p_1 * o_cnt[j][val][1] / sm

        p_1 = p_1 * 10000000
        p_0 = p_0 * 10000000

        #print p_0
        #print p_1
        #print "########"

    act = int(i[13])
    if act == 0 and p_0 > p_1:
        correct = correct + 1

    if act > 0 and p_1 < p_0:
        correct = correct + 1

    total = total + 1

    print i[13] + " " + str(p_0) + " " + str(p_1)

print 1. * correct / total
