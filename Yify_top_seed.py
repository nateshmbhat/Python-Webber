import socket
import requests
import bs4 
import time
import urllib
import smssender
import json
import pymysql 




class yifyer:
	def __init__(self):

		resp = '' ;

		while(not resp):
			try:
				resp = requests.get('https://www.yify-torrent.org/' , timeout = 3) ;

			except Exception as e :
				print(e) ;
				print("\nServer refused connection . \nSleeping for 5 seconds .....\nZZZzzzzzzzzz\n\n")  ;
				time.sleep(5) ;


		self.soup = bs4.BeautifulSoup(resp.text , 'html.parser') ;

	def find_top_seeded_movies(self):
		self.topseeds = self.soup.find(id='topseed').find_all('a') ;
		topseeds = [] ;
		
		for i in self.topseeds:
			topseeds.append(i.text) ;

		for i in range(len(topseeds)):
			topseeds[i] = topseeds[i].strip('1080p').strip() ; 

		topseeds = list(set(topseeds)) ;
		return topseeds ;


class databasing:
	def __init__(self):

		with open('../config.json') as f:
			dbdata = json.load(f).get("database_localhost") ; 



		dburl = dbdata.get("host") ;
		dbname = dbdata.get("databasename") ;
		password = '' ;

		try:
			self.con = pymysql.connect(host=dburl,
			user='root',
			password=password,
			db=dbname ,
			charset='utf8mb4',
			cursorclass=pymysql.cursors.DictCursor);

			with self.con.cursor() as cur:

				cmd = """create table if not exists project ( SlNo INT NOT NULL AUTO_INCREMENT  , Movie VARCHAR(100) ,PRIMARY KEY(SlNo) )"""	

				cur.execute(cmd) ;

			self.con.commit() ;

		except Exception as e:
			print(e) ;


	def inserttodb(self , topseeds ):
		try:
			with self.con.cursor() as cur:

				for i in topseeds:
					cmd = "insert Ignore into project (Movie) values(%s)" ;
					cur.execute(cmd , i) ;

			self.con.commit() ; 
			print("success") ;
		except Exception as e :
			print(e) ;







def check_internet_conn(timeout = 2):
	try:
		s = socket.socket() ;
		socket.setdefaulttimeout(timeout) ;
		s.connect(('8.8.8.8' ,53)) ;
		return True ;
	except Exception as e:
		print(e) ;
		return False ;





if(__name__=='__main__'):
	while(1):
		if not check_internet_conn(2):
			print("\nNo connection to the Internet .\nCheck if the Internet Connection is working properly")
			time.sleep(10) ;
		else: break ;

	dbobj = databasing() ;
	yify = yifyer() ;
	topseeds = yify.find_top_seeded_movies() ; 
	print(topseeds) ; 	
	dbobj.inserttodb(topseeds) ;