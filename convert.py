#!/usr/bin/python

from math import e
import sys
import struct
import numpy as np
from os.path import join

# Based on the preprocessing in https://github.com/FALCONN-LIB/FALCONN

words = list()
matrix = list()

with open(join("dataset", "glove.6B.300d.txt"), "r", encoding="utf8") as data:
    for counter, line in enumerate(data):
        word, *rest = line.split()
        words.append(word)
        row = list(map(float, rest))
        matrix.append(np.array(row, dtype=np.float32))
        if counter % 5000 == 0:
            print(f"{counter} points processed...\n")

np.save(join("dataset", "glove.6B.300d"), np.array(matrix))

with open(join("dataset", "words"), "w", encoding="utf8") as data:
    data.write("\n".join(words))
