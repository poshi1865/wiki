#! /usr/bin/python3

import sys
import urllib
from bs4 import BeautifulSoup
from googlesearch import search

try:
    word = sys.argv[1]
except:
    print("No argument")
    sys.exit(0)

searchResult = search(word + " wiki", lang = "en", num = 10, start = 0, stop = None, pause = 0)

wiki = "wikipedia"
url = ""
for i in searchResult:
    if wiki in i:
        url = i
        break

f = urllib.request.urlopen(url)
html = f.read()
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.findAll('p'):
    if not tag.get_text().isspace():
        print(tag.get_text())
        break
