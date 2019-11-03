from django.test import TestCase

from controller.arithmetic_unit import long_int_addition, long_int_multiplication


class ArithmeticTestCase(TestCase):

    def test_add_numbers_with_same_length(self):

        number1 = [4]
        number2 = [5]

        self.assertEqual(long_int_addition(number1, number2), [9])

    def test_add_numbers_with_diff_length(self):

        number1 = [2,3]
        number2 = [5]

        self.assertEqual(long_int_addition(number1, number2), [2,8])

    def test_add_numbers_with_diff_length2(self):

        number1 = [2,3, 3]
        number2 = [5]

        self.assertEqual(long_int_addition(number1, number2), [2,3,8])

    def test_add_numbers_with_remainder(self):

        number1 = [2,5, 9]
        number2 = [6, 1]

        self.assertEqual(long_int_addition(number1, number2), [3,2,0])

    def test_add_numbers_with_remainder_at_the_end(self):

        number1 = [9, 9]
        number2 = [1]

        self.assertEqual(long_int_addition(number1, number2), [1,0,0])

    def test_multiply_numbers_with_same_length(self):

        number1 = [7,8]
        number2 = [ 1 ,1]

        self.assertEqual(long_int_multiplication(number1, number2), [8,5,8])

    def test_multiply_numbers_with_different_length(self):

        number1 = [7,8]
        number2 = [ 2]

        self.assertEqual(long_int_multiplication(number1, number2), [1,5,6])

    def test_multiply_numbers_with_remainder(self):

        number1 = [7,8]
        number2 = [ 2,3]

        self.assertEqual(long_int_multiplication(number1, number2), [1,7,9,4])

    def test_multiply_by_zero(self):

        number1 = [7,8]
        number2 = [ 0]

        self.assertEqual(long_int_multiplication(number1, number2), [0])