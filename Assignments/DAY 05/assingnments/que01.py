import math

print("---- Math Module Demo ----")

# Constants
print("Pi:", math.pi)
print("Euler's number:", math.e)

# Power and roots
print("Power (2^5):", math.pow(2, 5))
print("Square root of 25:", math.sqrt(25))

# Trigonometric functions (input in radians)
angle = math.radians(30)
print("Sin(30°):", math.sin(angle))
print("Cos(30°):", math.cos(angle))
print("Tan(30°):", math.tan(angle))

# Logarithmic functions
print("Log base 10 of 100:", math.log10(100))
print("Natural log of e:", math.log(math.e))

# Rounding functions
print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))

# Factorial & GCD
print("Factorial of 5:", math.factorial(5))
print("GCD of 24 and 36:", math.gcd(24, 36))
