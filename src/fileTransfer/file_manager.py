"""
#-----------------------------------------------------------------------------
# Name: file_manager.py
#
# Description: Import used to copy, rename and delete files
#
# Arguments: src_fpath, tmp_dst_fpath, local_tran_dict, logger
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
#import time
import shutil

class FileManager:
    """Class for FileManager"""

    def __init__(self, src_fpath, tmp_dst_fpath, local_tran_dict, logger):
        self.src_fpath = src_fpath
        self.tmp_dst_fpath = tmp_dst_fpath
        self.local_tran_dict = local_tran_dict
        self.logger = logger

    def copy_file(self):
        """Method to copy file"""
        try:
            shutil.copy(self.src_fpath, self.tmp_dst_fpath)
        except EnvironmentError:
            self.logger.error('ERROR occurred during COPY of %s to %s',
                              self.src_fpath, self.tmp_dst_fpath)
            raise ValueError
        else:
            self.logger.info('COPY was successful of %s to %s',
                             self.src_fpath, self.tmp_dst_fpath)

    def rename_file(self):
        """Method to rename a file"""
        try:
            if self.local_tran_dict['finalname'] is None:
                dst_fpath = os.path.join(self.local_tran_dict['dest_home'],
                                         os.path.basename(self.src_fpath))
            else:
                dst_fpath = os.path.join(self.local_tran_dict['dest_home'],
                                         self.local_tran_dict['finalname'])

            os.rename(self.tmp_dst_fpath, dst_fpath)
        except EnvironmentError:
            self.logger.error('\tERROR occurred during RENAME of %s to %s',
                              self.tmp_dst_fpath, dst_fpath)
            raise ValueError
        else:
            self.logger.info('\tRENAME was successful of %s to %s',
                             self.tmp_dst_fpath, dst_fpath)

    def delete_file(self):
        """Method to delete a file"""
        if self.local_tran_dict['delete'] == 'TRUE':
            try:
                os.remove(self.src_fpath)
            except EnvironmentError:
                self.logger.error('ERROR occurred during delete of %s', self.src_fpath)
                raise ValueError
            else:
                self.logger.info('\tDELETE was successful of %s', self.src_fpath)
