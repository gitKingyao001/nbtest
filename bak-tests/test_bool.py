#encoding=utf-8
from __future__ import unicode_literals, print_function, division
from nbtest.future2to3 import *

from nbtest.assertpyx import AX


def test_is_true():
    AX(True).is_true()
    AX(1 == 1).is_true()
    AX(1).is_true()
    AX('a中文').is_true()
    AX([1]).is_true()
    AX(['a中文']).is_true()
    AX({'a中文':1}).is_true()

def test_is_true_failure():
    try:
        AX(False).is_true()
        assert False, 'should have raised error'
    except AssertionError as ex:
        AX(str(ex)).ends_with('Expected <True>, but was not.')

def test_is_false():
    AX(False).is_false()
    AX(1 == 2).is_false()
    AX(0).is_false()
    AX([]).is_false()
    AX({}).is_false()
    AX(()).is_false()

def test_is_false_failure():
    try:
        AX(True).is_false()
        assert False, 'should have raised error'
    except AssertionError as ex:
        AX(str(ex)).ends_with('Expected <False>, but was not.')
