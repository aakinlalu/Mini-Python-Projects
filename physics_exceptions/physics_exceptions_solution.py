"""
Physics Exceptions
==================

In this exercise we have some functions that compute relativistic energy.

1. Modify the energy function to raise a NotImplemented error if the mass is 0
   and the speed is c, since this formula is not correct for massless
   particles.

2. Modify the energy function to raise ValueError exceptions for non-physical
   values of mass (non-positive values) and velocity (speed greater than or
   equal to c).

3. Modify the total energy function so that it ignores these exceptions and
   simply skips over any particles which are non-physical.  If there are
   non-physical values, warn the user.

"""

from warnings import warn

# speed of light in metres per second
c = 299792458.0

def energy(mass, velocity):
    """ Return the relativistic energy

    Parameters
    ----------
    mass:
        The mass of the object in kilograms.  This should be a non-negative
        quantity.

    velocity:
        The velocity of the object in m/s.  The absolute value of the velocity
        should be less than c.

    Returns
    -------

    energy:
        The energy of the object in Joules.

    """
    if mass == 0 and abs(velocity) == c:
        raise NotImplementedError("Massless particles not supported")
    if mass <= 0:
        raise ValueError("Non-physical value: mass must be non-negative")
    if abs(velocity) >= c:
        raise ValueError("Non-physical value: speed must be less than c")
    e = mass*c**2*(1/(1-(velocity/c)**2)**0.5 - 1)
    return e


def total_energy(particles):
    """ Return the totla reletivistic energy of a collection of particles.

    Parameters
    ----------
    particles:
        A set of (mass, velocity) tuples for each particle.

    Returns
    -------

    energy:
        The total energy of the system in Joules.

    """
    e = 0
    for m, v in particles:
        try:
            e += energy(m, v)
        except NotImplementedError:
            warn("Computing energy of a massless particle")
        except ValueError:
            warn("Computing energy of a non-physical particle")
    return e


if __name__ == "__main__":

    # Let's use our functions on a few particles

    # 1. a massless particle
    mass = 0
    velocity = c

    try:
        print "The energy is:", energy(mass, velocity)
    except NotImplementedError as exc:
        print exc

    # 2. some non-physical values
    mass = -1
    velocity = 3e12

    try:
        print "The energy is:", energy(mass, velocity)
    except ValueError as exc:
        print exc

    # 3. a system with some non-physical particles

    particles = {(2, 20), (1, -10), (-1, 10), (0, c), (12, 3e12)}

    print "The total energy of the system is:", total_energy(particles)
