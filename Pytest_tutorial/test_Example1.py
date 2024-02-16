import pytest

@pytest.mark.regression
def test_t1():
    s="i am a automation tester"
    assert s.upper()=="I AM A AUTOMATION TESTER"

@pytest.mark.regression
def test_method2():

    a,b=10,10
    assert a+b==100

@pytest.mark.smoke
def test_t3():
    n,m=20,20
    assert n*m==400

@pytest.mark.smoke
def test_method4():
    h="HELLO"
    assert h.upper()=="HELLO"
