from math_series import  __version__
 
def test_version():
    assert __version__ == '0.1.0'

# i will import the functions that i will test it 
from math_series.series import *

 #fibonacci_tests#

def test_fibonacci_0 ():
    assert (fibonacci(0)==[0])

def  test_fibonacci_1():
    actual=fibonacci(1)
    expected=[1]
    assert actual==expected

def test_fibonacci_2():
    actual=fibonacci(2)
    expected=[0,1]
    assert actual==expected

def test_fibonacci_3():
    assert(fibonacci(3)==[0,1,1])

def test_fibonacci_7():
    assert(fibonacci(7)==[0,1,1,2,3,5,8])



 
#lucos_tests
def test_lucos_0():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_lucos_1():
    actual=lucas(1)
    expected=1
    assert actual==expected

def test_lucos_7():
     actual=lucas(7)
     expected=29
     assert actual==expected
 
def test_lucos_11():
     actual=lucas(11)
     expected=199
     assert actual==expected
#sum_series_tests
def test_sum_series_2():
     actual=sum_series(12,2,1)
     expected=322
     assert actual==expected

def test_sum_3():
    actual=sum_series(8,4,6)
    expected=178
    assert actual==expected


def test_sum_series_4():
 actual=sum_series(4)
 expected=3
 assert actual==expected

 
def test_sum_series_3_parameters():
 actual=sum_series(10,2,1)
 expected=123
 assert actual==expected

 
def test_sum_series_2_3_parameters():
 actual=sum_series(10,0,1)
 expected=55
 assert actual==expected
