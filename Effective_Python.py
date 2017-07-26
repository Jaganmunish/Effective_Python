
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
fl2 = [x*100 for x in ch if x >=3 if x <=10 if x %8 == 0]
print (fl2)

