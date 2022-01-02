#!/usr/bin/python

from math import e
import sys
import struct
import numpy as np
from os.path import join

# Based on the preprocessing in https://github.com/FALCONN-LIB/FALCONN

matrix = []
words = []
with open(join('dataset','glove.6B.300d.txt'), 'r', encoding='utf8') as inf:
    for counter, line in enumerate(inf):
        word, *rest = line.split()
        words.append(word)
        row = list(map(float, rest))
        assert len(row) == 300
        matrix.append(np.array(row, dtype=np.float32))
        if counter % 10000 == 0:
            sys.stdout.write('%d points processed...\n' % counter)

np.save(join('dataset','glove.6B.300d'), np.array(matrix))

with open(join('dataset','words'), 'w', encoding='utf8') as ouf:
    ouf.write('\n'.join(words))
