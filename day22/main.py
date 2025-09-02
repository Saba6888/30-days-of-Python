#List comprehension with conditions
nums = [i for i in range(20) if i % 2 == 0 and i % 3 == 0]
print(nums)  # [0, 6, 12, 18]
