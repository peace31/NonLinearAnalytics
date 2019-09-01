def func(x):
    return (float(1) / (1 + x * x))


# Function to perform calculations
def simpson83(a, b, n):
    interval_size = (float(b - a) / n)
    sum = func(a) + func(b)

    # Calculates value till integral limit
    for i in range(1, n):
        if (i % 3 == 0):
            sum = sum + 2 * func(a + i * interval_size)
        else:
            sum = sum + 3 * func(a + i * interval_size)

    return ((float(3 * interval_size) / 8) * sum)


a = float(input("Input a value:"))#1
b = float(input("Input b value:"))# 10
n = int(input("Input n value:"))# 10

integral_res = simpson83(a, b, n)

# rounding the final answer to 6 decimal places
print(round(integral_res, 6))