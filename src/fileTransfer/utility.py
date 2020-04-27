"""
#-----------------------------------------------------------------------------
# Name: utility.py
#
# Description: Import for setup and validation.
#
# Arguments: various.
#
# Authors: Franke Morris and Devan Lorenson
#
# Version: 1.0.0
#
# Date: 24 Oct 2019
#-----------------------------------------------------------------------------
# Update History
#
# Version      Date        Who              What Changed
#-----------------------------------------------------------------------------
"""

import os
import re
import sys
import glob
import logging

def set_properties_in_file(in_file):
    """Method to set properties from file"""
    try:
        if not in_file.endswith('properties'):
            raise ValueError()
        return in_file
    except ValueError:
        print('Properties file is invalid: %s' % in_file)
        sys.exit(1)

def set_transfer_id(transfer_id):
    """Method to handle transfer ID"""
    try:
        if not is_valid_transfer_id(transfer_id):
            raise ValueError()
        return transfer_id
    except ValueError:
        print('Transfer ID is invalid: %s' % transfer_id)
        sys.exit(1)

def is_valid_transfer_id(transfer_id, search=re.compile(r'[a-zA-Z0-9_]').search):
    """Method to check for valid transfer ID"""
    for _x in transfer_id:
        if not bool(search(_x)):
            print('Found invalid character in transfer ID: %s' % _x)
            return False
    return True

def set_path(path, var_name, logger=None):
    """Method to handle path"""
    try:
        if not os.path.exists(path) or not os.access(os.path.dirname(path), os.W_OK):
            raise ValueError()
        return path
    except ValueError:
        if logger is not None:
            raise RuntimeError('%s path is invalid: %s. It either doesn\'t exist, '\
                'or you don\'t have write access.' % (var_name, path))
        else:
            print('%s path is invalid: %s. It either doesn\'t exist, '\
                'or you don\'t have write access.' % (var_name, path))
            sys.exit(1)

def set_numeric_log_level(log_level_str):
    """Method to handle numeric log level"""
    try:
        # 5 standard logging levels: DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50

        numeric_log_level = getattr(logging, log_level_str.upper(), None)

        if not isinstance(numeric_log_level, int):
            raise ValueError()

        return numeric_log_level
    except (ValueError, AttributeError):
        print('Log level is invalid: %s' % log_level_str)
        sys.exit(1)

def set_positive_int(string, var_name, logger=None):
    """Method to handle positive int"""
    try:
        if string is None or len(string) == 0:
            return None
        else:
            new_int = int(string)
            if new_int < 0:
                raise ValueError()
            return new_int
    except ValueError:
        if logger is not None:
            raise RuntimeError('%s is invalid: %s. Must be a positive'\
                    'integer.' % (var_name, string))
        else:
            print('%s is invalid: %s. Must be a positive integer.' % (var_name, string))
            sys.exit(1)

#def set_bool(string, var_name, logger=None):
def set_bool(string, var_name):
    """Method to handle bool"""
    try:
        string_upper = string.upper()
        if string_upper not in ['TRUE', 'FALSE']:
            raise ValueError
        return string_upper
    except ValueError:
        raise RuntimeError('%s is invalid: %s. Must be boolean.' % (var_name, string))

def set_final_name(final_name):
    """ handles blank and single character (*) final name tags"""
    if final_name is None or len(final_name) < 2:
        return None
    else:
        return final_name

def build_path_dct(local_tran_dict):
    """Returns dict w/src path (key) & tmp dst path (value).

    {src_fpath : tmp_dst_fpath}
    """
    path_dct = {}
    for src_fpath in glob.glob(local_tran_dict['source']):
        src_f = os.path.basename(src_fpath)

        tmp_dst_f = local_tran_dict['tmp_prefix'] + src_f
        tmp_dst_fpath = os.path.join(local_tran_dict['dest_home'], tmp_dst_f)
        path_dct[src_fpath] = tmp_dst_fpath

    return path_dct
