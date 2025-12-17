# Lambda conversion functions
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda ft: ft * 12
inches_to_cm = lambda inch: inch * 2.54


# Higher-order function
def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    print(f"{conversion_type}: {result}")


# Main program
def main():
    distance = float(input("Enter the distance value: "))

    print("\n--- Distance Conversions ---")
    distance_converter(distance, "Kilometers to Meters", km_to_m)
    distance_converter(distance, "Meters to Centimeters", m_to_cm)
    distance_converter(distance, "Centimeters to Millimeters", cm_to_mm)
    distance_converter(distance, "Feet to Inches", feet_to_inches)
    distance_converter(distance, "Inches to Centimeters", inches_to_cm)


# Run the program
main()
