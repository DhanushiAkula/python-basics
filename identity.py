x=5
if(type(x)is int):
    print("True")
else:
    print("false")
x=5.5
if(type(x)is not float):
    print("true")
else:
    print("false")
x=90
y=90
if(x is y):
    print("x ix y same identity")
y=40
if(x is not y):
    print("x & y have different identity")
    