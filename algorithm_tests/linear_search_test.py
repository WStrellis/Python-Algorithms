from algorithms.linear_search import linear_search
import pytest


class TestLinearSearch:
    def setup_method(self, method):
        self.test_list = [10, 56, 496, 334, 98, 105]

    def test_1(self):
        assert linear_search(56) == 56

    def test_2(self):
        assert linear_search(1) == None
