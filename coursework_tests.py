import unittest
from numpy import *

# Import file with to be tested below. Change name if file name changes with time
from IDAPICourseworkSkeleton import *

class CourseworkTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data     = [[0,1,2], [0,2,3], [1,2,2], [1,2,4]]
        self.noStates = [2,3,5] 

    def test_Prior(self):
        prior = Prior(self.data, 0, self.noStates)
        self.assertEqual([0.5, 0.5], prior)
        self.assertEqual(sum(prior), 1)

    def test_CPT(self):
        cpt_1_2 = [[0.5, 1.0, 0.3333333333333333],
                    [0.5, 0.0, 0.6666666666666666]]
        cpt = CPT(self.data, 0, 1, self.noStates)
        numpy.testing.assert_array_equal(cpt_1_2, cpt)
        self.assertEqual(True, self.__check_column_sum_to_one(cpt))

    def test_JPT(self):
        jpt_1_2   = [[0, 0.25, 0.25],
                     [0, 0, 0.5]]
        jpt = JPT(self.data, 0, 1, self.noStates)
        numpy.testing.assert_array_equal(jpt_1_2, jpt)

    def test_JPT2CPT(self):
        cpt_1_2 = [[0.5, 1.0, 0.3333333333333333],
                    [0.5, 0.0, 0.6666666666666666]]
        jpt_1_2   = [[0, 0.25, 0.25],
                     [0, 0, 0.5]]
        cpt = CPT(self.data, 0, 1, self.noStates)
        jpt = JPT(self.data, 0, 1, self.noStates)
        numpy.testing.assert_array_equal(jpt_1_2, jpt)
        numpy.testing.assert_array_equal(cpt_1_2, cpt)
        self.assertEqual(True, self.__check_column_sum_to_one(cpt))
        converted_cpt = JPT2CPT(jpt)
        numpy.testing.assert_array_equal(cpt, converted_cpt)

    def __check_column_sum_to_one(self,matrix):
        for j in range(len(matrix[0])):
            sum = 0
            for i in range(len(matrix)):
                sum += matrix[i][j]
            if sum != 1:
                return False
        return True


if __name__ == '__main__':
    unittest.main()
