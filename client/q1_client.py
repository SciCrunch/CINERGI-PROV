#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


host = os.environ.get('PROV_HOST')
if (host == None):
   print "Set PROV_HOST variable"
   sys.exit()
   #host = 'http://geoprovdb.webfactional.com/provdb'

parser = OptionParser()
parser.add_option("-n","--namespace")
parser.add_option("-u","--uuid")
(options, args) = parser.parse_args()

print len(args)
namespace = options.namespace
uuid = options.uuid
str = 'curl -u test:cinergi -i ' + host + '/api/%(namespace)s' %{"namespace":namespace} + '/provenance/%(uuid)s' % {"uuid":uuid}
print str
os.system(str)
