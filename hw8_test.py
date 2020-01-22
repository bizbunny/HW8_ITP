>>> from hw8 import *

##### Problem 1 #####

Copy the following snippet to the top of your hw8.py file:

"""
class Polygon:
    def __init__(self, sideLength):
        self.sideLength=sideLength
"""

Create two classes that inherit the Polygon class, Square and Triangle. 
Square and Triangle should not have custom constructors, they will default to using Polygon's constructor.
Add methods perimeter() and area() to each class, that return the perimeter and area, respectively.

NOTE: The area of an equilateral triangle is (sideLength**2 * math.sqrt(3) / 4)

>>> sq = Square(10)
>>> issubclass(Square, Polygon) # this confirms you've set up inheritance correctly
True
>>> sq.area()
100
>>> sq.perimeter()
40
>>> tr = Triangle(10)
>>> isinstance(tr, Polygon) # this confirms you've set up inheritance correctly
True
>>> a=tr.area() #a should be roughly 43.301270189
>>> a>=43.30127 and a<=43.30128 #I'm doing this to avoid float rounding discrepancies
True
>>> tr.perimeter()
30



##### Problem 2 #####

##2a##
Create a class Player that takes in required fields name, jersey number, and city code in which they play.

>>> p1 = Player('Lebron James', 23, 'LA')
>>> p1.name=='Lebron James' and p1.jerseyNumber==23 and p1.cityCode=='LA'
True


##2b##
Create a class BasketballPlayer that takes in additional required fields pointsPerGame and reboundsPerGame.
Create a class BaseballPlayer that takes in additional required fields battingAverage and runsBattedIn.
Use the superclass constructor inside each constructor so we don't have to repeat ourselves.
Add the appropriate special method to each class to display the player's stats as shown below.

>>> bsk1 = BasketballPlayer('Lebron James', 23, 'LA', 27.2, 7.4)
>>> bsk1.name=='Lebron James' and bsk1.pointsPerGame==27.2
True
>>> print(bsk1)
Number 23 Lebron James scores 27.2 points per game and grabs 7.4 rebounds per game for LA.
>>> bsb1 = BaseballPlayer('Anthony Rizzo', 44, 'CHI', 0.293, 94)
>>> bsb1.name=='Anthony Rizzo' and bsb1.battingAverage==.293 and bsb1.runsBattedIn==94
True
>>> print(bsb1)
Number 44 Anthony Rizzo has a 0.293 batting average and 94 runs batted in for CHI.


##2c##
We want to add a method that will print every player located in the same city code as a given basketball or baseball player.
Since we want it for both classes, we can just add it to the Player class so all basketball/baseball players will inherit it.
Add a method printWithSameCityCode() to Player to print the name of every player in a list that plays in the same city.

>>> players = [BaseballPlayer('Mike Trout', 27, 'LA', .291, 104), BaseballPlayer('Yoan Moncada', 10, 'CHI', .315, 79), \
... BasketballPlayer('Blake Griffin', 23, 'DET', 21.9, 9.0), BasketballPlayer('Michael Jordan', 23, 'CHI', 30.1, 6.2), \
... BasketballPlayer('Jerry West', 44, 'LA', 27.0, 5.8)]
>>> bsk1.printWithSameCityCode(players)
Mike Trout
Jerry West
>>> bsb1.printWithSameCityCode(players)
Yoan Moncada
Michael Jordan


##2d##
Repeat the functionality of 2c but with Jersey number. We can add it to Player in the same way, so all subclasses can inherit the method.

>>> bsk1.printWithSameJerseyNumber(players)
Blake Griffin
Michael Jordan
>>> bsb1.printWithSameJerseyNumber(players)
Jerry West
