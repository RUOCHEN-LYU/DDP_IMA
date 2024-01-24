x = "awesome "

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

y = "beautiful"

def myfunc():
    global y
    y = "attractive"

myfunc()

print("Python is " + y)

x = 5
print(type(x))

x = "May "
y = "John"
print(x + y)
