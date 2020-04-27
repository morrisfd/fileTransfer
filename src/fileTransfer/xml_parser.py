"""
#-----------------------------------------------------------------------------
# Name: xml_parser.py
#
# Description: Import used for parsing filetransfer xml.
#
# Arguments: xml_in_file, in_transfer_id, logger
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

import sys
import xml.etree.ElementTree as et

import fileTransfer.utility as ut

class XMLParser:
    """Class for parsing XML"""

    def __init__(self, xml_in_file, in_transfer_id, logger):
        self.xml_in_file = xml_in_file
        self.in_transfer_id = in_transfer_id
        self.logger = logger

    def build_local_tran_lst(self):
        """For XML 'filetransfer' parent element tagged w/the specified TransferID,
        build list of dict(s) w/data fields within each 'localtransaction' sub-element.
        """
        tree = et.parse(self.xml_in_file)

        local_tran_lst = []
        for elmnt_01 in tree.findall('filetransfer'):
            if elmnt_01.get('id') == self.in_transfer_id:
                # elmnt_02_local_tran is the 'localtransaction' sub-element
                for elmnt_02_local_tran in elmnt_01:
                    local_tran_dict = self.build_local_tran_dict(elmnt_02_local_tran)

                    if local_tran_dict is not None:
                        local_tran_lst.append(local_tran_dict)

        return local_tran_lst

    def build_local_tran_dict(self, elmnt_02_local_tran):
        """Build dict of data fields within 'localtransaction' sub-element."""

        try:
            local_tran_dict = {'transfer_id' : self.in_transfer_id}
            local_tran_dict['dest_home'] = ut.set_path(elmnt_02_local_tran.get(
                'destHome', default=None), 'dest_home', logger=self.logger)
            local_tran_dict['max_retries'] = ut.set_positive_int(elmnt_02_local_tran.get(
                'maxRetries', default=None), 'max_retries', logger=self.logger)
            local_tran_dict['retry_interval'] = ut.set_positive_int(elmnt_02_local_tran.get(
                'retryInterval', default=None), 'retry_interval', logger=self.logger)

            for elmnt_03 in elmnt_02_local_tran:
                local_tran_dict['transfer_type'] = elmnt_03.get('type', default=None)

                local_tran_dict['tmp_prefix'] = '.TMP.'
                local_tran_dict['source'] = None
                local_tran_dict['finalname'] = None

                for elmnt_04 in elmnt_03:
                    if elmnt_04.tag == 'source':
                        local_tran_dict['delete'] = ut.set_bool(elmnt_04.get(
                            'delete', default=None), 'delete')
                        local_tran_dict['source'] = elmnt_04.text
                    #if elmnt_04.tag == 'destination':
                        #local_tran_dict['tmp_prefix'] = elmnt_04.text
                    if elmnt_04.tag == 'finalname':
                        local_tran_dict['finalname'] = ut.set_final_name(elmnt_04.text)

            return local_tran_dict

        except Exception as _e:
            self.logger.error(_e)
            sys.exit(1)
