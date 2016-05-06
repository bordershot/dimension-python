#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sort_function(url):
    match = re.search(r'http://.+/.+-(.+).jpg' , url)
#    if match:
#        print match.group(1)
#    else:
#        print 'No Match found'
    return match.group(1)

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  match = re.search(r'\S+_(\S+)', filename)
  if match:
      host = match.group(1)
  else:
      sys.stderr.write('ERROR: URL not found')
      sys.exit(1)
  f = open(filename, 'r')
  text = f.read()
  f.close()
  urls = re.findall(r'GET\s(.+puzzle.+jpg)\s', text)
  urls = sorted(urls)
  #remove dupes
  clean_urls = []
  while len(urls) > 0:
      current = urls.pop(0)
      current = 'http://' + host + current
      if current in clean_urls:
          continue
      else:
          clean_urls.append(current)
  # re-sort by second word
#  for url in clean_urls:
#      sort_function(url)
  return sorted(clean_urls, key=sort_function)
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
      os.mkdir(dest_dir)
  index_filename = os.path.join( dest_dir, 'index.html')
  index_file = open( index_filename, 'w')
  index_file.write('<verbatim>\n<html>\n<body>\n')
  counter = 0
  for url in img_urls:
      filename = 'img' + str(counter) + '.jpg'
      index_file.write('<img src="' + filename + '">')
      fqfilename = os.path.join( dest_dir, filename)
      urllib.urlretrieve(url, fqfilename)
      counter += 1
  
  index_file.write('\n</body>\n</html>\n')
  index_file.close()

  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
