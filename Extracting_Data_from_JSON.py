#Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib 
#and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. 
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.


import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter – ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)
print('User count:', len(info))

tot = 0

for item in info["comments"] :
    number = int(item["count"])
    tot = tot + number
    print(tot)
