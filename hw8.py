# Hw 8
# Collaborator: Vi-Linh Nguyen
import math
from math import sqrt


# Problem 1
class Polygon:
    def __init__ (self, sideLength):
        self.sideLength = sideLength


class Square(Polygon):
    def perimeter (self):
        return (self.sideLength * 4)

    def area (self):
        return (self.sideLength ** 2)


class Triangle(Polygon):
    def perimeter (self):
        return (self.sideLength * 3)

    def area (self):
        return ((self.sideLength ** 2) * (math.sqrt(3) / 4))


# Problem 2
# 2A
class Player:
    def __init__ (self, name, jerseyNumber, cityCode):
        self.name = name
        self.jerseyNumber = jerseyNumber
        self.cityCode = cityCode

    # 2C
    def printWithSameCityCode (self, other):
        for i in other:
            if self.cityCode == i.cityCode:
                print(i.name)

    # 2D
    def printWithSameJerseyNumber (self, other):
        for j in other:
            if self.jerseyNumber == j.jerseyNumber:
                print(j.name)


# 2B
class BasketballPlayer(Player):
    def __init__ (self, name, jerseyNumber, cityCode, pointsPerGame, reboundsPerGame):
        super().__init__(name, jerseyNumber, cityCode)
        self.pointsPerGame = pointsPerGame
        self.reboundsPerGame = reboundsPerGame

    def __str__ (self):
        return (
            'Number {} {} scores {} points per game and grabs {} rebounds per game for {}.'.format(self.jerseyNumber,
                                                                                                   self.name,
                                                                                                   self.pointsPerGame,
                                                                                                   self.reboundsPerGame,
                                                                                                   self.cityCode))


class BaseballPlayer(Player):
    def __init__ (self, name, jerseyNumber, cityCode, battingAverage, runsBattedIn):
        super().__init__(name, jerseyNumber, cityCode)
        self.battingAverage = battingAverage
        self.runsBattedIn = runsBattedIn

    def __str__ (self):
        return (
            'Number {} {} has a {} batting average and {} runs batted in for {}.'.format(self.jerseyNumber, self.name,
                                                                                         self.battingAverage,
                                                                                         self.runsBattedIn,
                                                                                         self.cityCode))


if __name__ == "__main__":
    import doctest

    print(doctest.testfile('hw8_test.py', verbose=True))
