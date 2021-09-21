#!/usr/bin/env python3

wind=int(input("What is the wind speed (MPH)? "))
if wind >= 157:
    print("Category 5")
elif wind >= 130:
    print("Category 4")
elif wind >= 111:
    print("Category 3")
elif wind >= 96:
    print("Category 2")
elif wind >= 74:
    print("Category 1")
else:
    print("That's just a little wind and not a hurricane")
