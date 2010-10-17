#!/usr/bin/env python
"""
short.py - Phenny URL shorten Module
Copyright 2008-9, Sathyajith, http://sathyabh.at

"""
import bitly

def short(phenny, input):
   api_user = 'sathyabhat'
   api_key = 'R_b53d9a2a031a098b5bb749288cedbe20'
   long_url = input.group(2)
 #  phenny.say(long_url)
   bitly_api = bitly.Api(api_user,api_key)
   short_url = bitly_api.shorten(long_url)
   phenny.reply('URL shortened to ' + short_url)

short.commands = ['short']
short.priority = 'high'

if __name__ == '__main__': 
   print __doc__.strip()
