#!/usr/bin/env python

import imdb

def movie(phenny, input):
   ia = imdb.IMDb()
   movie_title = input.group(2)
 # phenny.reply('Searched for: ' + movie_title)
   search_for = ia.search_movie(movie_title)
   movie_info = search_for[0]
   ia.update(movie_info)
   movie_rating = movie_info['rating']
   long_title = movie_info['long imdb title']
   phenny.reply(long_title + ' has a rating of ' + movie_rating )

movie.commands = ['movie']
movie.priority = 'medium'

if __name__ == '__main__': 
   print __doc__.strip()
