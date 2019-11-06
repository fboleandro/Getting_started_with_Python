#9.4 Write a program to read through the mbox-short.txt 
#and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.



fname = raw_input('Enter file name: ')
fhand = open(fname)
c = dict()
for line in fhand:
  if not line.startswith('From ') : continue
  pieces = line.split()
  email = pieces[1]
  c[email] = c.get(email,0) + 1

bigc = None
bige = None
for word in c:
  value = c[word]
  if bigc == None or value > bigc:
    bigw = word
    bigc = value

print (bigw, bigc)
