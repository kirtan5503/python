import math

def power(n):
    def implpower (x):
        return int(math.pow(x,n))
        return implpower

square=power(2)
cube=power(3)

print("Equation: ax^3 + bx^2 + cx + d")
a,b,c,d = input("Enter the values of a, b, c, d:").split('')


a,b,c,d = int(a) , int(b) , int (c) , int (d)
x = int(input("Enter the value of x:")) 
result=a*cube(x) + b*square(x) + c*x + d 
print("Result:",result)
