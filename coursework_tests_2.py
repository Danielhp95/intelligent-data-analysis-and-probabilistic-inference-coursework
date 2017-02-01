import unittest
import numpy as np

from IDAPICoursework02 import *

class CourseworkTest2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.jpt  = [[0.07, 0.03, 0, 0.05],
                     [0.09, 0, 0, 0.01],
                     [0.04, 0.16, 0, 0],
                     [ 0, 0.05, 0.08, 0],
                     [ 0.05, 0.03, 0.07, 0.01],
                     [ 0.08, 0.09, 0.04, 0.03]]

    def test_probability_marginaliser(self):
        p_a, p_b = marginalise_probability(self.jpt)
        numpy.testing.assert_almost_equal(p_a, 0.98)
        numpy.testing.assert_almost_equal(p_b, 0.98)

    def test_mutual_information(self):
        mutual_information = MutualInformation(self.jpt)

if __name__ == '__main__':
    unittest.main()
