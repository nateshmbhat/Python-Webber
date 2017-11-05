import requests
import bs4 
import time
import urllib3
import smssender

class yifyer:
	def __init__(self):
		resp = requests.get('https://www.yify-torrent.org/') ;
		soup = bs4.BeautifulSoup(resp.text , 'html.parser') ;
		self.topseeds = soup.find(id='topseed').find_all('a') ;
		print(self.topseeds) ;



if(__name__=='__main__'):
	yify = yifyer() ;