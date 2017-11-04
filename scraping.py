import requests
import bs4
import urllib
import json
import re 

#LOAD THE REQURIED CREDENTIALS TO SEND THE MESSAGES FROM THE CONFIG FILE 
#----------------------------------->

with open("../config.json") as f:
	creds = json.load(f) ;

#----------------------------------->

username = creds.get('Natesh').get('number') ;
password = creds.get('Natesh').get('password') ; 

host_url = "http://site24.way2sms.com/Login1.action" ;

data = {'username' : username, 'password' : password} 

resp = requests.post(host_url , data = urllib.parse.urlencode(data) , headers={'Content-Type' :'application/x-www-form-urlencoded' , 'User-Agent': 'Mozilla/5.0 }'}) ;


 
mytoken = re.search("Token=([\w\d.]+)" , resp.text).group[1] ;
 