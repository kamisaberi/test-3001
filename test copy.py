a = 7
if a%2 == 0:
    b = a**2
else:
    b = a*2

print(b)

b = a**2 if a%2 == 0 else a*2
print(b)