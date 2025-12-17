# main.py
from geometry import area_circle, area_rectangle

print("1. Area of Circle")
print("2. Area of Rectangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius of the circle: "))
    print("Area of Circle:", area_circle(r))

elif choice == 2:
    l = float(input("Enter length of the rectangle: "))
    w = float(input("Enter width of the rectangle: "))
    print("Area of Rectangle:", area_rectangle(l, w))

else:
    print("Invalid choice")
