
x = int(input("What is the x coordinate of the  left jungle temple guard? "))
y = int(input("What is the y coordinate of the  left jungle temple guard? "))
z = int(input("What is the z coordinate of the  left jungle temple guard? "))

#Debug
after = False

x = x + 61
y = y - 44
z = z + 18

#Debug
after = True

coords_after: str = str(x) + " " + str(y) + " " + str(z)

print()
print("If you have the mod skytils, then use the following command to set the waypoint:")
print("/sthw set " + coords_after + " NAME_HERE")
print()
print("If you dont have the mod, here are the coordinates:")
print(coords_after)

wait = input("Press Enter to close this window...")
