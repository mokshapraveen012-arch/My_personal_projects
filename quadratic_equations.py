
#basic calculator for quadratic equations
#Can't run complex number
import math

a=float(input("Enter the value for a: "))
b=float(input("Enter the value for b: "))
c=float(input("Enter the value for c: "))
if a==0:
    if b !=0:
        linear_root= -c/b
        print(f"Since a=0, hence this is a linear equation...x= {linear_root:.2f}:)")
    else:
        print("Invalid equation...a and b both cannot be equal to 0...*computer dies* ;_; :(")

else:
    discriminant= b**2-(4*a*c)
    if discriminant > 0:
        d= (-b+ math.sqrt(b**2-(4*a*c)))/(2*a)
        e = (-b- math.sqrt(b**2-(4*a*c)))/(2*a)
        print(f"Values of x are: {d:.2f}, or, {e:.2f} :)")
    elif discriminant == 0:
        f= -b/(2*a)
        print(f"x has only one value as it is a perfect square, x= {f:.2f} :)")
    else:
        print("Sorry this calculator doesn't work for imaginary numbers :(")