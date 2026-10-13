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