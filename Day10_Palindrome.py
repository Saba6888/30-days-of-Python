def is_palindrome(num):
    if num < 2 or num > 10000:
        return "Number out of range! Please enter a number between 2 and 10,000."
    
    num_str = str(num)
    if num_str == num_str[::-1]:
        return f"{num} is a palindrome number."
    else:
        return f"{num} is not a palindrome number."

number = int(input("Enter a number between 2 and 10,000: "))
result = is_palindrome(number)
print(result)
