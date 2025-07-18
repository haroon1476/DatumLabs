nums = [4,2,9,1,7,5]

min = nums[0]
max = nums[0]

for num in nums:
    if num < min:
        min = num
    if num > max:
        max = num


print(f"Max = {max}")
print(f"Min = {min}")            