nums = [0, 1, 0, 3, 12]
a = 0

for i in range(5):
    if nums[i] != 0:
        nums[a] = nums[i]
        a += 1
    if i >= a:
        nums[i] = 0

print(nums)
