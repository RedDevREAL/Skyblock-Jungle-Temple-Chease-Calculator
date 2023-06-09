
try:
    x = int(input("\033[92mWhat is the x coordinate of the  left jungle temple guard? "))
    y = int(input("\033[92mWhat is the y coordinate of the  left jungle temple guard? "))
    z = int(input("\033[92mWhat is the z coordinate of the  left jungle temple guard? "))
except ValueError:
    print("\n\033[91mCoordinate must be Number!")
    input("Press Enter to close this window...")
    exit()

#Debug
done = False

x += 61
y -= 44
z += 18

#Debug
done = True

coords_after = str(x) + " " + str(y) + " " + str(z)

print()
print('If you have the mod "Skytils", then use the following command to set the waypoint:')
print("/sthw set " + coords_after + " NAME_HERE")
print()
print("If you dont have the mod, here are the coordinates:")
print(coords_after)

wait = input("Press Enter to close this window...")
