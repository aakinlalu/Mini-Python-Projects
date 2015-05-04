""" 
Write a module called "rockphysics" that has a single
function called "ggg" that calculates bulk density (rhob)
from P-wave velocity (vp) using the Garnder, Gardner, 
Gregory relationship::

    rhob = 1.741*vp**0.25
    
Import that module into this module and use the ggg 
function to:

1. Calculate rhob if vp=2.0
2. Calculate rhob for all the values::
    
        vp = [1.9, 2.0, 2.5, 2.1]
   
"""

# Import the module [Use rockphysics in your example].
#import rockphysics
import rockphysics_solution as rockphysics

# 1. Calculate rhob for vp=2.0
vp = 2.0 # km/s
rhob = rockphysics.ggg(vp)

print 'Gardner, Gardner, Gregory vp->rhob:'
print 'vp (km/s):', vp
print 'rhob (g/cc):', rhob

# 2. Calculate rhob for a list of vp values.
# Use a list comprehension to create a rhob list.
# Note: This is not how we'll do this in "real life."
#       Instead, we'll use numpy arrays [more on those later].
vp = [1.9, 2.0, 2.5, 2.1]
rhob = [rockphysics.ggg(x) for x in vp]
print 'Gardner, Gardner, Gregory vp->rhob:'
for vp_, rhob_ in zip(vp, rhob):
    print '%3.2f->%3.2f:' % (vp_, rhob_)
