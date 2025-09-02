# File read and write
with open("sample.txt", "w") as f:
    f.write("Hello, Saba!\nLet's build cool stuff.")

with open("sample.txt", "r") as f:
    print(f.read())
