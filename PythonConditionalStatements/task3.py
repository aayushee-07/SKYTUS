# simulate a traffic light red= stop yellow=wait green=go

light = input("Enter traffic light color: ")

if light == "red":
    print("Stop")

elif light == "yellow":
    print("Wait")

elif light == "green":
    print("Go")

else:
    print("Invalid color")