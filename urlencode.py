#!/usr/bin/env python
import urllib
import sys
with open(sys.argv[1]) as fp:
    contents = fp.read().strip()
print urllib.quote(contents)
