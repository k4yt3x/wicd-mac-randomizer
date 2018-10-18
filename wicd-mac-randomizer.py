#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: ICD Radomize MAC Script
Dev: K4YT3X
Date Created: October 18, 2018
Last Modified: October 18, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt
(C) 2018 K4YT3X

VERSION = 1.0.0
"""
import configparser
import os
import subprocess
import sys
import syslog
import traceback


class Utilities:
    """ Useful utilities

    This class contains a number of utility tools.
    """

    def execute(command, input_value=''):
        """ Execute a system command and return the output
        """
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = process.communicate(input=input_value)[0]
        return output.decode().replace('\n', '')


class WICD:
    """ WICD handler

    This class creates an object that will handle
    everything that's related to WICD.
    """

    def __init__(self):
        self.config_path = '/etc/wicd/manager-settings.conf'

    def get_wicd_settings_value(self, key):
        """ Read a specific key from WICD settings
        """
        wicd_config = configparser.ConfigParser()
        wicd_config.read(self.config_path)
        try:
            return wicd_config['Settings'][key]
        except KeyError:
            pass

    def get_wired_interface(self):
        """ Returns the wired interface name
        """
        return self.get_wicd_settings_value('wired_interface')

    def get_wireless_interface(self):
        """ Returns the wireless interface name
        """
        return self.get_wicd_settings_value('wireless_interface')


class Log:
    """ Logs message to syslog and print to tty
    """

    def info(message):
        syslog.syslog(syslog.LOG_INFO, message)
        print(message, file=sys.stdout)

    def err(message):
        syslog.syslog(syslog.LOG_ERR, message)
        print(message, file=sys.stderr)


def randomize_mac(interface):
    """ Randomize MAC address of interface via macchanger
    """
    Utilities.execute(['ip', 'link', 'set', interface, 'down'])
    Utilities.execute(['macchanger', '-b', '-A', interface])
    Utilities.execute(['ip', 'link', 'set', interface, 'up'])


def main():
    """ Main function of WRM

    This main function controls the flow of the entire
    program.
    """
    wicd = WICD()
    interface_type = sys.argv[1]
    essid = sys.argv[2]
    bssid = sys.argv[3]

    if interface_type == 'wired':
        interface = wicd.get_wired_interface()
    elif interface_type == 'wireless':
        interface = wicd.get_wireless_interface()
    else:
        Log.err('ERR: Interface type \"{}\" unidentified'.format(interface_type))
        sys.exit(1)

    Log.info('Interface: {}'.format(interface))
    Log.info('ESSID: {}'.format(essid))
    Log.info('BSSID: {}'.format(bssid))

    Log.info('Randomizing MAC for {}'.format(interface))
    randomize_mac(interface)


# Check if script is being executed as root
# Root privilege is required for this program
if os.getuid() != 0:
    Log.err('ERR: This script must be run as root')
    sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        # Log any exceptions
        Log.err(traceback.format_exc())
