#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess

host = os.environ.get('PROV_HOST')
if (host == None):
   host = 'http://geoprovdb.webfactional.com/provdb'

parser = OptionParser()
parser.add_option("-n","--node")
(options, args) = parser.parse_args()

uuid = args[0]
str = 'curl -i -X DELETE ' + host + '/resource/%(uuid)s' % {"uuid":uuid}
print str
os.system(str)



