#!/usr/local/bin/python2.7

import sys, json, os
import subprocess

uuid = sys.argv[1]
str = 'curl -i http://geoprovdb.webfactional.com/api/v2.0/provenance/b/resource/%(uuid)s' % {"uuid":uuid}
print str
os.system(str)
