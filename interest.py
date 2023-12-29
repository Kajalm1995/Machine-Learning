# Take P, N, R as input as user
P = float(input('Please enter Principal in INR:'))
N = float(input('Please enter number of years:'))
R = float(input('Please enter rate of interest in %p.a.:'))

# Calculate simple interest
I = P*N*R/100

# Calculate the total amount
A = P + I

# Print above results
print(f'simple interest:{I:.2f}INR')
print(f'total amount is:{A:.2f}INR')