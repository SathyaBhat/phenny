#!/usr/bin/env python
"""
xubz_facepalm.py - Phenny URL shorten Module
Copyright 2008-9, Sathyajith, http://sathyabh.at

"""
def xubz_facepalm(phenny, input):
   irc_nick = input.group(2)


   if irc_nick.lower() in ('the_b0rg','sathyabhat'):
      message = "Borgs cannot be facepalm'd. YOU FAIL!! You get the facepalm! http://i.imgur.com/wuH1V.png"
      phenny.reply(message)
   elif irc_nick.lower() in ('captn_picard'):
      message = "Captain Picard INVENTED the facepalm! How DARE YOU!!"
      phenny.reply(message)
   else:
      message = "You deserve a xubz facepalm for that http://i.imgur.com/wuH1V.png " + irc_nick
      phenny.say(message)

xubz_facepalm.commands = ['xubz_facepalm']
xubz_facepalm.priority = 'high'

if __name__ == '__main__':
   print __doc__.strip()
