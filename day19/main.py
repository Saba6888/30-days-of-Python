#Fibonacci sequence generator
def fibonacci(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(10))
