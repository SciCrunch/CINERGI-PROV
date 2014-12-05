#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


host = os.environ.get('PROV_HOST')
if (host == None):
   host = 'http://geoprovdb.webfactional.com/provdb'

parser = OptionParser()
parser.add_option("-u","--uuid", help = "UUID of the resource")
parser.add_option("-a","--activity", help ="Activity property such as name or activityid")
(options, args) = parser.parse_args()

uuid = args[0]
activity = args[1]
str = 'curl -i ' + host + '/provenance/b/resource/%(uuid)s/activity/%(activity)s' % {"uuid":uuid,"activity":activity}
print str
os.system(str)
