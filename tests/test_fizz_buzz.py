from src.super_fizz_buzz import super_fizz_buzz

import unittest


class SuperFizzBuzzDevide3(unittest.TestCase):

    def test_give_lowwest_bordery(self):
        num = 3
        test = super_fizz_buzz(num)
        self.assertEqual('Fizz', test, 'fail')

    def test_give_middle_bordery(self):
        num = 5001
        test = super_fizz_buzz(num)
        self.assertEqual('Fizz', test, 'fail')

    def test_give_highest_bordery(self):
        num = 9996
        test = super_fizz_buzz(num)
        self.assertEqual('Fizz', test, 'fail')


class SuperFizzBuzzDevide5(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 5
        test = super_fizz_buzz(num)
        self.assertEqual('Buzz', test, 'fail')


''' ในกรณีหารด้วย 5 ไม่สามารถเขียนในกรณีที่มากสุดของขชอบเขตข้อมูลนำเข้าได้
    เนื่องจากจำไปซำ้กดับการหารด้วย 25 ที่จะต้องได้ผลลัพธ์เป็นคำว่า BuzzBuzz
    '''


class SuperFizzBuzzDevide9(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 9
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizz', test, 'fail')

    def test_give_middle_bordery(self):
        num = 4986
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizz', test, 'fail')

    def test_give_highest_bordery(self):
        num = 9999
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizz', test, 'fail')


class SuperFizzBuzzDevide25(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 25
        test = super_fizz_buzz(num)
        self.assertEqual('BuzzBuzz', test, 'fail')

    def test_give_middle_bordery(self):
        num = 5000
        test = super_fizz_buzz(num)
        self.assertEqual('BuzzBuzz', test, 'fail')

    def test_give_highest_bordery(self):
        num = 10000
        test = super_fizz_buzz(num)
        self.assertEqual('BuzzBuzz', test, 'fail')


class SuperFizzBuzzDevide3and5(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 15
        test = super_fizz_buzz(num)
        self.assertEqual('FizzBuzz', test, 'fail')

    def test_give_middle_bordery(self):
        num = 5010
        test = super_fizz_buzz(num)
        self.assertEqual('FizzBuzz', test, 'fail')

    def test_give_highest_bordery(self):
        num = 9990
        test = super_fizz_buzz(num)
        self.assertEqual('FizzBuzz', test, 'fail')


class SuperFizzBuzzDevide9and25(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 225
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')

    def test_give_middle_bordery(self):    
        num = 5175
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')
        
    def test_give_highhest_bordery(self):
        num = 9900
        test = super_fizz_buzz(num)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')

class SuperFizzBuzzNotmacthcase(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        num = 1
        test = super_fizz_buzz(num)
        self.assertEqual('NoFizzBuzz', test, 'fail')
    def test_give_middle_bordery(self):
        num = 5002
        test = super_fizz_buzz(num)
        self.assertEqual('NoFizzBuzz', test, 'fail')
    def test_give_highhest_bordery(self):
        num = 9998
        test = super_fizz_buzz(num)
        self.assertEqual('NoFizzBuzz', test, 'fail')

