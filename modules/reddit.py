#!/usr/bin/env python

"""
reddit.py - Phenny Reddit Module
Copyright 2010 Sathyajith
Licensed under the Eiffel Forum License 2.

http://sathyabh.at
TODO: Add support for sub reddit input
TODO: Implement caching
"""

import urllib
import xml.dom.minidom
import random

def reddit(phenny, input):
   reddit_url = 'http://www.reddit.com/.xml'
   reddit_rss = xml.dom.minidom.parse(urllib.urlopen(reddit_url))
   links_dom = reddit_rss.getElementsByTagName('guid')
   return_link = links_dom[random.randrange(0,9)].firstChild.nodeValue
  
   phenny.reply('Reddit link: '+ return_link )

reddit.commands = ['reddit']
reddit.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
