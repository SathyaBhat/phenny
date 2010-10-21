#!/usr/bin/env python
"""
kick.py - Phenny URL shorten Module
Copyright 2008-9, Sathyajith, http://sathyabh.at

"""
def kick(phenny, input): 
   """Part the specified channel. This is an admin-only command."""
   if input.admin:
      # phenny.say(input)
      phenny.say('/kick #chip-india ' + input.group(2))
    
#      phenny.write(['KICK'], input.group(2))
kick.commands = ['kick']
kick.priority = 'low'
kick.example = '.kick example'

if __name__ == '__main__': 
   print __doc__.strip()
