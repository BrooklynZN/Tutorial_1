
import numpy
from matplotlib import pyplot as plt
    #Question 3
def pyvect(n): 
    #0 to n-1 will have n points.
    x=numpy.arange(0,n)
    #the largest value is n-1, so we have to divide by that
    x=0.5*x*numpy.pi/(n-1)
    return x

def integral_cos_simple(n):
    dx=numpy.pi/2/n
    vec=pyvect(n)
    tot=numpy.sum(numpy.cos(vec))
    return dx*tot
    #Question 5
def integral_cos_simpson(n):
    dx=numpy.pi/2/(n-1)*2
    vec=numpy.cos(pyvect(n))
    #(Question4 cont.)
    x_even=vec[2:-1:2]
    x_odd=vec[1:-1:2]
    #(Question 5 cont)
    tot=numpy.sum(x_even)/3+numpy.sum(x_odd)*2/3+vec[0]/6+vec[-1]/6
    return tot*dx
    
if __name__=='__main__':
    
    
    print 'answering problem 2'
    nelem=[11,31,101,301,1001,3001,10001,3001,100001]    
    for n in nelem:
        bad_int=integral_cos_simple(n)
        print 'simple integrator with ' + repr(n) + ' points has value ' + repr(bad_int)

    
    print 'answering problem 4'
    val=integral_cos_simpson(11)
    err=numpy.abs(val-1)
    print 'error on 11 points is ' + repr(err-1)
    for n in nelem:
        myerr=numpy.abs(integral_cos_simpson(n)-1)
        print 'simpsons error on ' + repr(n) + ' is ' + repr(err)

    #Question 6
    print 'answering problem 5'
    nelem=[11,31,101,301,1001,3001,10001,30001,100001]
    nelem=numpy.array(nelem)
    simpson_err=numpy.zeros(nelem.size)
    simple_err=numpy.zeros(nelem.size)
    for ii in range(nelem.size):
        n=nelem[ii]
        simpson_err[ii]=numpy.abs(integral_cos_simpson(n)-1)
        simple_err[ii]=numpy.abs(integral_cos_simple(n)-1)
    plt.plot(nelem,simple_err)
    plt.plot(nelem,simpson_err)
    ax=plt.gca()

    ax.set_yscale('log')
    ax.set_xscale('log')
plt.show()