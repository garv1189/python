# Accept the number of terms in the Fibonacci sequence from the user
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Initialize the first two terms of the sequence
previous = 0
current = 1

# Print the first two terms
print(previous)
print(current)

# Generate the sequence up to the specified number of terms
for i in range(num_terms - 2):
    # Compute the next term of the sequence
    next_term = previous + current
    
    # Print the next term
    print(next_term)
    
    # Update the previous two terms
    previous = current
    current = next_term