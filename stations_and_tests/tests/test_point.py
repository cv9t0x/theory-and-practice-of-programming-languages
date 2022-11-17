from plib import Station, Point
import pytest


class TestPoint:

    def test_creation(self):
        Station("../stations.json")

    def test_minSquare(self):
        return Station("../stations.json").minSquare() == 9.382093856738155e-07
