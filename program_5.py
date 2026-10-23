import sys

# Function to calculate simple interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Get values from command-line arguments
p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

# Function call
result = simple_interest(p, r, t)

# Display the result
print("Simple Interest =", result)