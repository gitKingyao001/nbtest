#encoding=utf-8
from __future__ import unicode_literals, print_function, division
from nbtest.future2to3 import *

from nbtest.assertpyx import AX


def test_is_equal():
    AX('foo').is_equal_to('foo')
    AX(123).is_equal_to(123)
    AX(0.11).is_equal_to(0.11)
    AX(['a中文','b']).is_equal_to(['a中文','b'])
    AX((1,2,3)).is_equal_to((1,2,3))
    AX(1 == 1).is_equal_to(True)
    AX(1 == 2).is_equal_to(False)
    AX(set(['a中文','b'])).is_equal_to(set(['b','a中文']))
    AX({ 'a':1,'b':2 }).is_equal_to({ 'b':2,'a':1 })

def test_is_equal_failure():
    try:
        AX('foo').is_equal_to('bar')
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str_fmt(ex)).ends_with('Expected <foo> to be equal to <bar>, but was not.')

def test_is_equal_int_failure():
    try:
        AX(123).is_equal_to(234)
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str_fmt(ex)).ends_with('Expected <123> to be equal to <234>, but was not.')

def test_is_equal_list_failure():
    try:
        AX(['a中文','b']).is_equal_to(['a中文','b','c'])
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str_fmt(ex)).ends_with(b"Expected <[u'a\u4e2d\u6587', u'b']> to be equal to <[u'a\u4e2d\u6587', u'b', u'c']>, but was not.")

def test_is_not_equal():
    AX('foo').is_not_equal_to('bar')
    AX(123).is_not_equal_to(234)
    AX(0.11).is_not_equal_to(0.12)
    AX(['a中文','b']).is_not_equal_to(['a中文','x'])
    AX(['a中文','b']).is_not_equal_to(['a'])
    AX(['a中文','b']).is_not_equal_to(['a中文','b','c'])
    AX((1,2,3)).is_not_equal_to((1,2))
    AX(1 == 1).is_not_equal_to(False)
    AX(1 == 2).is_not_equal_to(True)
    AX(set(['a中文','b'])).is_not_equal_to(set(['a']))
    AX({ 'a':1,'b':2 }).is_not_equal_to({ 'a':1,'b':3 })
    AX({ 'a':1,'b':2 }).is_not_equal_to({ 'a':1,'c':2 })

def test_is_not_equal_failure():
    try:
        AX('foo').is_not_equal_to('foo')
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str_fmt(ex)).ends_with('Expected <foo> to be not equal to <foo>, but was.')

def test_is_not_equal_int_failure():
    try:
        AX(123).is_not_equal_to(123)
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str_fmt(ex)).ends_with('Expected <123> to be not equal to <123>, but was.')

def test_is_not_equal_list_failure():
    try:
        AX(['a中文','b']).is_not_equal_to(['a中文','b'])
        assert False, ('should have raised error')
    except AssertionError as ex:
        ex_fmt = str_fmt(ex)
        AX(str_fmt(ex)).ends_with(b"Expected <[u'a\u4e2d\u6587', u'b']> to be not equal to <[u'a\u4e2d\u6587', u'b']>, but was.")
