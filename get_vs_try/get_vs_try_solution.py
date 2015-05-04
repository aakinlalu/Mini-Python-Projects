
# Get vs. KeyError Exercise
# =========================
# 
# When you are using dictionaries, there are (at least) three ways that you can deal with missing keys:
# 
# * you can use the `get()` method and supply a default value to use if the key is missing
# * you can put a `try: ... except KeyError: ...` around your dictionary access
# * if you should never have a missing key in a correctly functioning script, you can ignore the possibility, and let the exception stop your code from running.
# 
# Which is the best strategy depends on your use case.  In this exercise, we'll investigate some of the advantages and disadvantages of each approach.
# 
# Question 1
# ----------
# 
# Write a function `get_a()` that takes a dictionary and returns the value associated with the key `"a"` using the `get()` dictionary method, returning `1` if there is no value associated with the key:
# 
#     def get_a(d):
#         ...


def get_a(d):
    return d.get("a", 1)


# Question 2
# ----------
# 
# Write a function `try_a()` which does the same as `get_a()`, but using a `try: ... except KeyError: ...` instead.
# 
#     def try_a(d):
#         ...
# 


def try_a(d):
    try:
        return d["a"]
    except KeyError:
        return 1


# Question 3
# ----------
# 
# Write a function `lookup_a()` which is the same as the previous two functions, but doesn't handle the case of a missing value at all.
# 
#     def lookup_a(d):
#         ...


def lookup_a(d):
    return d["a"]


# Question 4
# ----------
# 
# Use IPython's `%timeit` magic to see how long each function takes on the dictionary


d = {"a": 2}


# Time for `get_a()`:


get_ipython().magic(u'timeit get_a(d)')


# Time for `try_a()`:


get_ipython().magic(u'timeit try_a(d)')


# Time for `lookup_a()`:


get_ipython().magic(u'timeit lookup_a(d)')


# Question 5
# ----------
# 
# Repeat question 4 for `get_a()` and `try_a()` with the dictionary:


empty = {}


# Time for `get_a()`:


get_ipython().magic(u'timeit get_a(empty)')


# Time for `try_a()`:


get_ipython().magic(u'timeit try_a(empty)')


# Based on the results of questions 4 and 5, if speed is critical to your code:
# 
# * what is the best approach to use when you expect keys to be missing often?
# * what is the best approach to use when you expect keys to be missing infrequently?
# * what is the best approach to use when keys should never be missing?
# 
# If speed is not an issue, but keys may be missing, which approach would you prefer?
# 
# Bonus
# -----
# 
# In the `collections` module there is a class called `defaultdict` that provides another way of providing for missing keys:


from collections import defaultdict


# A `defaultdict` expects an argument which is a function which returns the default value for a missing key.  For example:


def default_1():
    return 1

example_defaultdict = defaultdict(default_1, a=2)

print example_defaultdict["a"]
print example_defaultdict["b"]


# Use IPython's `%timeit` with `lookup_a()` and this `example_defaultdict`:


get_ipython().magic(u'timeit lookup_a(example_defaultdict)')


# Create an empty defaultdict with the same default function:


empty_defaultdict = defaultdict(default_1)


# Repeat the timing with this:


get_ipython().magic(u'timeit lookup_a(empty_defaultdict)')


# Finally, if you do not supply a default value function, the `defaultdict` will behave similarly to a regular dictionary:


nodefault_defaultdict = defaultdict(a=2)

print nodefault_defaultdict["a"]



print nodefault_defaultdict["b"]


# Repeat the timing with `lookup_a` and this `defaultdict`.


get_ipython().magic(u'timeit lookup_a(nodefault_defaultdict)')


# Does this change your preferred approach in any of the scenarios mentioned in Question 5?
# 
# (Keep in mind the value of readability, particularly if speed is not the most important thing, and perhaps even if it is!)
