# Finding Numbers

# Read through and parse a file with text and numbers. Extract all the numbers in the file 
# and compute the sum of the numbers.

# Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt
# (There are 87 values with a sum=445822)
# Actual data: http://python-data.dr-chuck.net/regex_sum_201873.txt
# (There are 96 values and the sum ends with 156)

# These links open in a new window. Make sure to save the file into the same
# folder as you will be writing your Python program.

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using
# the re.findall(), looking for a regular expression of '[0-9]+' and then
# converting the extracted strings to integers and summing up the integers.



fname = input('Enter file:' )
if len(fname) < 1 : fname = "regex_sum_42.txt"
handle = open(fname)
#import regular expression module in your code
import re
#make sum '0'
sum = 0
#create outher loop to go through each file's line
for line in handle :
    line = line.rstrip()
    #use re.findall to look for numbers, one or more times
    numbers = re.findall('[0-9]+', line)
    #inner for loop to iterate each number
    for number in numbers:
        #convert 'numbers' to integers and put them into 'sum'
        sum = sum + int(number)
print(sum)
