n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, "using a for loop:")
for i in range(1, n + 1):
    print(i)
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1
print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")