def ggg(vp, scale=1.741, exponent=0.25):
    """ Calculate bulk density (rhob) from P-wave velocity (vp).
    
        This function uses an empirical relationship developed by
        Gardner, Gardner, and Gregory.  The default relationship
        is given by:
        
            rhob = 1.741*vp**.25
        
        where vp is in km/s and rhob is in g/cc.  The scale factor (1.741) 
        and the exponent (0.25) can be modified using key word arguments.
        
        Ref: Gardner, G. H. F., L. W. Gardner, and A. R. Gregory, 1974.
             Formation velocity and density: the diagnostic basics for
             stratigraphic maps, Geophysics 39:270-80.
    """
    rhob = scale*vp**exponent    
    return rhob