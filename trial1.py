# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:56:16 2019

@author: it support
"""
#link: https://en.wikipedia.org/wiki/Philosophy
#path: C:\Users\it support\Downloads\code3\webcrawler


import sys
import pandas as pd
path = input('Your Path')
sys.path.append(path)
import wikicrawler
x = wikicrawler.WIKI_CRAWLER()
x.get_links()
x.get_paragraphs()
df = pd.DataFrame(dict(zip(x.links[:5],x.paragraphs[:5])),index=range(5))

print(df)