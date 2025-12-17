
conversions = [
    lambda tonnes: tonnes * 1000,                
    lambda kg: kg * 1000,                         
    lambda g: g * 1000,                            
    lambda mg: mg / 453592.37                   
]

# User input
tonnes = float(input("Enter weight in tonnes: "))

# Applying conversions step by step
kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

# Output
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")
