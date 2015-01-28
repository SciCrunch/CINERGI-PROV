#!/usr/local/bin/python2.7

import sys, json, os
import subprocess

f = open(sys.argv[1], 'r')
obj = f.read()

host = os.environ.get('PROV_HOST')
if (host == None):
   print "Set PROV_HOST environment variable"
   sys.exit()
   #host = 'http://geoprovdb.webfactional.com/provdb'

str = 'curl -u tanu:cinergi -i -H "Content-Type: application/json" -X POST -d \'%(obj)s\' ' % {"obj":obj} + host + '/api/provenance/'
#print str
os.system(str)

