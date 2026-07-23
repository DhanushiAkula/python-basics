temperature=int(input("enter the today's temperature in celsius:"))
if temperature<20:
    outfit="jacket"
    print("it is cold today")
    print("wear a",outfit)
else:
    outfit="t-shirt"
    print("it is warm today")
    print("wear a",outfit)
is_raining=input("it is raining today?(yes/no):")
if is_raining=="yes":
    print("bring the umberlla!")
wind_speed=int(input("enter the wind speed in km/h"))   
if wind_speed>30:
    needs_windbreaker="yes"
    print("it is windy today")
    print("wear a windbreaker over your",outfit)
has_puddles=input("are there puddles on the ground/(yes/no):")
if has_puddles=="yes":
    shoes="boots"
    print("the ground is wet")
    print("wear",shoes)
else:
    shoes="sneakers"
    print("the ground is dry")
    print("wear",shoes)
print("")
print("weather check complete!")
print("======= WEATHER CHECK COMPLETE==================")
print("temperature:",temperature)
print("outfit chosen:",outfit)
print("raining:",is_raining)
print("windbreaker neeeded:",needs_windbreaker)
print("shoes chosen:",shoes)
print("==================================")

