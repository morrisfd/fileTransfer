#!/usr/bin/env python3
"""
######################################################################################
 date          Eng      SCR          Description
 2019-10-24    lorensd  SYSSAT-448   Created for testing
                                     1. Unit tests for testing file transfer python code.
######################################################################################
"""
import os
import re
import sys
#import shutil

import unittest
import subprocess

import context
import fileTransfer.utility as ut

USER = os.environ['USER']
print('sys.argv[0] =', sys.argv[0])
PATHNAME = os.path.dirname(sys.argv[0])
print('path =', PATHNAME)
FULLPATH = os.path.abspath(PATHNAME)
print('full path =', FULLPATH)

TESTDIR = FULLPATH.replace('/tests', '')
print('TESTDIR: ', TESTDIR)
MAINDIR = TESTDIR.replace('/tests', '')
print('MAINDIR: ', MAINDIR)
sys.path.append(MAINDIR + '/src')
print(sys.path)

class TestFileTransfer(unittest.TestCase):
    """Class for Unit testing file transfer"""

    def test_set_properties_in_file(self):
        """Unit test for set_properties_in_file method"""
        print('TEST 1.01:')
        self.assertEqual(ut.set_properties_in_file('TESTMFT.properties'),
                         'TESTMFT.properties')
        print('TEST 1.02:')
        self.assertRaises(SystemExit, ut.set_properties_in_file, 'TESTMFT.txt')

    def test_set_transfer_id(self):
        """Unit test for set_transfer_id method"""
        print('TEST 2.01:')
        self.assertEqual(ut.set_transfer_id('ssies_transfer'),
                         'ssies_transfer')
        print('TEST 2.02:')
        self.assertRaises(SystemExit, ut.set_transfer_id, 'NAP-IMAGES')

    def test_is_valid_transfer_id(self):
        """Unit test for is_valid_transfer_id method"""
        print('TEST 3.01:')
        self.assertTrue(ut.is_valid_transfer_id('ssies_transfer'))
        print('TEST 3.02:')
        self.assertTrue(ut.is_valid_transfer_id('faker'))
        print('TEST 3.03:')
        self.assertTrue(ut.is_valid_transfer_id('fdm_transfer03'))
        print('TEST 3.04:')
        self.assertFalse(ut.is_valid_transfer_id('NAP-IMAGES'))
        print('TEST 3.05:')
        self.assertFalse(ut.is_valid_transfer_id('oval-transfer'))

    def test_set_path(self):
        """Unit test for set_path method"""
        print('TEST 4.01:')
        self.assertTrue(ut.set_path(os.getcwd(), 'var_name'), os.getcwd())
        print('TEST 4.02:')
        self.assertRaises(SystemExit, ut.set_path, 'fakepath/fakefile', 'var_name')

    def test_set_numeric_log_level(self):
        """Unit test for set_numeric_log_level method"""
        print('TEST 5.01:')
        self.assertEqual(ut.set_numeric_log_level('DEBUG'), 10)
        print('TEST 5.02:')
        self.assertEqual(ut.set_numeric_log_level('INFO'), 20)
        print('TEST 5.03:')
        self.assertEqual(ut.set_numeric_log_level('WARNING'), 30)
        print('TEST 5.04:')
        self.assertEqual(ut.set_numeric_log_level('ERROR'), 40)
        print('TEST 5.05:')
        self.assertEqual(ut.set_numeric_log_level('critical'), 50)
        print('TEST 5.06:')
        self.assertRaises(SystemExit, ut.set_numeric_log_level, 'fakelog')

    def test_set_positive_int(self):
        """Unit test for set_positive_int method"""
        print('TEST 6.01:')
        self.assertEqual(ut.set_positive_int(None, 'var_name'), None)
        print('TEST 6.02:')
        self.assertEqual(ut.set_positive_int('', 'var_name'), None)
        print('TEST 6.03:')
        self.assertEqual(ut.set_positive_int('1', 'var_name'), 1)
        print('TEST 6.04:')
        self.assertRaises(SystemExit, ut.set_positive_int, '-1', 'var_name')

    def test_set_bool(self):
        """Unit test for set_bool method"""
        print('TEST 7.01:')
        self.assertEqual(ut.set_bool('true', 'var_name'), 'TRUE')
        print('TEST 7.02:')
        self.assertEqual(ut.set_bool('FALSE', 'var_name'), 'FALSE')
        print('TEST 7.03:')
        #self.assertRaises(AttributeError, ut.set_bool, 'fakebool', 'var_name')
        #print('TEST 7.04')
        self.assertRaises(RuntimeError, ut.set_bool, 'fakebool', 'var_name')

    # integration tests
    def test_ssies_transfer(self):
        """Unit test for number of files being moved"""
        print('TEST 8.01:')
        subprocess.call(['python', MAINDIR + '/src/fileTransfer/cli/main_file_transfer.py',
                         TESTDIR + '/config/TESTMFT.properties', 'ssies_transfer'])

        output_dir = TESTDIR + '/data/dmsp/ssies/archive/ies'

        regex = re.compile(".*SIES.*\.EDR")
        print('TEST 8.02:')
        file_matches = [name for name in os.listdir(output_dir)
                        if os.path.isfile(os.path.join(output_dir, name))
                        and re.match(regex, name)]

        print('TEST 8.03:')
        self.assertEqual(len(file_matches), 10)

    def test_faker(self):
        """Unit test for fake data"""
        print('TEST 9.01:')
        #subprocess.call(['chmod 444 ~/data/fakedir/faker/Product'])
        #print('TEST 9.01.01:')
        subprocess.call(['python', MAINDIR + '/src/fileTransfer/cli/main_file_transfer.py',
                         TESTDIR + '/config/TESTMFT.properties', 'faker'])

        print('TEST 9.02:')
        output_dirs = [TESTDIR + '/data/fakedir/input']
        finalname = 'PS.AFWA_SC.U_DI.A_DC.IMAGERY_DS.SPACE-OBS_PA.SUMMARY_DF.GIF'

        #        for dir in output_dirs:
        #            file_match = [name for name in os.listdir(dir)
        #                if os.path.isfile(os.path.join(dir, name))
        #                and name == finalname]
        #
        #            self.assertEqual(len(file_match), 1)

        for _dir in output_dirs:
            file_match = [name for name in os.listdir(_dir)
                          if os.path.isfile(os.path.join(_dir, name))
                          and name == finalname]
            print('TEST 9.03:')
            print(f'file_match: {file_match} finalname: {finalname}')
            self.assertEqual(len(file_match), 1)

        output_dirs = [TESTDIR + '/data/fakedir/faker/Product']

        for _dir in output_dirs:
            file_match = [name for name in os.listdir(_dir)
                          if os.path.isfile(os.path.join(_dir, name))
                          and name == finalname]
            print('TEST 9.04:')
            self.assertEqual(len(file_match), 1)

        output_dirs = [TESTDIR + '/data/fakedir/faker']

        for _dir in output_dirs:
            file_match = [name for name in os.listdir(_dir)
                          if os.path.isfile(os.path.join(_dir, name))
                          and name == finalname]
            print('TEST 9.04:')
            self.assertEqual(len(file_match), 0)

if __name__ == '__main__':
    unittest.main()
