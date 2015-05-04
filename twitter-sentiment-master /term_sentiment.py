"""
Assignment 1 Coursera 2013 - Introduction to Data Science

Computes the sentiment for the terms that do not appear in the file AFINN-111.txt
Example:

$ python term_sentiment.py AFINN-111.txt output_first_20.txt
jaja -0.125
paramore 0.142857142857
just -0.0454545454545
...
"""

from __future__ import division
import sys
import json


def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def score_tweet(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet)


def unknown_word_scores(tweet_file, scores):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return {word: score_tweet(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores}


if __name__ == '__main__':
    scores = read_scores(sent_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in unknown_word_scores(
                              tweet_file=sys.argv[2],
                              scores=scores).items())
