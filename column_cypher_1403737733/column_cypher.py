
# Column Cypher
# =============
# 
# A column cipher works by writing the message in rows of a fixed length, and
# then extracting the columns and concatenating them.  So the message
# "THISISACOLUMNCYPHER" with rows of length 5, would be written::
# 
#     THISI
#     SACOL
#     UMNCY
#     PHERX
# 
# and then be sent as "TSUPHAMHICNESOCRILYX".  Note that you want to
# pad the message with extra characters to make it a multiple of the number of
# columns.
# 
# In this exercise we will use numpy multidimensional arrays to encode a message as a column cypher.


message = "THISMESSAGEISVERYSECRETX"


# Question 1
# ----------
# 
# Convert the variable `message` to a numpy array of characters.

# Hint: You will want to convert it to a list of characters first.


# your code goes here



print message_array


# Question 2
# ----------
# 
# We want to create a column cypher with 3 columns.  Change the shape of the array to be Nx3.

# Hint: You could compute the value of N, but you can also use a shape of `(-1, 3)`.


N = message_array.size/3
message_array.shape = (N, 3)



print message_array


# Question 3
# ----------
# 
# The `transpose` function transposes a 2d array so that rows become columns and columns become rows.  Transpose the message_array.


# your code goes here



print transposed_message


# Question 4
# ----------
# 
# Use array indexing to get the first row of the transposed array.  Convert the first row back to a string.

# You can use `''.join()` with arrays of characters in exactly the same way as with lists of strings.


# your code goes here


# Question 5
# ----------
# 
# Loop over the rows of the transposed message and to build the encoded string.


# your code goes here



print encoded_message

