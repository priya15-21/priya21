num = [10, 5, 8, 12, 3]
a = 0
b = 0

for i in num:
	if i > a:
		b = a
		a = i
	elif i > b:
		b = i

print("first Largest:", a)
print("Second largest:", b)
		
