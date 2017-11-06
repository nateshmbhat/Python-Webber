import requests
import bs4
import urllib
import json
import re 

#LOAD THE REQURIED CREDENTIALS TO SEND THE MESSAGES FROM THE CONFIG FILE 
#----------------------------------->
class smssender:

	def __init__(self):
		with open("../config.json") as f:
			creds = json.load(f) ;
		#----------------------------------->
		self.username = creds.get('way2sms_Natesh').get('number') ;
		self.password = creds.get('way2sms_Natesh').get('password') ; 

		self.session = requests.Session() ;


	def login_to_way2sms(self ):
		username = self.username ; 
		password = self.password ;
		host_url = "http://site24.way2sms.com/Login1.action" ;
		data = {'username' : username, 'password' : password} 
		resp = self.session.post(host_url , data = urllib.parse.urlencode(data) , headers={'Content-Type' :'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0'}) ;

		self.sessiontoken = re.search("Token=([\w\d.]+)" , resp.text).group(1) ;


	def send_sms_using_way2sms(self , mobile = '' , message = '' ):

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
	smssender.send_sms_using_way2sms() ;