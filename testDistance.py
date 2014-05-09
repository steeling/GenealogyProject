#!/usr/bin/python

import findDistance

f = open("temp.html", "r")
doc = f.read()
print findDistance.parse_doc(doc)