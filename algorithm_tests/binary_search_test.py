from algorithms.binary_search import binary_search
import pytest


class TestBinarySearch:
    def setup_method(self, method):
        self.test_list = [10, 56, 98, 105, 334, 496,
                          566, 589, 602, 661, 679, 843, 855, 900, 921]

    def test_1(self):
        assert binary_search(496, self.test_list) == 5

    def test_2(self):
        assert binary_search(1, self.test_list) == -1

    def test_3(self):
        assert binary_search(1, []) == -1

    def test_4(self):
        assert binary_search(1, [4]) == -1
