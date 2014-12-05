#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


host = os.environ.get('PROV_HOST')
if (host == None):
   host = 'http://geoprovdb.webfactional.com'

parser = OptionParser()
parser.add_option("-u","--uuid")
(options, args) = parser.parse_args()

uuid = args[0]
str = 'curl -i ' + host + '/api/v2.0/provenance/b/resource/%(uuid)s' % {"uuid":uuid}
print str
os.system(str)
