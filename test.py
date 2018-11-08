#/usr/bin/env python

import os
import numpy as np

import unittest

def cleanup(line):

    return line.strip().strip('\n').split()

def get_cmg_pressures():

    with open('assignment16.txt') as f:

        raw_content = f.readlines()


    pressure = []
    for i in range(len(raw_content)):
        line = raw_content[i]
        clean_line = cleanup(line) 

        if clean_line != []:
            if clean_line[1] == 'K':
                pressure += [cleanup(raw_content[i+1])]

    return np.array(pressure, dtype=np.double)


class TestSolution(unittest.TestCase):

    def test_output_pressures(self):

        pressures = get_cmg_pressures()

        np.testing.assert_allclose(get_cmg_pressures(),
                                   np.array([[1009, 1054,  1331,  1959.],
                                             [1009, 1054,  1331,  1959.],
                                             [1009, 1054,  1331,  1959.]]),
                                   atol=1)
        return


if __name__ == '__main__':
    unittest.main()
