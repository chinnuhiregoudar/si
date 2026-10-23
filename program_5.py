# Function to calculate simple interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Get input from the user
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

# Function call
result = simple_interest(p, r, t)

# Display the result
print("Simple Interest =", result)