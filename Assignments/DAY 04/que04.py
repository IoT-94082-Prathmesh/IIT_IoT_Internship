def histogram(numbers):
    for num in numbers:
        print(f"{num}: " + "*" * num)


# User input
values = list(map(int, input("Enter integers separated by space: ").split()))

# Function call
histogram(values)
