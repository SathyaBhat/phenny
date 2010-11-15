#!/usr/bin/env python
"""
whois.py - Phenny Module to fetch profile URL

"""

import os, pickle

def whois(phenny, input): 
  irc_nick = input.group(2)
  find_profile(phenny, irc_nick)
   
whois.commands = ['whois']
whois.priority = 'medium'
whois.example = '.whois blargh'

def find_profile(phenny, irc_nick):
  try:
    maps_dict = pickle.load(open(os.path.join(os.path.expanduser('~/.phenny'),'maps'),'rb'))
  except IOError:
    phenny.reply("No profiles available!")
  else:
    try:
      chip_profile = maps_dict[irc_nick]
    except KeyError:
        message = "Chip Profile for " + irc_nick + " not found!"
        phenny.reply(message)
    else:
        message = irc_nick + "'s Chip Profile is " + chip_profile
        phenny.reply(message)
       
if __name__ == '__main__': 
   print __doc__.strip()
