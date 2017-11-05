import requests
import bs4 
import time
import urllib3
import smssender
import json

class yifyer:
	def __init__(self):
		resp = requests.get('https://www.yify-torrent.org/') ;
		self.soup = bs4.BeautifulSoup(resp.text , 'html.parser') ;

	def find_top_seeded_movies(self):
		self.topseeds = self.soup.find(id='topseed').find_all('a') ;
		topseeds = [] ;
		
		for i in self.topseeds:
			topseeds.append(i.text) ;

		for i in range(len(topseeds)):
			topseeds[i] = topseeds[i].strip('1080p').strip() ; 

		topseeds = list(set(topseeds)) ;
		


if(__name__=='__main__'):
	yify = yifyer() ;
	yify.find_top_seeded_movies() ;