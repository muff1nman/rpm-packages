#!/usr/bin/env python2
from glob import glob
import build-rpm

paths = set(glob('*/'))
for path in paths:
	release_repo(path)
