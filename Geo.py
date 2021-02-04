import json
import urllib

#Stroring the parameters
serviceurl = "http://py4e-data.dr-chuck.net/json?"

#prompt for location

location = input("Enter the location:")

if len(location) < 1: break

#Setup the URL
url = serviceurl + urllib.parse.urlencode({'location': location})

print ("Retrieving http://...")
