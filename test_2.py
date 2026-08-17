import random
secret=random.randint(1,50)
lives=1
while lives < 6:
    user_guess=int(input("enter the number(1,50):"))
    if user_guess==secret:
        print("it is correct")
        break

    elif user_guess<10:
        print("it is ice cold")
    elif user_guess<20:
        print("it is cold")
    elif user_guess<30:
        print("it is warm")
    elif user_guess<40:
        print("it is hot")
    else:
        print("it is valid")
    lives= lives+1


