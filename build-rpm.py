#!/usr/bin/env python2

import ConfigParser
import subprocess
import os

from contextlib import contextmanager

from glob import glob

@contextmanager
def cd(path):
	prevdir = os.getcwd()
	os.chdir(os.path.expanduser(path))
	try:
		yield
	finally:
		os.chdir(prevdir)

# Returns the builds that succeeded
def try_build(paths):
	good = set()
	for path in paths:
		print("Building specs in %s" %(path))
		with cd(path):
			tito_cmd = "tito release %s" %(release_target)
			result = subprocess.call(tito_cmd, shell=True)
			if result == 0:
				good.add(path)
	return good
			


branch_name = subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).rstrip()
release_target = "s3cmd-%s" %(branch_name)
print("Release target: %s" %(release_target))

# get bucket we are going to clear
tito_config = ConfigParser.RawConfigParser()
tito_config.read('.tito/releasers.conf')
s3bucket = tito_config.get(release_target,'s3cmd')

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

paths = set(glob('*/'))
while True:
	print("Attempting another round of builds")
	good_builds = try_build(paths)
	paths -= good_builds
	if len(good_builds) == 0 or len(paths) == 0:
		break
