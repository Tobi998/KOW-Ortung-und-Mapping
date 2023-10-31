from contextlib import AbstractContextManager
import sys
from typing import Any
sys.path.insert(1, 'src')

import unittest
import pre_procces as pp
import pandas as pd

class TestPreProccess(unittest.TestCase):

    def test_read_csv_file(self):
        self.assertEqual(0, 0)

    def test_filter_dublicates(self):
        data_pre = {
            'fixpoint_odometer_steps': [10, 20, 30, 30, 30, 60, 70, 70, 70, 70],      
            'steering': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        }
        data_post = {
            'fixpoint_odometer_steps': [10, 20, 30, 60, 70],
            'steering': [5, 10, 15, 30, 35]
        }
        self.assertEqual(pp.filter_dublicates(pd.DataFrame(data_pre)).size, 10)

if __name__ == '__main__':
    unittest.main()