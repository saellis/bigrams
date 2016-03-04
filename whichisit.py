import re
import os
import sys
import math
import numpy as np
from collections import defaultdict

punc_pattern = re.compile('[\w\d\s]')


def main(*args):
    trained = [train(x) for x in [punc_replace(t) for t in args]]
    punc_sent = punc_pattern.sub('', raw_input('Paste a sentence from your favorite book: '))
    perplexities = [perplexity(punc_sent, trainfile) for trainfile in trained]
    print 'This is probably from', args[perplexities.index(max(perplexities))][:-3]


def perplexity(sent, dist):
    sum = 0
    for bigram in zip(sent, sent[1:]):
        try:
            sum += math.log(2, dist[bigram])
        except:  # the punctuation bigram was never seen in this book.
            sum += np.inf
    return -sum


def train(text):
    dist = defaultdict(int)
    for bigram in zip(text, text[1:]):
        dist[bigram] += 1
    N = sum(dist.values())
    new_dist = defaultdict(float)
    for bigram in dist.keys():
        new_dist[bigram] = float(dist[bigram]) / N
    return new_dist


def punc_replace(filename):
    with open(filename, 'r') as f:
        return ''.join([punc_pattern.sub('', line) for line in f])
            

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
