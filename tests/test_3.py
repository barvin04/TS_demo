''' demo '''
import os
import sys

sys.path.insert(0, os.getcwd())

from script import addition


def test_add():
    ''' demo '''
    subj = addition(2, 3)
    assert subj == 5
