# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:31:39 2019

@author: it support
"""



import urllib
from bs4 import BeautifulSoup as bs
import ssl
import os
import requests
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
import sys
import re

class WIKI_CRAWLER():
    def __init__(self):
        self.url = input('Please enter url\n>')
        self.paragraphs = []
        self.links = []
        print('***WIKI_CRAWLER***')

    def get_response(self,url):
      return urllib.request.urlopen(url,context=ctx)

    def soup(self,response,parser='html.parser'):
      return bs(response,parser)
    
    def get_links(self):
      print('collecting links; please wait')
      soup = self.soup(self.get_response(self.url))('p')
      links = []
      for i in soup:
        links.append(i.find_all('a'))
      for i in links:
        for j in i:
          self.links.append(j.get('href'))
      for i in self.links:
        if i.startswith('#'):
          self.links.remove(i)
      self.links = ['https://en.wikipedia.org'+i for i in self.links]
      print('data successfully appended to WIKI_CRAWLER.links')   
        
    def get_paragraphs(self):
      print('collecting paragraphs data')
      soup = self.soup(self.get_response(self.url))('p')
      for i in soup:
        self.paragraphs.append(i.text)
      desired_length = int(input('enter desired length </={}\n>'.format(len(self.links))))
      if desired_length>len(self.links):
          sys.exit('Invalid search query')
      for i in self.links[:desired_length]:
        soup = self.soup(self.get_response(i))('p')
        for j in soup:
          self.paragraphs.append(j.text)
      print('data successfully appended to WIKI_CRAWLER.paragraphs')
  
