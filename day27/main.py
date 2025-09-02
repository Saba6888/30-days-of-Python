# Lambda + map+ filter
nums = list(range(10))
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, squared))
print(evens)
