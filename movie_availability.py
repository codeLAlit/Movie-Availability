from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

http=urllib3.PoolManager()

base="https://in.bookmyshow.com/"


def isAvailable(event, city, name):
	name_modi=''.join(e for e in name if e.isalnum())
	response=http.request('GET', base+city+"/"+event)
	webPage=BeautifulSoup(response.data, "html.parser")
	res=webPage.findAll("div", attrs={"class":"card-title"})
	flag=0
	for mov in res:
		title=mov.text
		title_modi=''.join(e for e in title if e.isalnum())
		if (title_modi.lower() == name_modi.lower()):
			print("%s is Available" %(title)) 
			flag=1
			return True
			break;
	if(flag==0):
		print("Oops! It seems that it is not Available here. Try changing city name or Event type.")
		return False
		

print("MOVIE AVAILABILITY CHECKER")
print('Results from "Book My Show"')

city=input("Enter City Name:").lower()
event=input("Enter Event type \n movie events plays sports monuments activities: ").lower()
name=input("Enter Name of the %s:" %(event))


isAvailable(event, city, name)
