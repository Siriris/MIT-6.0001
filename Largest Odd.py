x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x>y>z:
        print("The largest odd number is ", x)
    elif y>z:
        print("The largest odd number is ", y)
    else:
        print("The largest odd number is ", z)
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x>y:
        print("The largest odd number is ", x)
    else:
        print("The largest odd number is ", y)
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x>z:
        print("The largest odd number is ", x)
    else:
        print("The largest odd number is ", z)
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y>z:
        print("The largest odd number is ", y)
    else:
        print("The largest odd number is ", z)
elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    print("The largest odd number is ", x)
elif x%2 == 0 and y%2 != 0 and z%2 == 0:
    print("The largest odd number is ", y)
elif x%2 == 0 and y%2 == 0 and z%2 != 0:
    print("The largest odd number is ", z)
else:
    print("None of the numbers entered are odd.")