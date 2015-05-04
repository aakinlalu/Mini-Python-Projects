
# Image Processing Exercise
# =========================
# 
# In this exercise we'll use fancy indexing to perform basic image manipulation using multi-dimensional fancy indexing.
# 
# Let's start by reading in the "dc_metro" image:


from scipy.misc.pilutil import imread
from pylab import imshow, gray

# 'flatten' creates a 2D array from a JPEG.
img = imread('dc_metro.JPG', flatten=True)

# quickly view the image
gray()

# use vmin, vmax for full range of values
imshow(img, vmin=0, vmax=255)


# Question 1
# ----------
# 
# Create a sub-image by extracting the set of pixels in the rectangle from 100 to 200 vertically and 300 to 400 horizontally.


# your code goes here



# use 'nearest' interpolation to see pixels clearly
imshow(subimage, interpolation='nearest', vmin=0, vmax=255)


# Question 2
# ----------
# 
# The image is a grayscale image with values ranging from 0 (black) to 255 (white).
# 
# Use the `fill()` method on the subimage to replace every pixel in the sub-image with a medium gray (value 128).
# 
# What does the original image look like now?


# your code goes here



imshow(img, vmin=0, vmax=255)


# Question 3
# ----------
# 
# A simple way to downsample data is to select every `n`th pixel from an image.
# 
# Create a downsampled image from the original image by selecting every 8th pixel horizontally and vertically.


# your code goes here



imshow(downsampled, interpolation='nearest', vmin=0, vmax=255)


# Question 4
# ----------
# 
# Now create a mask of all the points where the value of the image is less than 128, and plot it.


# your code goes here



imshow(mask)


# Question 5
# ----------
# 
# Now extract the values in the image from that mask into an array. Plot a histogram of the values:


# your code goes here



hist(values)


# Question 6
# ----------
# 
# One of the more powerful features that fancy indexing provides is the ability to assign into a slice.  For example:
# 
#     img[mask] = 128
# 


img[mask] = 128
imshow(img, vmin=0, vmax=255)


# would turn every point in the original image where the mask is true to a medium gray.  You can also assign an array to the masked values as long as the shapes are compatible.
# 
# For every masked value in the original array, replace it with twice its value.

# Hint:


# your code goes here



imshow(img, vmin=0, vmax=255)

