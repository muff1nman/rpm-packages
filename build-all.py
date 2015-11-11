#!/usr/bin/env python2

import ConfigParser
import sys
import subprocess

# get bucket we are going to clear
tito_config = ConfigParser.RawConfigParser()
tito_config.read('.tito/releasers.conf')
s3bucket = tito_config.get(sys.argv[1],'s3cmd')

# Clear folder if it exists
check_cmd = "s3cmd info %s" %(s3bucket)
print(check_cmd)
check_result = subprocess.call(check_cmd, shell=True)
if(check_result == 12):
	pass
elif(check_result == 0):
	clear_cmd = "s3cmd del -r %s" %(s3bucket)
	print(clear_cmd)
	subprocess.check_call(clear_cmd, shell=True)
else:
	raise Exception('Unknown bucket status')

# Create the initial index
index_upload_cmd = "s3cmd put index.html %s" %(s3bucket)
print(index_upload_cmd)
subprocess.check_call(index_upload_cmd, shell=True)
