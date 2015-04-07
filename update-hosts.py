#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Update hosts for *nix
Author: cloud@txthinking.com
Version: 0.0.1
Date: 2012-10-24 14:35:39

        Modified:2015-04-05 22:44:38 By DropFan@Gmail.com

'''

import urllib2
import os
import sys
from var_dump import var_dump

HOSTS_PATH = "/etc/hosts"
HOSTS_SOURCE = "http://freedom.txthinking.com/hosts"
SEARCH_STRING = "#TX-HOSTS"

def GetRemoteHosts(url):
    try:
        f = urllib2.urlopen(url, timeout=5)
        hosts = [line for line in f]
        # print hosts
        f.close()
        print 'Done.'
        return hosts
    except urllib2.HTTPError, e:
        print  e
        print "Could't connect to %s. \nPlease try again." % HOSTS_SOURCE
        sys.exit()
def main():
    print '*'*80
    print '''
        Fuck GFW.
            update hosts for unix/linux/OS X

        Author:cloud@txthinking
        Date:2012-10-24 14:35:39

        Modified:2015-04-05 22:44:38 By DropFan@Gmail.com
'''
    print '*'*80

    HOSTS_SOURCE = raw_input('Please set a url for hosts source:\n1:https://raw.githubusercontent.com/DropFan/hosts/master/hosts\n2:http://freedom.txthinking.com/hosts\nor input your customized url\n:')
    if HOSTS_SOURCE == '1':
        HOSTS_SOURCE = 'https://raw.githubusercontent.com/DropFan/hosts/master/hosts'
    elif HOSTS_SOURCE == '2':
        HOSTS_SOURCE = "http://freedom.txthinking.com/hosts"

    print '1. Getting remote hosts from : %s' % HOSTS_SOURCE
    try:
        hosts = GetRemoteHosts(HOSTS_SOURCE)
    except Exception,e:
        print e
        print 'It\'s a exception here.Please retry.'
        sys.exit(1)

    print '2. Reading current hosts...'
    try:
        yours = ""
        if os.path.isfile(HOSTS_PATH):
            f = open(HOSTS_PATH, "r")
            for line in f:
                if SEARCH_STRING in line:
                    break
                yours += line
            f.close()
        yours += SEARCH_STRING + "\n"
    except OSError,e:
        if e[0]==13:
            print e
            print 'Please run this script with sudo.'
            sys.exit()
    except Exception,e:
        print e
        print 'Please try again.'
        sys.exit()
    finally:
        print 'Done.'

    print '3. Writting hosts file...'
    try:
        os.rename(HOSTS_PATH, HOSTS_PATH + ".bak")
        print 'The original hosts has renamed as %s.bak' % HOSTS_PATH
        fp = open(HOSTS_PATH, "w")
        fp.write(yours)
        fp.writelines(hosts)
        fp.close()
        fp = open('./hosts.bak','w')
        fp.write(yours)
        fp.close
        os.system('cp '+HOSTS_PATH+' ./hosts-latest')
        print "\nUpdate success !"
    except OSError,e:
        if e[0]==13:
            print e
            print 'Please run this script with sudo.'
            sys.exit()
        print e
        print 'Please try again.'
if __name__ == "__main__":
    main()
