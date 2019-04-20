#Yield statement suspends function execution and sends a value back to the caller, but retains enough state to enable function 
#to resume where it is left off. When resumed, the function continues its execution immediately after the last yield run.

#yield is a generator
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

for value in simpleGeneratorFun():
	print(value)

#yield are used when we want to iterate over a sequence, but we don't want to store the 
#entire sequence in memory. See the following func

#find all the fact from 1 to n
def factorial(n):
	fact = []
	k = 1
	for i in range(1, n+1):
		k *= i
		fact.append(k)
	return fact

#using yield
#flow 27,28,29,30,31 -> 29,30,31 ...
def factorial2(n):
	k = 1
	for i in range(1,n+1):
		k*=i
		yield k