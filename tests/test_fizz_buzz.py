from production.super_fizz_buzz import super_fizz_buzz

import unittest

class SuperFizzBuzzDevide3(unittest.TestCase):
    def test_give_true(self):
        num = 3
        test = super_fizz_buzz(num)
        self.assertEqual('Fizz', test, 'success' )

class SuperFizzBuzzDevide5(unittest.TestCase):
    def test_give_true(self):
        num = 5
        test = super_fizz_buzz(num)
        self.assertEqual('Buzz', test, 'success' )

class SuperFizzBuzzDevide9(unittest.TestCase):
    def test_give_true(self):
        num = 9
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizz', test, 'success' )

class SuperFizzBuzzDevide25(unittest.TestCase):
    def test_give_true(self):
        num = 25
        test = super_fizz_buzz(num)
        self.assertEqual('BuzzBuzz', test, 'success' )
        
class SuperFizzBuzzDevide3and5(unittest.TestCase):
    def test_give_true(self):
        num = 15
        test = super_fizz_buzz(num)
        self.assertEqual('FizzBuzz', test, 'success' )

class SuperFizzBuzzDevide9and25(unittest.TestCase):
    def test_give_true(self):
        num = 225
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'success' )

class SuperFizzBuzzNotmacthcase(unittest.TestCase):
    def test_give_true(self):
        num = 1
        test = super_fizz_buzz(num)
        self.assertEqual('NoFizzBuzz', test, 'success' )