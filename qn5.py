# Question5:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the first 5 elements in the list.

def squre_values():
	mylst = list()
	for num in range(1,21):
		mylst.append(num**2)
	print(mylst[:5])

squre_values()


