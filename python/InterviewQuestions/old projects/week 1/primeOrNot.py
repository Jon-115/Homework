num = input("Enter a number. ")
num = int(num)
if num > 1:
	for i in range(2, int(num/2)+1):
		if (num % i) == 0:
			print("is not a prime number")
			break
	else:
		print("is a prime number")
else:
	print("is not a prime number")
