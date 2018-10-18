# WICD MAC Randomizer

## 1.0.0 (October 18, 2018)

1. Initial commit (basic functionalities)

## Description

This is a script that will randomize the MAC address of your WICD-controlled interfaces. It will determine which interface (wired / wireless) is being activated, and randomize the interface MAC address before a connection is established.

## Installation

Copy the python script file to the WICD pre-connect script folder. It is usually located at `/etc/wicd/scripts/preconnect`.

### Option 1: Direct Download

This is the fastest way of installing this script.

```bash
$ sudo curl https://raw.githubusercontent.com/K4YT3X/wicd-mac-randomizer/master/wicd-mac-randomizer.py -o /etc/wicd/scripts/preconnect/wicd-mac-randomizer.py && chown root: /etc/wicd/scripts/preconnect/wicd-mac-randomizer.py && chmod 755 /etc/wicd/scripts/preconnect/wicd-mac-randomizer.py
```

### Option 2: Clone and Copy

First, clone the repository.

```bash
$ git clone https://github.com/K4YT3X/wicd-mac-randomizer.git
```

Then move the script into the WICD script folder.

```bash
$ sudo cp wicd-mac-randomizer.py /etc/wicd/scripts/preconnect
```

Check the file permission of the script is not working properly.

## Uninstalling

Simply remove the script from the WICD pre-connect script directory.

```bash
$ sudo rm /etc/wicd/scripts/preconnect/wicd-mac-randomizer.py
```

## Debugging

WICD MAC Randomizer logs everything into the syslog. To find out what's doing wrong, just look at the syslog. Here's  a sample command that you can use.

```bash
$ sudo tail -f /var/log/syslog | grep wicd-mac-randomizer
```