import feedparser
from bs4 import BeautifulSoup
from lxml import html
import requests
import re

import csv

words = ['divorce', 'custody', 'meal ticket', 'behind closed doors', 'detail of the case emerged on a legal database', ]

hit_article = []
links_list = []
hits = []
hit_link = []

d = feedparser.parse('http://www.dailymail.co.uk/articles.rss')

for item in d.entries:
    link = ( item[ "link" ] )
    links_list.append(link)


for link in links_list:
    page = requests.get(link)
    tree = html.fromstring(page.content)

    soup = BeautifulSoup(page.text, 'html.parser')

    text = soup.find('body')
    text = text.text

    for word in words:
        regex = r"\b"+ re.escape(word) + r"\b"
        match = re.search(regex, text)
        if match:
            print (word, "________found")
            hits.append(word)
            hit_link.append(str(link))

match_dictionary = dict(zip(hit_link, hits))

print (match_dictionary)

w = csv.writer(open("output.csv", "w"))
for key, val in match_dictionary.items():
    w.writerow([key, val])






