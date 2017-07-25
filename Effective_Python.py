
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









