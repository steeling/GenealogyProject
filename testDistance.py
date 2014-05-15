#!/usr/bin/python

from bs4 import BeautifulSoup
import re
f = open("test.html", "r")
doc = f.read()
soup = BeautifulSoup(doc.lower())
temp = soup(text=re.compile(r'\b((1[4-9]\d\d)|(20((1[0-4])|(0\d))))\b'))