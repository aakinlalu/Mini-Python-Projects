"""
Dow Database
-------------

This exercise covers with interacting with SQL databases from Python using
the DB-API 2.0 interface. It will require for you to write a few basic SQL
instructions. Take the time to refresh on them if you haven't written SQL
commands in a while. Feel free to refer to http://www.sqlcourse.com/ or search
for other resources.


The database table in the file 'dow2008.csv' has records holding the
daily performance of the Dow Jones Industrial Average from the
beginning of 2008.  The table has the following columns (separated by
a comma).

DATE        OPEN      HIGH      LOW       CLOSE     VOLUME      ADJ_CLOSE
2008-01-02  13261.82  13338.23  12969.42  13043.96  3452650000  13043.96
2008-01-03  13044.12  13197.43  12968.44  13056.72  3429500000  13056.72
2008-01-04  13046.56  13049.65  12740.51  12800.18  4166000000  12800.18
2008-01-07  12801.15  12984.95  12640.44  12827.49  4221260000  12827.49
2008-01-08  12820.9   12998.11  12511.03  12589.07  4705390000  12589.07
2008-01-09  12590.21  12814.97  12431.53  12735.31  5351030000  12735.31
...         ...       ...       ...       ...       ...         ...


1. Create a database table that has the same structure (use real
   for all the columns except the date column).

2. Insert all the records from dow.csv into the database.

3. Select (and print out) the records from the database that have a volume
   greater than 5.5 billion.   How many are there?

Bonus
~~~~~
1. Select the records which have a spread between high and low that is greater
   than 4% and sort them in order of that spread.

2. Select the records which have an absolute difference between open and close
   that is greater than 1% (of the open) and sort them in order of that spread.
"""
import sqlite3 as db

# 1. Create a database table that has the same structure (use real
#   for all the columns except the date column).

# We can either make that database in memory with the following or we could
# make it persistent by providing some filename my_db.db instead of :memory:
connection = db.connect(":memory:")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE dow (
    date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume FLOAT,
    adj_close FLOAT) """)
connection.commit()

# 2. Insert all the records from dow.csv into the database.

with open('dow2008.csv') as fp:
    fp.readline()
    for line in fp:
        values = line.strip().split(',')
        cursor.execute("INSERT INTO dow VALUES (?, ?, ?, ?, ?, ?, ?)", values)
connection.commit()

# 3. Select (and print out) the records from the database that have a volume
#   greater than 5.5 billion.   How many are there?

cursor.execute("SELECT * FROM dow WHERE volume > 5500000000")
print "The following entries have a volume above 5.5 billions."
for row in cursor:
    print row

cursor.execute("SELECT COUNT(*) FROM dow WHERE volume > 5500000000")
print "Number of entries:"
for row in cursor:
    print row

# Another way to answer this question with only 1 SQL query would be to use
# fechall to get a list of all the rows from the cursor and print the length of
# that list.
cursor.execute("SELECT * FROM dow WHERE volume > 5500000000")
all_results = cursor.fetchall()
print all_results
print len(all_results)

# Bonus 1: Records with a spread greater than 4%

sql = "SELECT * FROM dow WHERE (high-low)/low > ? ORDER BY (high-low)/low"
cursor.execute(sql, (0.04,))

print "The following entries have a spread above 4%."
N = 0
for row in cursor:
    print row
    N += 1
print "Bonus 1 number of rows: ", N

# Bonus 2: Records where absolute difference between open and close greater
# than 1% (of the open)

# The solution could be very very similar to the above question. Alternatively
# we show below executing the command directly on the connection object.
# That's a more compact way of querying if the cursor object isn't used.

# Since we won't use it anymore, let's close that cursor
cursor.close()

# Now on to our query:
sql = "SELECT * FROM dow WHERE abs(open-close)/open > ? ORDER BY abs(open-close)/open"

print "The following entries have a open-close different above 1%."
N = 0
for row in connection.execute(sql, (0.01,)):
    print row
    N += 1
print "Bonus 2 number of rows: ", N

connection.close()
