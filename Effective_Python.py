
# Effective Python 3.5

# Know to slice

a = 'Jagatheesh'

print (a[1:])   #agatheesh
print (a[::1])
print (a[::-1])
print (a[2:6])
print (a[1:10:2]) #Using Stride

# list comperhension

b = [1,2,3,4,5,6,7,8,9,10]

sqr = [x**2 for x in b] # Square Root
add = [x+10 for x in b] # Addition

# Map function in list comprehension

sqr_map = map(lambda x : x ** 2, a)

#sqmp = list(sqr_map)

print (sqr_map)

odd_cub = [i**3 for i in b if i % 3 == 0]

even_sqr = [i**2 for i in b if i % 2 == 0]

# Map function in list comperhension

#alt = map(lambda x : x ** 2, filter(lambda x: x % 2 == 0,b))
#assert alt_map == list(alt)

# Note : Avoid using more than two expresion in the list

#Excerise :

#mat = [[1,2,3,4,5],[3,4,5,6,7],[9,8,7,6,6,4]]

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

pr_list = [x for row in mat for x in row]

print (pr_list)

# Adding 10 for the conscutive numbers in the list

mat1 = [[1,2,3,4],[20,30,40,50],[100,390,510,21,200]]

lsch = [i+10 for val in mat1 for i in val]

# Condition & looping in list comperhension

ch = [1,2,3,4,5,6,7,8,8,9,10,12,42]

fl = [x for x in ch if x >=3 if x <=10]
fl1 = [x*100 for x in ch if x >=3 if x <=10]
fl2 = [x*100 for x in ch if x >=3 if x <=10 if x % 8 == 0]
print (fl2)

#list comperhension for large input

import os


os.chdir("C:\\Users\\sadhja02\\Documents\\Process Documents\\Python Practice\\Practice input")

#Find the lenght of the file

lent = [len (i) for i in open("Textfile.txt")] # List comprehension
print (lent)

lenof = (len (i) for i in open("Textfile.txt"))

print (next(lenof))

llist = [100,340,980,670,509,100,500]

genlis = [len(val)+ i for i in llist for val in open("Textfile.txt")]
print (genlis)

genlis1 = (len(val)+ 100 for val in open("Textfile.txt"))

print (next(genlis1))

gen = ((x, x**0.5) for x in llist)

gen = ((x **2) for x in llist)

#Enumerate

# bit = 0
#
# for i in range(64):
#     if randint(0,1):
#         bit |= 1<< i

name = ['Jagatheesh','Barathi','Gopi','Sabari','Viswa']

# for i in name:
#     print ('%s is Friends' % name)
#
# for i in range(len(name)):
#     name1 = name[i]
#     print ('%d: %s' % (i+1, name1))
#
# for i, name1 in enumerate(name):
#     print ('%d : %s' % (i+1,name1))

for item in enumerate(name):
    print (item)

# Zip

name = ['Jagatheesh','Barathi','Gopi','Sabari','Viswa']

lenth = [len(x) for x in name]
longname = None
maxlt = 0

for i in range(len(name)):
    count = lenth[i]
    if count > maxlt:
        longname = name[i]
        maxlt = count

print (longname)


for name,count in zip(name,lenth):
    if count > maxlt:
        longname = name
        maxlt = count


print (longname)

zls = [1,2,3,4,5,6]

zsl = ['one','two','three','four','five','six']

nezl = dict(zip(zls,zsl))

print (nezl)

