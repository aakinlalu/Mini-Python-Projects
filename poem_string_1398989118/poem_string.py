
# The Haggis poem
# ===============
# 
# Despite the number of snakes that are used on books, websites and package names, the `Python` language was named after the British comedy group Monty Python. Part of their `Big Red Book` was a poem called `The Haggis poem` that we will "analyze".
# 
# Copy the text below (only the first half of the poem) and use it to create a string containing the following poem in a variable called `poem`:
# 
# <pre>
# Jack
# Much to his Mum and Dad's dismay
# Jack ate himself one day.
# He didn't stop to say his grace,
# He just sat down and ate his face.
# "We can't have this his Dad declared,
# "If that lad's ate, he should be shared."
# But even as he spoke they saw
# Jack eating more and more:
# First his legs and then his thighs,
# His arms, his nose, his hair, his eyes...
# "Stop him someone!" Mother cried
# "Those eyeballs would be better fried!"
# </pre>


def change(poem):
     total = 0
     
     with open(poem) as f:
         for line in f:
              if 'Jack' in line:
                  total += 1
              line.replace('Jack', "Horace")
              print line
         return total


# The name in this version of the poem is wrong and all occurences of "Jack" should be replaced by "Horace". First, count how many occurences of "Jack" there are and find where (at what character) the first occurence happens. Then modify the variable `poem` by replacing them all at once by "Horace". Print the result.


# your code goes here

