#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


parser = OptionParser()
parser.add_option("-u","--uuid")
(options, args) = parser.parse_args()
uuid = args[0]
str = 'curl -i http://geoprovdb.webfactional.com/api/v2.0/provenance/b/resource/%(uuid)s' % {"uuid":uuid}
print str
os.system(str)
