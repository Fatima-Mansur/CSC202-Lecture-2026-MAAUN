# Create your variables
candidate_name = 'Muhammad Hassan'         # String
student_id = 104576             # Integer
test_score = 88.45              # Float
has_completed_test = True     # Boolean
age = 25                        # Integer

# Do it now: Print a welcome message using an f-string (formatted string) that includes the candidate's name and ID.
#print(f"Welcome {candidate_name} (ID: {student_id}) to the examination portal.")

# Relational operators and control flow
# Relational operators: >, <, >=, <=, ==, !=

if age >= 16:
    # Check if the user is eligible to take the test based on age
    print(f"{candidate_name} is eligible to take the test.")
    if has_completed_test==True: # Checker, is left side of the equation is equal to the right side of the equation
        # Will be executed if the condition above is true
        print(f"Logged in student: {student_id}")
        print(f"{candidate_name} has completed the test with a score of {test_score}.")
        print("Congratulations on completing the test!")
    else:
        # Will be executed if the condition above is false
        print(f"{candidate_name} has not completed the test yet.")
        print("Please complete the test to see your score.")

else:
    print(f"{candidate_name} is not eligible to take the test. Minimum age requirement is 16.")
