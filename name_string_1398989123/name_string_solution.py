
# Name String
# ===========
# 
# We would like to create a custom welcome message for a future application  that greats the user using his/her name. 
# 
# Question 1
# ----------
# Create a string with your first name  and assign it to a variable 'fst_name'.


fst_name = "Eric"


# Question 2
# ----------
# Create another one with your last name and assign it to a variable  'last_name'. 


last_name = "Jones"


# Question 3
# ----------
# Print a third string made of the concatenation of "Hello ", and the two  variables above.


print "Hello " + fst_name + " " + last_name


# Question 4
# ----------
# Now print a string full of the character "=" to underline the previous output. For example, if your name is Eric Jones, your welcome message is 
# 
#     
#     Hello Eric Jones 
# 
# so you should then print 16 occurences of "=". 
# 
# Note: Your code should work with any name (in other words, you can't assume that you can count the length of the name).

# Hint: The number of characters needed is the length of "Hello ", the length of the first name, the length of the last name, plus 1 more for the space in between.


# The number of characters needed is the length of "Hello ", the first name, the last name, and the space in between.
number_char = len("Hello ") + len(fst_name) + 1 + len(last_name)
print "=" * number_char

