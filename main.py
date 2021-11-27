import pyshorteners
url=input("enter url here")
s=pyshorteners.Shortener().tinyurl.short(url)
print("youtube shortner is",s)