#!/usr/bin/python3

"""
Unit test for checkHost.parse_dpkg(text) with sample output from dpkg -l
"""

import unittest
import checkHost

class TestParsing(unittest.TestCase):
    def test_parser(self):
        dpkg_output = """Desired=Unknown/Install/Remove/Purge/Hold
    | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
    |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
    ||/ Name                                        Version                                             Architecture Description
    +++-===========================================-===================================================-============-================================================================================
    ii  a11y-profile-manager-indicator              0.1.10-0ubuntu3                                     amd64        Accessibility Profile Manager - Unity desktop indicator
    ii  account-plugin-facebook                     0.12+16.04.20160126-0ubuntu1                        all          GNOME Control Center account plugin for single signon - facebook
    ii  account-plugin-flickr                       0.12+16.04.20160126-0ubuntu1                        all          GNOME Control Center account plugin for single signon - flickr
    ii  account-plugin-google                       0.12+16.04.20160126-0ubuntu1                        all          GNOME Control Center account plugin for single signon
    ii  accountsservice                             0.6.40-2ubuntu10                                    amd64        query and manipulate user account information"""
#    def test_parser(self):
        self.assertEqual(checkHost.parse_dpkg(dpkg_output), [ 'a11y-profile-manager-indicator', 'account-plugin-facebook', 'account-plugin-flickr', 'account-plugin-google', 'accountsservice' ])


#def main():


if __name__ == '__main__':
      unittest.main()
