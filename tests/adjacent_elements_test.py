from challenges.adjacent_elements import adjacentElementsProduct


class TestAdjacentElements:
    def test_1(self):
        assert adjacentElementsProduct([-23, 4, -3, 8, -12]) == -12

    def test_2(self):
        assert adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]) == 50

    def test_3(self):
        assert adjacentElementsProduct([1, 2, 3, 0]) == 6
