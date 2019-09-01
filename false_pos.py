def func(x):
    return (x * x * x - x * x + 2)


# Prints root of func(x) in interval [a, b]
def False_pose(a, b,tol):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result
    while abs(func(c))>tol:

        # Find the point that touches x axis
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Check if the above found point is root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ", '%.4f' % c)


a = float(input("Input a a value:")) # -200

b = float(input("Input a b value:")) # 300
# maxiter = int(input("Input the max iteration value:")) # 300
tol = float(input ("input the tolerance:"))
False_pose(a, b,tol)