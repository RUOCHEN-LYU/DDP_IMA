a = 66
b = 66
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

c = 200
d = 67
if d >c:
    print("d is greater than c")
elif d == c:
    print("d and c are equal")
else:
    print("c is greater than d")

e = 200
f = 67
if e >f: print("e is greater than f")

a = 200
b = 34
print("a") if a >b else print ("=") if a==b else print("b")

x = 12

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
