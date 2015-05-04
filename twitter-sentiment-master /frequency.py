"""
Assignment 1 Coursera 2013 - Introduction to Data Science

Print relative word frequency in a Twitter Stream file.
Example:

>>> python frequency.py output_first_20.txt
jaja 0.00555555555556
paramore 0.00555555555556
just 0.00555555555556
...
"""

from __future__ import division
import sys
import json
from collections import Counter


def frequency(tweet_file):
    "string -> dict"
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return Counter(word for tweet in tweets for word in tweet)


if __name__ == '__main__':
    frecuencies = frequency(tweet_file=sys.argv[1])
    total = sum(frecuencies.values())
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), frecuencies[word] / total)
                          for word in frecuencies)
