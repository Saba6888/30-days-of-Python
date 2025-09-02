#Frequency counter using dictionary
def count_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(count_frequency("hello world"))
