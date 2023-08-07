#simple but effective URL shortener

import pyshorteners

url = input("enter url: \n")

print("Url after shortening: ",pyshorteners.Shortener().tinyurl.short(url))