import pytest
from principal import somar
from principal import subtrair

def test_somar():
    """docstring for test_somar"""
    assert somar(2,4) == 6

def test_subtrair():
    """docstring for test_somar"""
    assert subtrair(2,4) == -2

