#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

#
# Downloading the page and parsing the data.
#
def ScrapeLinks(url):
  '''Collecting HTML document and parsing the links.'''

  #
  # Requesting the site doc.
  #
  try:
    r = requests.get(url)

  except Exeption as e:
    if verbose:
      print e
    print 'Failed to connect with URL.'
  
  #
  # Extracting the links
  #
  soup = BeautifulSoup(r.text)
  link_list = []
  for link in soup.find_all('a'):
    a = link.get('href')
    link_list.append(url + a[1:])

  return link_list
    
#
# Parse files and topics.
#
def ParseFilesAndTopics():
  '''Parsing the file types and topics so we can create datasets on HDX.'''
  print 'nothing'

def Main():
  '''Wrapper.'''
  l = ScrapeLinks('http://www.un.org.np/data-coll')
  print len(l)



if __name__ == '__main__':
  Main()  
