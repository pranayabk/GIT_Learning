### this here is a simple code file for learning git commands and version control.
height = {
    'John': 5.9,
    'Alice': 5.5,
    'Bob': 6.0,
    'Eve': 5.7
}
average_height = sum(height.values()) / len(height)
print(f"The average height is: {average_height:.2f} feet.")
who_is_tallest = max(height, key=height.get)
print(f"The tallest person is: {who_is_tallest} with a height of {height[who_is_tallest]:.2f} feet.")
def ft_in_decimal_to_cm(val: float) -> float:
    # Separate whole feet and inches from decimal format
    feet = int(val)
    inches = round((val - feet) * 10)
    
    # Calculate total inches and convert to cm
    total_inches = (feet * 12) + inches
    return round(total_inches * 2.54, 2)

# Example usage
heights = [5.0, 6.1, 5.11, 6.0]

for h in heights:
    print(f"{h} ft -> {ft_in_decimal_to_cm(h)} cm")