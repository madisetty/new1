val = input("Enter a value: ")
num = 2
total = 0
while total!=val:
	for i in range(2,num):
		if num%i == 0:
			num += 1
			break
	else:
			num += 1
			total += 1
print "the num of {} is {}".format(total,num)
