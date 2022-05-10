#! /usr/bin/python3

import sys
import urllib
from bs4 import BeautifulSoup
from googlesearch import search

word = ""
try:
    word = sys.argv[1]
    for i in range(2, len(sys.argv)):
        word = word + " " + sys.argv[i]
except:
    print("No argument")
    sys.exit(-1)

try:
    searchResult = search(word + " wiki", lang = "en", num = 10, start = 0, stop = None, pause = 0)
except:
    print("search() failed")
    sys.exit(-1)

wiki = "wikipedia"
url = ""
for i in searchResult:
    if wiki in i:
        url = i
        break

try:
    f = urllib.request.urlopen(url)
except:
    print("urllib.request.urlopen failed")
    sys.exit(0)

html = f.read()
soup = BeautifulSoup(html, 'html.parser')


totalCharacters = 0
for tag in soup.findAll('p'):
    if not tag.get_text().isspace():
        print(tag.get_text())
        totalCharacters = totalCharacters + len(tag.get_text())
        if (totalCharacters > 1000):
            break
