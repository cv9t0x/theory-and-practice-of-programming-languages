from xmlrpc.client import MAXINT
import json


class PointError(Exception):
    ...


class Point:

    def __init__(self, x: float, y: float) -> None:
        if not isinstance(x, float) or not isinstance(y, float):
            raise PointError("x should be float")
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            if hasattr(other, "__iter__"):
                return self == Point(*other)
            else:
                raise NotImplementedError
        return self.x == other.x and self.y == other.y

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def to_json(self) -> str:
        return json.dumps({"x": self.x, "y": self.y})

    @classmethod
    def from_json(cls, f: dict) -> "Point":
        if "lat" not in f['location'] and "lon" in f['location']:
            return cls(0.0, float(f["location"]["lon"]))
        elif "lat" in f['location'] and "lon" not in f['location']:
            return cls(float(f["location"]["lat"], 0.0))
        else:
            return cls(float(f["location"]["lat"]), float(f["location"]["lon"]))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}"

    def is_center(self: "Point") -> bool:
        return self == Point(0, 0)


class Station:
    def __init__(self, station: str):
        self.arr = []

        with open(station) as f:
            f = json.load(f)
        for i in f:
            self.arr.append(Point.from_json(i))

    def minSquare(self):
        min = MAXINT

        for i in range(len(self.arr) - 2):
            for j in range(i + 1, len(self.arr) - 1):
                for k in range(j + 1, len(self.arr)):
                    a = Point(self.arr[i].x, self.arr[i].y).distance_to(
                        Point(self.arr[j].x, self.arr[j].y))
                    b = Point(self.arr[j].x, self.arr[j].y).distance_to(
                        Point(self.arr[k].x, self.arr[k].y))
                    c = Point(self.arr[k].x, self.arr[k].y).distance_to(
                        Point(self.arr[i].x, self.arr[i].y))
                    p = (a + b + c) / 2
                    Square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                    if Square < min:
                        min = Square
        return
