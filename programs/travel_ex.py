travel_distance = input("How far would you like to travel, in miles? ")
# convert input to an integer
travel_distance = int(travel_distance)
if travel_distance < 3:
    print("You should walk")
elif travel_distance >= 3 and travel_distance < 300:
    print("You should drive")
elif travel_distance > 300:
    print("You should fly")
