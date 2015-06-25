#!/usr/bin/env python

import fileinput
import re
import sys

def url_sub(matches):
	url = matches.group(1).lower()

	if url.endswith('wiki'):
		return url + '/home.html)'
	else:
		return url + '.html)'

for line in fileinput.input():
	sys.stdout.write(re.sub('https:\/\/github\.com\/compomics([^.]*)\)', url_sub, line))