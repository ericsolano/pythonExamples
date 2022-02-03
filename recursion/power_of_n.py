def power_of(a, n):
	if n == 0:
		p = 1
	else:
		p = a * power_of(a, n-1)		
	return p
	
print(power_of(2, 3))
print(power_of(4, 0))
print(power_of(4, 4))





