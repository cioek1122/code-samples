'''
Program: Rational.py
Author: Korey Cioe
Date: 2/12/2022

An ADT implementaion of a rational (real) number.
Demonstrates operator overloading
'''

class Rational(object):

    def __init__(self, num = 0, den = 1):

        '''creates a new Rational object
        pre: num and den are integers
        post: creates the Rational object num / den'''
        
        self.num = num           
        self.den = den


    def __mul__(self, other):       

        '''* operator
        pre: self and other are Rational objects
        post: returns Rational product: self * other'''

        num = self.num * other.num      #multiplies both numerators
        den = self.den * other.den      #multiplies both denominators
        return Rational(num, den)       #returns num and den

                
    def __str__(self):

        '''return string for printing
        pre: self is Rational object
        post: returns a string representation self'''
        
        return str(self.num) + '/' + str(self.den)  # returns num and den as string


    def __add__(self, other):

        '''adds two fractions
        pre: self and other must be rational objects
        post: returns self + other'''

        num = self.num * other.den + self.den * other.num       #multiply opposite numerators and denominators then adds them together
        den = self.den * other.den                              # multiplies both denominators
        return Rational(num, den)                               #returns num and den

    def __sub__(self, other):

        '''adds two fractions
        pre: self and other must be rational objects
        post: returns self + other'''

        num = self.num * other.den - other.num * self.den   #multiply opposite numerators and denominators then subtracts them
        den = self.den * other.den                          #multiplies both denominators
        return Rational(num, den)                           #returns num and den

    def __truediv__(self, other):

        '''adds two fractions
        pre: self and other must be rational objects
        post: returns self + other'''

        num = self.num * other.den      #multiply self num by other den
        den = self.den * other.num      #multiply oself den by other num
        return Rational(num, den)       #returns num and den 

    def __lt__(self, other):

        '''compares two fractions saying that one is less than the other
        pre: self and other must be rational objects
        post: returns self < other'''

        num_1 = self.num * other.den    #multiply self num by other den
        num_2 = other.num * self.den    #multiply oself den by other num
        return num_1 < num_2            #returns both fractions and sets 1 < 2

    def __gt__(self, other):

        '''compares two fracti0ns saying that one is greater than the other
        pre: self and other must be rational objects
        post: returns self < other'''

        num_1 = self.num * other.den    #multiply self num by other den
        num_2 = other.num * self.den    #multiply oself den by other num
        return num_1 > num_2            #returns both fractions and sets 1 > 2


    def __le__(self, other):

        '''compares that two fractions are less than or equal
        pre: self and other must be rational objects
        post: returns self <= other'''

        num_1 = self.num * other.den    #multiply self num by other den
        num_2 = other.num * self.den    #multiply oself den by other num
        return num_1 <= num_2           #returns both fractions and sets 1 <= 2


    def __ge__(self, other):

        '''compares that two fractions are greater than or equal
        pre: self and other must be rational objects
        post: returns self >= other'''

        num_1 = self.num * other.den    #multiply self num by other den
        num_2 = other.num * self.den    #multiply oself den by other num
        return num_1 >= num_2           #returns both fractions and sets 1 >= 2


    def __eq__(self, other):

        '''compares that two fractions are equal
        pre: self and other must be rational objects
        post: returns self == other'''

        num_1 = self.num * other.den    #multiply self num by other den
        num_2 = other.num * self.den    #multiply oself den by other num
        return num_1 == num_2           #returns both fractions and sets 1 == 2

    
    def __ne__(self, other):

        '''compares that two fractions are not equal
        pre: self and other must be rational objects
        post: returns self != other'''

        num_1 = self.num * other.den    #multiply self num by other den
        num_2 = other.num * self.den    #multiply oself den by other num
        return num_1 != num_2           #returns both fractions and sets 1 != 2


