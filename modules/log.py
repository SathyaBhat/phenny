#!/usr/bin/env python
"""
log.py - Phenny chat logger + finder Module
Most of the below code has been recycled from Aditya VM's python-twitter-bot found at
http://code.google.com/p/python-twitter-bot/
"""
import time
import os
import urllib
import urllib2
import sys

def log(phenny, input): 
  log_text = input.group(2)
  log_time = time.strftime("%d-%m-%y %H:%M %Z")
  log_file = os.path.join(os.path.expanduser('~/.phenny'), 'favs.log')
#  log_file = 'favs.log'
  f = open(log_file,'a')
  f.write(input.nick + "(" +  log_time + ") " +log_text + "\n")
  f.close()
  
  phenny.reply(log_text[:10] + '... was logged! ')
   
log.commands = ['log']
log.priority = 'high'
log.example = '.log blargh'

def find_log(phenny, input):
    find_text = input.group(2)
    log_file = os.path.join(os.path.expanduser('~/.phenny'), 'favs.log')
    f = open(log_file,'r')
    found_count = 0
    max_count = 5
    found_text = ''
  #  paste_url = ''
    
    found = 1
    phenny.say('----------- Retrieving logs, please wait --------------')
    while True:
        curr_line = f.readline()
        if curr_line =='':
            break
        if curr_line.lower().find(find_text.lower()) != -1:
            if found_count < max_count:
               
                phenny.say(curr_line)
                found_count = found_count +1
                time.sleep(1)
                found_text = found_text + curr_line
            else:
              #  phenny.say(str(found_count) +  ' ' + str(max_count))
                found_count = found_count +1
                found = 1
                found_text = found_text + curr_line
    if found_count < max_count:
        max_count = found_count
    else:
        pastebin(phenny, found_text)
       
        
    if found_count == 0:
        phenny.say("Nothing found!")
    else:
        phenny.say("Showing " + str(max_count) + " of " + str(found_count) + " log(s). ")

find_log.commands = ['find_log']
find_log.priority = 'high'
find_log.example = '.find_log blargh'                

def pastebin(phenny, found_text):  
    
    api_url = 'http://pastebin.com/api_public.php'
   #  print >> sys.stderr, found_text
    
    post_text = { 'paste_code' : str(found_text) }
    post_text = urllib.urlencode(post_text)
    req = urllib2.Request(api_url,post_text)
    resp = urllib2.urlopen(req)
    paste_url = resp.read()
    phenny.say('Full logs for this keyword is available at ' + paste_url)
  # print >> sys.stderr, paste_url
    # return paste_url

       
if __name__ == '__main__': 
   print __doc__.strip()
