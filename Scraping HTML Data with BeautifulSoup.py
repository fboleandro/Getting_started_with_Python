# Instructions here: https://pr4e.dr-chuck.com/tsugi/mod/python-data/index.php?PHPSESSID=f43514813233b4b30e299c1f9575ace6
# Scraping Numbers from HTML using BeautifulSoup. In this assignment you will 
# write a Python program similar to http://www.pythonlearn.com/code/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and 
# parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you 
# the sum for your testing and the other is the actual data you need to process for 
# the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_282735.html (Sum ends with 0)

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
total = 0
for span in spans:
    #Got a list of <span class="comments">97</span> 
    #First content of each span line is a number (like 97) 
    #Use function int() to get integers, and property .contents[0] the get first item (like 97). 
    #Get total. 
    total = total + int(span.contents[0])
print(total)
