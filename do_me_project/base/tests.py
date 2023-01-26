from django.test import TestCase
from collections.abc import Mapping
import pytest


# Create your tests here.


def test_method():
    x = 5
    y = 6
    assert x + 1 == 6, 'test failed'
    assert y - 1 == 5, 'test failed'

def test_numbers():
    10 % 2 == 0, 'test failed'







