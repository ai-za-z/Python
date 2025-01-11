import math

# Get the angle from the user
angle_degrees = float(input("Enter the angle in degrees: "))

# Convert the angle to radians
angle_radians = math.radians(angle_degrees)

# Calculate sine, cosine, and tangent
sine = math.sin(angle_radians)
cosine = math.cos(angle_radians)
tangent = math.tan(angle_radians)

# Print the results
print(f"Sine of {angle_degrees} degrees: {sine}")
print(f"Cosine of {angle_degrees} degrees: {cosine}")
print(f"Tangent of {angle_degrees} degrees: {tangent}")