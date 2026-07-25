print("=====smart school day planner=====")
print("answer 3 question quickly and i will plan your day!\n")
day=input("what day is it?(monday to sunday):").strip().capitalize()
weather=input("what is the weather?(sunny/rainy/cloudy):").strip().capitalize()
homework=input("Is your homework done?(yes/no):").strip().capitalize()
print()
print(f"====your plan for {day}====")
print("-"*35)
if day in("saturday","sunday"):
    print("day type:weekend-enjoy your free time!")
elif day=="monday":
    print("day type:first day of the week.pack your weekly planner.")
elif day=="friday":
    print("day type:last school day.return library books today.")
elif day in ("tuesday","wednesday","thursday"):
    print("day type:regular school day.stay focused!")
else:
    print("day type:day not recognised.please check the spelling")
if weather=="sunday" and homework=="yes":
    print("weather tip:pack your umbrella-it may get wet outside")
if not (homework=="yes"):
    print("homework:not done yet.finish it before going out!")
if weather=="rainy "and not (homework=="yes"):
    print("best plan:stay in,finish homework,then watch your favorite movie")
elif weather=="sunny" and homework=="yes" and not (day in("saterday","sunday") ):
    print("best plan:all set for great school day-you are prepared!")
else:
    print("best plan:take it one step at a time-you have got this")
print()
print("plan completed have a wonderful day !")
 

