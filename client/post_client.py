#!/usr/local/bin/python2.7

import sys, json, os
import subprocess

f = open(sys.argv[1], 'r')
obj = f.read()

host = os.environ.get('PROV_HOST')
if (host == None):
   host = 'http://geoprovdb.webfactional.com'

str = 'curl -i -H "Content-Type: application/json" -X POST -d \'%(obj)s\' ' % {"obj":obj} + host + '/api/v2.0/resource/provenance'
print str
#os.system(str)



