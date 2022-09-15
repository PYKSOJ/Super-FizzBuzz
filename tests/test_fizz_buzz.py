from production.super_fizz_buzz import super_fizz_buzz

import unittest


class SuperFizzBuzzDevide3(unittest.TestCase):
    def test_give_true(self):
        num = 3
        test = super_fizz_buzz(num)
        self.assertEqual('Fizz', test, 'success')

    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('Fizz', test, 'fail')


class SuperFizzBuzzDevide5(unittest.TestCase):
    def test_give_true(self):
        num = 5
        test = super_fizz_buzz(num)
        self.assertEqual('Buzz', test, 'success')

    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('Buzz', test, 'fail')


class SuperFizzBuzzDevide9(unittest.TestCase):
    def test_give_true(self):
        num = 9
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizz', test, 'success')

    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizz', test, 'fail')


class SuperFizzBuzzDevide25(unittest.TestCase):
    def test_give_true(self):
        num = 25
        test = super_fizz_buzz(num)
        self.assertEqual('BuzzBuzz', test, 'success')

    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('BuzzBuzz', test, 'fail')


class SuperFizzBuzzDevide3and5(unittest.TestCase):
    def test_give_true(self):
        num = 15
        test = super_fizz_buzz(num)
        self.assertEqual('FizzBuzz', test, 'success')

    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('FizzBuzz', test, 'fail')


class SuperFizzBuzzDevide9and25(unittest.TestCase):
    def test_give_true(self):
        num = 225
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'success')

    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')


class SuperFizzBuzzNotmacthcase(unittest.TestCase):
    def test_give_true(self):
        num = 1
        test = super_fizz_buzz(num)
        self.assertEqual('NoFizzBuzz', test, 'success')
        
    def test_give_zero(self):
        num = 0
        test = super_fizz_buzz(num)
        self.assertEqual('NoFizzBuzz', test, 'fail' )

