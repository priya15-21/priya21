nums = [2, 7, 11, 15]
target = 9

for i in range(4):
	for j in range(1, 4):
	       
		if nums[i] + nums[j] == target:
			print([i, j])
