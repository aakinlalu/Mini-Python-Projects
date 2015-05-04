""" 
Calculate Integral
------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical integral for ``sin`` from 0 to `x`, for every value
in the `x` array below (0 to ``2*pi``) using Riemann sums or
the trapezoidal rule.  There is no need to use a 'for' loop for this.

Plot the resulting values and compare to the analytical integral
for this problem, ie. ``1-cos(x)``.

Hint: At the interactive prompt, type `cumsum?` as it is a function
      that is likely helpful.

See :ref:`calc-integral-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from pylab import plot, show, subplot, legend, suptitle

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)

plot(x,y)
show()

