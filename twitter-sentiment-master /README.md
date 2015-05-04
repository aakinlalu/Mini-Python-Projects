twitter-sentiment
=================

Solution to Twitter Sentiment assignment in Introduction to Data Science(Coursera)


## Exercises 

1.  **Get Twitter Data:**
  Copy API credentials into the given **twitterstream.py** and run the following for 10 minutes:
  
  ```bash
    python twitterstream.py > output.txt
  ```
2.	**Derive the sentiment of each tweet:**
  Compute the sentiment of each tweet based on the sentiment scores of the terms in the
  tweet. Each word or phrase found in a tweet, but not in AFINN-111.txt should be given
  a sentiment score of 0.
  Example:
  
  ```bash
  $ python tweet_sentiment.py AFINN-111.txt output_first_20.txt
  0.0
  0.0
  0.0
  0.0
  0.0
  0.0
  -1.0
  ...
  ```
3.	**Derive the sentiment of new terms:**
  Computes the sentiment for the terms that do not appear in the file AFINN-111.txt
  Example:
  
  ```bash
  $ python term_sentiment.py AFINN-111.txt output_first_20.txt
  jaja -0.125
  paramore 0.142857142857
  just -0.0454545454545
  ...
  ```

4.	**Compute Term Frequency:**
  Print relative word frequency in a Twitter Stream file.
  Example:
  ```bash
  >>> python frequency.py output_first_20.txt
  jaja 0.00555555555556
  paramore 0.00555555555556
  just 0.00555555555556
  ...
  ```

5.	**Which State is happiest?:**
  Returns the code of the happiest state as a string. The average tweet
  happiness for each state is used as metric.
  Example:
  ```bash
  $ python happiest_state.py AFINN-111.txt output.txt
  KS
  ```

6.	**Top ten hash tags:**
  Computes the ten most frequently occurring hash tags from a tweet file.
  Example:
  ```bash
  $ python top_ten.py output.txt
  gameinsight 77.0
  TFBJP 65.0
  RT 53.0
  5DebilidadesMias 51.0
  ...
  ```
