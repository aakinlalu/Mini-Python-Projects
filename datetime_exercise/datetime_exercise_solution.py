"""
Datetime Exercise
-----------------

The file `dow2008.csv` has the following columns (separated by
commas).

DATE        OPEN      HIGH      LOW       CLOSE     VOLUME      ADJ_CLOSE
2008-01-02  13261.82  13338.23  12969.42  13043.96  3452650000  13043.96
2008-01-03  13044.12  13197.43  12968.44  13056.72  3429500000  13056.72
2008-01-04  13046.56  13049.65  12740.51  12800.18  4166000000  12800.18
2008-01-07  12801.15  12984.95  12640.44  12827.49  4221260000  12827.49
2008-01-08  12820.9   12998.11  12511.03  12589.07  4705390000  12589.07
2008-01-09  12590.21  12814.97  12431.53  12735.31  5351030000  12735.31

1. Read this file in, using the datetime module to parse the dates.

2. Print out date and volume for the Monday which has the highest volume
   in the data set.

"""

import datetime

data = []

with open('dow2008.csv') as fp:
    fp.readline()
    for row in fp:
        values = row.strip().split(',')
        data.append({
            'date': datetime.datetime.strptime(values[0], "%Y-%m-%d"),
            'open': float(values[1]),
            'high': float(values[2]),
            'low': float(values[3]),
            'close': float(values[4]),
            'volume': float(values[5]),
            'adj_close': float(values[6])
        })

print data

max_date = None
max_volume = 0
for row in data:
    date = row['date']
    if date.weekday() == 0: # monday
        volume = row['volume']
        if max_volume < volume:
            max_volume = volume
            max_date = date

print "The Monday with the highest volume is:"
print max_date.strftime("%Y-%m-%d")
print "The volume is:"
print max_volume
    
