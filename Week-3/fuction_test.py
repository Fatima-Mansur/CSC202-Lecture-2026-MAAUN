def calculate_percentage(score, max_score):
    """Calculates the percentage and returns it."""
    return (score / max_score) * 100

def print_result(name, percentage):
    if percentage >= 50:
        print(f"Congratulations {name}, you passed with {percentage}%!")
    else:
        print(f"Sorry {name}, you failed with {percentage}%.")

# Do it now: Call calculate_percentage() with a score of 8 out of 10. Pass the result into the print_result() function along with a candidate name.
score = 40
max_score = 100
name = "Anas"
percentage = calculate_percentage(score, max_score)
print_result(name, percentage)
print(f"Result: {percentage}%")
