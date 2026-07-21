name=input("enter the real name,agent:")
gadget=input("enter your favorite agent:")
agent_number=7
speed_rating=9.5
mission_count=12
height_m=1.65
is_active=True
print("name:",name,"-> type:",type(name))
print("gadget:",gadget,"->type:",type(agent_number))
print("speed rating :",speed_rating,"->type:",type(speed_rating))
print("mission count :",mission_count,"->type:",type(mission_count))
print("height(m) :",height_m,"->type:",type(height_m))
print("is active :",is_active,"->type:",type(is_active))
agent_number_text=str(agent_number)
mission_count_text=str(mission_count)
speed_rating_text=str(speed_rating)
status_text=str(is_active)
print("agent number as text: ",agent_number_text,"->type:",type(agent_number_text))
print("agent number as text: ",mission_count_text,"->type:",type(mission_count_text))
print("agent number as text: ",speed_rating_text,"->type:",type(speed_rating_text))
print("agent number as text: ",status_text,"->type:",type(status_text))
first_three=name[0:3]
last_letter=name[-1:]
code_name=first_three+last_letter
print(code_name)
reversed_gadget=gadget[::-1]
print("reversed gadget name:",reversed_gadget)







