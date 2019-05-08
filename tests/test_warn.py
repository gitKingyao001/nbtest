# Copyright (c) 2015-2018, Activision Publishing, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

from assertpy import assert_that, assert_warn, fail


def test_success():
    assert_warn('foo').is_length(3)
    assert_warn('foo').is_not_empty()
    assert_warn('foo').is_true()
    assert_warn('foo').is_alpha()
    assert_warn('123').is_digit()
    assert_warn('foo').is_lower()
    assert_warn('FOO').is_upper()
    assert_warn('foo').is_equal_to('foo')
    assert_warn('foo').is_not_equal_to('bar')
    assert_warn('foo').is_equal_to_ignoring_case('FOO')

def test_failures():
    if sys.version_info[0] == 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    # capture stdout
    old = sys.stdout
    sys.stdout = StringIO()

    assert_warn('foo').is_length(4)
    assert_warn('foo').is_empty()
    assert_warn('foo').is_false()
    assert_warn('foo').is_digit()
    assert_warn('123').is_alpha()
    assert_warn('foo').is_upper()
    assert_warn('FOO').is_lower()
    assert_warn('foo').is_equal_to('bar')
    assert_warn('foo').is_not_equal_to('foo')
    assert_warn('foo').is_equal_to_ignoring_case('BAR')

    # stop capturing stdout
    out = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = old

    assert_that(out).contains('Expected <foo> to be of length <4>, but was <3>.')
    assert_that(out).contains('Expected <foo> to be empty string, but was not.')
    assert_that(out).contains('Expected <False>, but was not.')
    assert_that(out).contains('Expected <foo> to contain only digits, but did not.')
    assert_that(out).contains('Expected <123> to contain only alphabetic chars, but did not.')
    assert_that(out).contains('Expected <foo> to contain only uppercase chars, but did not.')
    assert_that(out).contains('Expected <FOO> to contain only lowercase chars, but did not.')
    assert_that(out).contains('Expected <foo> to be equal to <bar>, but was not.')
    assert_that(out).contains('Expected <foo> to be not equal to <foo>, but was.')
    assert_that(out).contains('Expected <foo> to be case-insensitive equal to <BAR>, but was not.')

