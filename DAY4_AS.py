n = int(input("Enter a positive integer n: "))
sum_of_evens = 0

for i in range(2, n+1, 2):  
    sum_of_evens += i

# Print the result
print(f"The sum of all even numbers between 1 and {n} is: {sum_of_evens}")