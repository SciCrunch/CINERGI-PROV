#!/usr/local/bin/python2.7

import sys, json, os
import subprocess

f = open(sys.argv[1], 'r')
obj = f.read()
str = 'curl -i -H "Content-Type: application/json" -X POST -d \'%(obj)s\' http://geoprovdb.webfactional.com/api/v2.0/resource/provenance' % {"obj":obj}
os.system(str)



