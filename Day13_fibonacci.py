def fibonacci_sequence(limit):
    sequence=[]
    a,b=0,1

    while a<=limit:
        sequence.append(a)
        a,b=b,a+b
    return sequence

#User input
limit=int(input("Enter the sequence limit: "))

#output
fibonacci_sequence=fibonacci_sequence(limit)
print(f"fibonacci sequence up to {limit}:{fibonacci_sequence}")
