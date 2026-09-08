nums = [1, 1, 2, 2, 3]
b = 1

for i in range(1, 5):
	if nums[i] != nums[i-1]:
		nums[b] = nums[i]
		b += 1

print(nums[:b])
