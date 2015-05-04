"""
Assignment 1 Coursera 2013 - Introduction to Data Science

Compute the sentiment of each tweet based on the sentiment scores of the terms in the
tweet. Each word or phrase found in a tweet, but not in AFINN-111.txt should be given
a sentiment score of 0.
Example:

$ python tweet_sentiment.py AFINN-111.txt output_first_20.txt
0.0
0.0
0.0
0.0
0.0
0.0
-1.0
...
"""
import sys
import json


def read_scores(sent_file):
    "Parse sentiment file, returns a {word: sentiment} dict"
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def tweet_score(tweet, scores):
    "Returns the score for a tweet or 0 if it's not in AFINN-111.txt"
    return sum(scores.get(word, 0) for word in tweet.split())


def tweet_scores(tweet_file, scores):
    "Calculate scores for all tweets in tweet_file"
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '') for line in f)
        return [tweet_score(tweet, scores) for tweet in tweets]


if __name__ == '__main__':
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = read_scores(sent_file=sent_file)
    sys.stdout.writelines('{0}.0\n'.format(score)
                          for score in tweet_scores(tweet_file=tweet_file, scores=scores))






# import sys

# def hw():
#     print 'Hello, world!'

# def lines(fp):
#     print str(len(fp.readlines()))

# def main():
#     sent_file = open(sys.argv[1])
#     tweet_file = open(sys.argv[2])
#     hw()
#     lines(sent_file)
#     lines(tweet_file)

# if __name__ == '__main__':
#     main()
