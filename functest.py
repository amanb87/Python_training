import astroscrappy
from astropy.io import fits

def a_test(*args):        
    path = args[0]   
    s = fits.getdata(path)
    a = astroscrappy.detect_cosmics(s)
    return [a,path]