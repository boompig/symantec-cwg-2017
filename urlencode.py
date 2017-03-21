#!/usr/bin/env python
import urllib
import sys
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("--decode", action="store_true")
    args = parser.parse_args()
    with open(sys.argv[1]) as fp:
        contents = fp.read().strip()
    if contents.count("\n") > 0:
        print("error: found newlines in contents")
        sys.exit(1)
    if args.decode:
        print urllib.unquote(contents)
    else:
        print urllib.quote(contents)
