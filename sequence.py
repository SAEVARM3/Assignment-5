n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 0
b = 1
c = 0
d = 0

for i in range(n):
    d = c
    c = b
    b = a
    a = b + c + d
    print(a)