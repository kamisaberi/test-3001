s = "abcdefghijklmnopqrswxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

username = "ali1 23"

b = True
for ch in username : 
    if ch not in s:
        b = False

print(b)
