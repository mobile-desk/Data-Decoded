import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8]])

#get an element
print(a[1,0])


#all zero matrix
a = np.zeros((5,2))

print(f"Zero matrix {a}")


#all ones
a = np.ones((2,3))

print(f"all one matrix {a}")


#all x matrix
a = np.full((2,3), 3)

print(f"all x matrix {a}")

#copy shape from an existing matrix
b = np.full_like(a,3)
c = np.full(a.shape,3)

print(f'copied shape {b} and {c}')


#generating random decimal
a = np.random.rand(2,3)

print(f"random decimals{a}")

b = np.random.random_sample(a.shape)

print(f'random decimals with inherited shape {b}')


#generate random integer
a = np.random.randint(1, size=(2,3))
print(f'rand int {a}')
a = np.random.randint(1, 7, size=(2,3))
print(f'rand int wih end value {a}')


#identity matrix
c = np.identity(2)

print(f'identity matrix {c}')


a = np.array([[1,2], [3,4]])

print(np.linalg.det(a))

#reorganizing arrays
a = np.array([[1,2,3,4], [5,6,7,8]])
b = a.reshape((2,2,2))

print(f"reorganized = {b}")

#stacking

#vertical
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.vstack([a,b])
d = np.hstack([a,b])
print(f"vstack \n {c}")
print(f"hstack \n {d}")




###########################################################################################
#Range
a = np.arange(10, 100) #
print(f"range {a}")
a = np.arange(20, 100, 2) #
print(f"range {a}")


#shuffle an array
n = np.array([[1,2,3],[4,5,6]])

v = np.random.permutation(n)

print(v)

#load data from a file
x = np.genfromtxt("num.txt", delimiter=' ')
print(f'gotten from file {x}')


#change data type
print(x.dtype)
b = x.astype('int32')
print(b.dtype)


#boolean

a = np.array([40,20,10,5])

print(a>10)

#print only the values that are true
print(a[a>10])

a = np.array([[1, 5, 10], [20, 30, 40]])
print(np.any(a>10, axis=1))


#statistics
#generate an array of random numbers sampled from a standard normal distribution

b = np.random.randn(10)
print("statistics")
print(b)

#check mean

print(np.mean(b))

#check standard deviation
print(np.std(b))