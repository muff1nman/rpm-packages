#!/usr/bin/env python2

import ConfigParser
import subprocess
import os
import logging
import sys

from contextlib import contextmanager

from glob import glob

DRY_RUN = False
RELEASE_FILE = "release"

tito_config = ConfigParser.RawConfigParser()
tito_config.read('.tito/releasers.conf')
logging.basicConfig(level=logging.INFO)

def log_command(cmd):
	logging.info("Executing [%s] in path [%s]" %(cmd, os.getcwd()))

def check_call(cmd):
	log_command(cmd)
	if not DRY_RUN:
		subprocess.check_call(cmd, shell=True)
	else:
		logging.debug("Not Executing due to DRY RUN")

def call(cmd):
	log_command(cmd)
	if not DRY_RUN:
		return subprocess.call(cmd, shell=True)
	else:
		logging.debug("Not Executing due to DRY RUN")
		return 0

@contextmanager
def cd(path):
	prevdir = os.getcwd()
	os.chdir(os.path.expanduser(path))
	try:
		yield
	finally:
		os.chdir(prevdir)

# Returns the builds that succeeded
def try_build(release_target, paths):
	good = set()
        test = ""
        if release_target.endswith("-test") or release_target.endswith("-test-src"):
            test = "--test"
	for path in paths:
		logging.info("Building specs in %s" %(path))
		with cd(path):
			tito_cmd = "tito release %s --arg=nosign %s" %(test, release_target)
			result = call(tito_cmd)
			if result == 0:
				good.add(path)
	return good

def clear_bucket(s3bucket):
	# Clear folder if it exists
	check_cmd = "s3cmd info %s" %(s3bucket)
	check_result = call(check_cmd)
	if(check_result == 12):
		pass
	elif(check_result == 0):
		clear_cmd = "s3cmd del -r %s" %(s3bucket)
		check_call(clear_cmd)
	else:
		raise Exception('Unknown bucket status')

def create_index(s3bucket):
	# Create the initial index
	index_upload_cmd = "s3cmd put index.html %s" %(s3bucket)
	check_call(index_upload_cmd)

def do_release(release_target, path):
	logging.info("Release target: %s" %(release_target))
	# get bucket we are going to clear
	s3bucket = tito_config.get(release_target,'s3cmd')
	clear_bucket(s3bucket)
	create_index(s3bucket)
	src_paths = set(glob(path + '/*/'))
	while True:
		logging.info("Attempting another round of builds")
		good_builds = try_build(release_target, src_paths)
		src_paths -= good_builds
		if len(good_builds) == 0 or len(src_paths) == 0:
			break

def release_repo(path, release_targets=[]):
        if not release_targets:
            expected_release_file = os.path.join(path, RELEASE_FILE)
            if not os.path.isfile(expected_release_file):
                    raise RuntimeError("No %s file found at path %s" % (RELEASE_FILE, path))
            release_targets = [line.rstrip('\n') for line in open(expected_release_file)]
	logging.info("In directory %s using the following release targets %s" % (path, release_targets))
	for release_target in release_targets:
		do_release(release_target, path)

if __name__ == "__main__":
        path = sys.argv[1]
	release_repo(path, sys.argv[2:])
