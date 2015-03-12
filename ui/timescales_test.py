__author__ = 'noe'

import unittest
import numpy as np

from timescales import ImpliedTimescales

class ImpliedTimescalesTest(unittest.TestCase):

    def setUp(self):
        self.dtrajs = []

        # simple case
        dtraj_simple = [0,1,1,1,0]
        self.dtrajs.append([dtraj_simple])

        # as ndarray
        self.dtrajs.append([np.array(dtraj_simple)])

        dtraj_disc = [0,1,1,0,0]
        self.dtrajs.append([dtraj_disc])

        # multitrajectory case
        self.dtrajs.append([[0],[1,1,1,1],[0,1,1,1,0],[0,1,0,1,0,1,0,1]])


    def compute_nice(self, reversible):
        """
        Tests if standard its estimates run without errors

        :return:
        """
        for i in range(len(self.dtrajs)):
            its = ImpliedTimescales(self.dtrajs[i], reversible=reversible)
            print its.get_lagtimes()
            print its.get_timescales()


    def test_nice_sliding_rev(self):
        """
        Tests if nonreversible sliding estimate runs without errors
        :return:
        """
        self.compute_nice(True)

    def test_nice_sliding_nonrev(self):
        """
        Tests if nonreversible sliding estimate runs without errors
        :return:
        """
        self.compute_nice(False)

    def test_too_large_lagtime(self):
        dtraj = [[0,1,1,1,0]]
        lags  = [1,2,3,4,5,6,7,8]
        expected_lags = [1,2,3] # 4 is impossible because only one state remains and no finite timescales.
        its = ImpliedTimescales(dtraj, lags=lags, reversible=False)
        got_lags = its.get_lagtimes()
        assert(np.shape(got_lags) == np.shape(expected_lags))
        assert(np.allclose(got_lags, expected_lags))



if __name__ == "__main__":
    unittest.main()
