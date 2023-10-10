import sys
sys.path.insert(1, 'src')

import unittest
import custome_calculations as cc
import numpy as np


class TestCustomeCalculations(unittest.TestCase):

    def test_calculate_adjacent_side(self):
        self.assertEqual(cc.calculate_adjacent_side(45, 100), 70.71067811865476)

        self.assertRaises(ValueError, cc.calculate_adjacent_side, 90, 100)
        self.assertRaises(ValueError, cc.calculate_adjacent_side, 0, 100)
        self.assertRaises(ValueError, cc.calculate_adjacent_side, -90, 100)
        self.assertRaises(ValueError, cc.calculate_adjacent_side, 180, 100)

    def test_calculate_opposit_side(self):
        self.assertEqual(cc.calculate_opposit_side(45, 100), 70.71067811865476)

        self.assertRaises(ValueError, cc.calculate_adjacent_side, 90, 100)
        self.assertRaises(ValueError, cc.calculate_adjacent_side, 0, 100)
        self.assertRaises(ValueError, cc.calculate_adjacent_side, -90, 100)
        self.assertRaises(ValueError, cc.calculate_adjacent_side, 180, 100)
    
    def test_calculate_alpha(self):
        self.assertEqual(cc.calculate_alpha(10, 5*np.pi), 90)
        self.assertEqual(cc.calculate_alpha(10, 10*np.pi), 180)
        self.assertAlmostEqual(cc.calculate_alpha(10, 15*np.pi), 270)
        self.assertEqual(cc.calculate_alpha(10, 20*np.pi), 360)

        self.assertRaises(ValueError, cc.calculate_alpha, 0, 100)
        self.assertRaises(ValueError, cc.calculate_alpha, -10, 100)

    def test_generate_2d_function(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 20, 30, 40, 50])
        f = cc.generate_2d_function(x, y)

        self.assertEqual(f(1), 10)
        self.assertEqual(f(2), 20)
        self.assertEqual(f(3), 30)
        self.assertEqual(f(4), 40)
        self.assertEqual(f(5), 50)


if __name__ == '__main__':
    unittest.main()