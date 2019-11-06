#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fname = input('Enter file name: ')
if len(fname) < 1 : fname = "filex.txt"
fhand = open(fname)
c = dict()

for line in fhand:
    if not line.startswith('From ') : continue
    pieces = line.split()
    time = pieces[5]
    parts = time.split(':')
    hour = parts[0]
    c[hour] = c.get(hour,0) + 1
ls = list()

for key, val in c.items() :
    newtup = (key, val)
    ls.append(newtup)
ls = sorted(ls)
for key, val in ls :
    print(key,val)
