n = int(input("Input a binary number: "))
value = 0

for i in range(len(n)):
	digit = n.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)
