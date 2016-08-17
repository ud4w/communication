#!/usr/bin/env python

import urllib
import argparse

parser = argparse.ArgumentParser(usage="downloader.py [url]")
parser.add_argument("url")

args = parser.parse_args()

myfile = urllib.URLopener()
myfile.retrieve(args.url, "file.jpg")
