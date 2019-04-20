#There are two types

#1.Generator function
def simpleGeneratorFun():
	yield 1
	yield 2

#2. Generator Object
x = simpleGeneratorFun() #x is a simple genertor object
print(x.__next__())
print(x.__next__())x`

#generator for fibonacci
def fib(n):
	a,b = 0,1

	while a<n:
		yield a
		a,b = b, a+b

x = fib(5)
print(x.__next__())
print(x.__next__())

print('Using loop')
for i in fib(5):
	print(i)