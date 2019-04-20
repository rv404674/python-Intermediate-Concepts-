#*args and **kwargs allows you to pass a variable number of arguements to a function.
#*args - allows you to pass a non keyword variable length arguement list to the function
#**kwargs - allows you to pass a keyworded length arguement to a function


def test_args(arg1, arg2, arg3):
	print("arg1", arg1)
	print("arg2", arg2)
	print("arg3", arg3)

args = ("two", 3, 5)
test_args(*args)

kwargs = {"arg3":3, "arg2":2, "arg1":1}
test_args(**kwargs)

def test_var_args(f_arg, *argv):
	print("first normal arg:", f_arg)
	for arg in argv:
		print("another arg through *argv:", arg)

test_var_args("rahul", 1,2,3)	

def greet_me(**kwargs):
	for key, value in kwargs.items():
		print("{} = {}".format(key, value))
greet_me(name="rahul")

#if you want to use all of them, then the order is
#some_func(fargs, *args, **kwargs)

#most common use case is function decorators