#!/usr/bin/env python
"""
xubz_facepalm.py - Phenny URL shorten Module
Copyright 2008-9, Sathyajith, http://sathyabh.at

"""
def xubz_facepalm(phenny, input):
   irc_nick = input.group(2)
   message = 'You deserve a xubz facepalm for that http://i.imgur.com/wuH1V.png ' + irc_nick
   phenny.say(message)

xubz_facepalm.commands = ['xubz_facepalm']
xubz_facepalm.priority = 'high'

if __name__ == '__main__':
   print __doc__.strip()
