from .base import Point, PointError, Station


class TestPoint:

    def test_creation(self):
        Station("../stations.json")

    def test_minSquare(self):
        min = Station("../stations.json").minSquare()
        print("Smallest square: ", min)
        return min


test_point = TestPoint
test_point.test_minSquare(test_point)
