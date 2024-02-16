import pytest


@pytest.mark.smoke
def test_met1():
    assert 10+10 == 20

@pytest.mark.smoke
def test_met2():
    assert 2*2 == 4

@pytest.mark.regression
def test_met3():
    assert 5/5 ==1

@pytest.mark.regression
def test_met4():
    assert 20-10 == 10