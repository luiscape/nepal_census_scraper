#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
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



def DownloadFile(url):
  '''Downloading files from an url.'''

  #
  # Downloading files in respective folders.
  #
  folder = url.split('/')[4] + '/'
  local_filename = 'download/' + folder + url.split('/')[-1]
  r = requests.get(url, stream=True)
  with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=1024): 
          if chunk: # filter out keep-alive new chunks
              f.write(chunk)
              f.flush()
  print 'File %s downloaded successfully.' % local_filename



def Main():
  '''Wrapper.'''
  l = ScrapeLinks('http://www.un.org.np/data-coll')

  for link in l:

    #
    # Parsing files. Not PDFs.
    #
    if os.path.splitext(link)[1] != '.pdf':
      # DownloadFile(link)
      print link


if __name__ == '__main__':
  Main()  
