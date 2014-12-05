#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


host = os.environ.get('PROV_HOST')
if (host == None):
   host = 'http://geoprovdb.webfactional.com'

parser = OptionParser()
parser.add_option("-d","--direction", help ="Direction of provenance [backword(b)|forward(f)]. Default is backword(b)")
parser.add_option("-r","--resource property", help = "property of a resource such as its UUID, name, URI")
parser.add_option("-a","--activity property", help ="Activity property such as its name or activityid")
(options, args) = parser.parse_args()

direction = "b"
if (args[0] != ""):
   direction = args[0]
r_prop = args[1]
a_prop = args[2]

str = 'curl -i ' + host + '/api/v2.0/provenance/%(direction)s/resource/%(rprop)s/activity/%(aprop)s' % {"direction":direction,"rprop":r_prop,"aprop":a_prop}
print str
os.system(str)
