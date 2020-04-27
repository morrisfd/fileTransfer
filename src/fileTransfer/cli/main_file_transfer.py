"""
#-----------------------------------------------------------------------------
# Name: main_file_transfer.py
#
# Description: Replacement for filetransfer from baseline FILE_TRANSFER
#
# Arguments: Properties.properties - used to set variables.
#            TransferID            - used to process files to be transfered
#                                    (copied, renamed, deleted)
#
# Authors: Franke Morris and Devan Lorenson
#
# Version: 1.0.0
#
# Date: 04 Oct 2019
#-----------------------------------------------------------------------------
# Update History
#
# Version      Date        Who              What Changed
#-----------------------------------------------------------------------------
"""

import os
import sys

import fileTransfer.utility as ut
from fileTransfer.logger import Logger
from fileTransfer.xml_parser import XMLParser
from fileTransfer import FileManager

def main():
    """main function"""
    if len(sys.argv) != 3:
        print('usage: python main_file_transfer.py Properties.properties TransferID')
        sys.exit(1)

    properties_in_file = ut.set_properties_in_file(sys.argv[1])
    in_transfer_id = ut.set_transfer_id(sys.argv[2])
    base_path = os.path.dirname(os.path.realpath(__file__))

    with open(properties_in_file, 'r') as _f:
        config_string = _f.read()

        for this_line in config_string.split('\n'):
            this_item = this_line.split('=')
            if this_item[0] == 'logger.directory':
                log_dir = ut.set_path(this_item[1], this_item[0])
            if this_item[0] == 'python.log.level':
                numeric_log_level = ut.set_numeric_log_level(this_item[1])
            if this_item[0] == 'python.log.days':
                log_days = ut.set_positive_int(this_item[1], this_item[0])
            if this_item[0] == 'filetransfer.xmlfile':
                xml_in_file = ut.set_path(this_item[1], this_item[0])

    logger = Logger(log_dir, numeric_log_level,
                    log_days, 'file_transfer').get_logger()

    logger.debug('args len: %s - %s', len(sys.argv), sys.argv)
    logger.debug('base_path: %s', base_path)
    logger.debug('log_dir:   %s', log_dir)
    logger.debug('log_level: %s', numeric_log_level)
    logger.debug('xml_file:  %s', xml_in_file)

    # for XML 'filetransfer' parent element tagged w/the specified TransferID,
    # build list of dict(s) w/data fields within each 'localtransaction' sub-element
    local_tran_lst = XMLParser(xml_in_file, in_transfer_id, logger).build_local_tran_lst()

    # iterate through each 'localtransaction' sub-element dict
    for local_tran_dict in local_tran_lst:
        logger.debug('Transfer ID: %s', local_tran_dict['transfer_id'])
        logger.debug('Transfer Type:  %s', local_tran_dict['transfer_type'])
        logger.debug('Source: %s', local_tran_dict['source'])
        logger.debug('Destination Home: %s', local_tran_dict['dest_home'])
        logger.debug('Tmp Prefix: %s', local_tran_dict['tmp_prefix'])
        logger.debug('Final Name: %s', local_tran_dict['finalname'])
        logger.debug('Delete: %s', local_tran_dict['delete'])
        logger.debug('Max Retries: %s', local_tran_dict['max_retries'])
        logger.debug('Retry Interval: %s', local_tran_dict['retry_interval'])

        # build dict w/paths for each 'localtransaction' src file match:
        # original src path & temp dst path
        path_dct = ut.build_path_dct(local_tran_dict)

        # iterate through each src file match
        for src_fpath, tmp_dst_fpath in path_dct.items():
            _fm = FileManager(src_fpath, tmp_dst_fpath, local_tran_dict, logger)
            _fm.copy_file()
            _fm.rename_file()
            _fm.delete_file()

if __name__ == "__main__":
    main()
