# Prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# The first few prime numbers are: 2, 3, 5, 7
starting_number = 1
ending_number = 20
print("This program will display all prime numbers between 1 and 200.")
print(f"Prime numbers between {starting_number} and {ending_number} are:")
print("initializing loop...")
for num in range(starting_number, ending_number + 1):
    if num > 1:  # Check if the number is greater than 1
        for i in range(2, num):  # Check for factors from 2 to num-1
            if (num % i) == 0:  # If num is divisible by any of these, it's not prime
                break
        else:  # This else corresponds to the for loop, it executes if the loop wasn't broken
            print(num)

# Make a function that checks if a number is prime and returns True or False. Then use this function to print all prime numbers between 1 and 100.
def prime_number_checker(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

to_check = 13
print(f"Is this number prime? {prime_number_checker(to_check)}")  # Example usage of the function


# Print all prime numbers between 1 and 100 using the prime_number_checker function
#for num in range(1, 101):
#    if prime_number_checker(num):
#        print(num)  