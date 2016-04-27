#!/bin/python2

import numpy as np
import sys

raw_data = {}

regions = ["ARB", "EAS", "EAP", "ECA", "EMU",
"ECS", "EUU", "HIC", "NOC", "OEC",
"HPC", "LDC", "LCN", "LAC", "MEA",
"OED", "PSS", "SSF", "SSA", "WLD"]

regions_number = len(regions)

def load_data():
    fdata = open("data")

    data = [line.rstrip('\n') for line in fdata]

    for reg in regions:
        raw_data[reg] = []

    for line in data:
        if len(line) < 1:
            break

        words = line.split(' ')

        raw_data[words[0]].append(words[1:])

    fdata.close()

def train_sample(sz):
    np.random.shuffle(train_set)
    return train_set[:sz][:]

def test_sample(sz):
    np.random.shuffle(test_set)
    return test_set[:sz][:]
