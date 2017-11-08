import requests
import bs4
import urllib
import json
import re 

#LOAD THE REQURIED CREDENTIALS TO SEND THE MESSAGES FROM THE CONFIG FILE 

class Error(Exception):
	pass ;
class Invalid_credentials(Error):
	def __init__(self , message):
		self.message = message ; 

#----------------------------------->
class smssender:

	def __init__(self ):		
		self.session = requests.Session() ;


	def login_to_way2sms(self  , username = '' , password=''):

		try:
			with open("../config.json") as f:
				creds = json.load(f) ;
			#----------------------------------->
			username = creds.get('way2sms_Natesh').get('number') ;
			password = creds.get('way2sms_Natesh').get('password') ; 

		except Exception as e:
			pass ; 


		host_url = "http://site24.way2sms.com/Login1.action" ;
		data = {'username' : username, 'password' : password} 
		resp = self.session.post(host_url , data = urllib.parse.urlencode(data) , headers={'Content-Type' :'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0'}) ;

		self.sessiontoken = re.search("Token=([\w\d.]+)" , resp.text)
		if(self.sessiontoken):
			self.sessiontoken = self.sessiontoken.group(1) ;
		else:
			raise Invalid_credentials ("Invalid phone number or password  ! ") ; 



	def send_sms(self , mobile = '' , message = '' ):

		if not mobile:mobile=input("Enter recipient phone number : ") ;
		if not message:message = input("Enter message : ") ;

		message_url = "http://site24.way2sms.com/smstoss.action" ;

		data = {
		'ssaction' : 'ss' , 
		'Token' : self.sessiontoken , 
		'mobile' : mobile , 
		'message' : message
		}

		resp = self.session.post(message_url , data  = urllib.parse.urlencode(data) , headers={'Content-Type' :'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0'}) ;


if(__name__=='__main__'):
	smssender = smssender() ; 
	smssender.login_to_way2sms() ; 
	smssender.send_sms() ;