from contextlib import AbstractContextManager
import sys
from typing import Any
sys.path.insert(1, 'src')

import unittest
import calculate_coordinates as cco
import custome_calculations as cc
import pandas as pd
class TestCalculateCoordinates(unittest.TestCase):

    def test_add_x_and_y_to_df(self):
        self.assertEqual(0,0)
        x = [2671, 2640, 2560, 2511, 2490]
        y = [ 295.4, 360, 0,-360, -295.4]
        f = cc.generate_2d_function(x, y)
        ODOMETER_TO_MM_FACTOR = 1
        df = pd.DataFrame({
            'fixpoint_odometer_steps': [0, 100, 200, 300, 400, 500],      
            'steering': [2671, 2640, 2560, 2511, 2490, 2560]
        })

        self.assertEqual(cco.add_x_and_y_to_df(df, f, ODOMETER_TO_MM_FACTOR).size, 24)


        df = pd.DataFrame({
            'fixpoint_odometer_steps': [0, 200, 400, 600, 800, 1000, 1200 ],      
            'steering': [2640, 2640, 2640, 2640, 2640, 2640, 2640]
        })

        self.assertEqual(cco.add_x_and_y_to_df(df, f, ODOMETER_TO_MM_FACTOR).size, 28)





if __name__ == '__main__':
    unittest.main()  