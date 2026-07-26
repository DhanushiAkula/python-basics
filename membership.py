print("enter the marks obtained in 5 subject")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
average=int(total/5)
validrange=range(0,101)
if average not in validrange:
    print("invalid input!")
elif average in range(91,101):
    print("your grade is a1!")
elif average in range(81,91):
    print("your grade is a2!")
elif average  in range(71,81):
    print("your grade is b1!")
elif average in range(61,71):
    print("your grade is b2!")
elif average not in range(51,61):
    print("your grade is c1!")
elif average not in range(41,61):
    print("your grade is c2!")
elif average not in range(33,41):
    print("your grade is d!")
elif average not in range(21,33):
    print("your grade is e1!")
elif average not in range(0,21):
    print("your grade is e2!")
