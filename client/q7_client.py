#!/usr/local/bin/python2.7

from optparse import OptionParser
import sys, json, os
import subprocess


host = os.environ.get('PROV_HOST')
if (host == None):
   print "set PROV_HOST variable"
   sys.exit()
   #host = 'http://geoprovdb.webfactional.com/provdb'

parser = OptionParser()
parser.add_option("-d","--direction", help ="Direction of provenance [backword(b)|forward(f)]. Default is backword(b)")
parser.add_option("-a","--activity property", help ="Activity property such as its name or activityid")
parser.add_option("-t1","--datetime start", help = "The start of an activity")
parser.add_option("-t2","--datetime end", help = "The end of an activity")
(options, args) = parser.parse_args()

direction = "b"
if (args[0] != ""):
   direction = args[0]
activity = args[1]
t1 = args[2]
t2 = args[3]

str = 'curl -i ' + host + '/provenance/%(d)s/activity/%(a)s/from/%(t1)s/to/%(t2)s' % {"d":direction,"a":activity,"t1":t1,"t2",t2}
print str
os.system(str)
