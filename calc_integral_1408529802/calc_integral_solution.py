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

See :ref:`calc-derivative-solution`.
"""

from numpy import linspace, pi, sin, cos, cumsum
from pylab import plot, show, legend, suptitle

# calculate the sin() function on evenly spaced data.
x = linspace(0, 2*pi, 101)
y = sin(x)

# calculate the derivative dy/dx numerically.
# First, calculate the distance between adjacent pairs of
# x values.
dx = x[1:]-x[:-1]

# Trapezoidal rule integration.
avg_height = (y[1:]+y[:-1])/2.0
int_sin = cumsum(dx * avg_height)

# Plot our numeric integration against the closed form solution:
#     1 - cos(x)
closed_form = 1 - cos(x)
plot(x[1:], int_sin,'rx', x, closed_form,'b-')
legend(('numerical', 'actual'))
suptitle(r"$\int \, \sin(x) \, dx$")
show()

