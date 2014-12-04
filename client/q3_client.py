#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


parser = OptionParser()
parser.add_option("-d","--direction", help ="Direction of provenance [backword(b)|forward(f)]. Default is backword(b)")
parser.add_option("-p","--resource property", help ="Property of a resource, such as name")
(options, args) = parser.parse_args()
direction = "b"
if (args[0] != ""):
   direction = args[0]
prop = args[1]
str = 'curl -i http://geoprovdb.webfactional.com/api/v2.0/provenance/%(direction)s/resource/%(prop)s' % {"direction":direction,"prop":prop}
print str
os.system(str)