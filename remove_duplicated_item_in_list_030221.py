#!/usr/bin/python

import sys
import mymodule030221

# from optparse import OptionParser
# 
# parser=OptionParser()
# 
# parser.add_option("-f", "--file", action="store", type="string", dest="file", help="<file>")
# 
# (options, args)=parser.parse_args()
# 
# if options.file == None:
#   print("Please use --help for options")
#   sys.exit(1)
# else:
#   m=open("item", "ro")
#   print(m.read())  

class weekend():
  time_off="Yes, Time off"
  house_clean="Yes, house_clean"

  def __init__(self, whichday, dowhat):
    self.whichday=whichday
    self.dowhat=dowhat

  def location(self, where):
    print('Activity like ' + self.dowhat + ' at ' + where + ' at ' + self.whichday + ' is pretty relax ')

w1=weekend('Sat', 'Hiking')
print(w1.dowhat)

w1.location('Lake Chabot')

# dict

thisdict={
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

for a in thisdict:
  print(a)

for b in thisdict:
  print(thisdict[b])

for c in thisdict.keys():
  print(c)

for d in thisdict.values():
  print(d)
  
for e,f in thisdict.items():
  print(e,f)

# invert dict

invert={}

for g in thisdict:
  invert[thisdict[g]]=g

print(invert)

# adding key item

thisdict["Thurs"]="Four"

print(thisdict)

# pop item using dict pop method

thisdict.pop("Wed")

print(thisdict)

# list

thatlist=["one", "two", "three"]

for h in thatlist:
  print(h)

# append list on top of another

i=["A", "B", "C"]
j=["D", "E", "F"]

for k in j:
  i.append(k)

print(i)

# function

def hello(name):
  print("Your name is " + name)

hello("Jordan")

# running method from module

mymodule030221.greeting("Dubin")

# open file and read it

l=open("item", "ro")
print(l.read())

# remove duplicated items in list

lista=[1, 3, 4, 3, 2, 4, 4, 5]
print("original list is "  +str(lista) )
final=[]

for n in lista:
  if n not in final:
    final.append(n)

print("after removing duplicated list becomes " +str(final) )
