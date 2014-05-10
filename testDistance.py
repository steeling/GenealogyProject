#!/usr/bin/python

import findDistance
from bs4 import BeautifulSoup
import re
f = open("temp.html", "r")
doc = f.read()
print findDistance.parse_doc(doc)


soup = BeautifulSoup(doc.lower())

temp = soup(text=re.compile(r'\b((1[4-9]\d\d)|(20((1[0-4])|(0\d))))\b'))