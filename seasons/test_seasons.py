from seasons import *
import pytest

def test_total_time():
    assert total_time(7670) == "Eleven million, forty-four thousand, eight hundred minutes"
    assert total_time(15812)== "Twenty-two million, seven hundred sixty-nine thousand, two hundred eighty minutes"

def test_time():
    assert total_time(5612)== "Eight million, eighty-one thousand, two hundred eighty minutes"
