"""Quadratic Equation 
ax^2 + bx + c = 0
formula = 
b^2 - 4ac > 0 , real roots
b^2 - 4ac = 0, roots equal
b^2 - 4ac < 0, complex roots 
"""
import cmath

def solveQuadraticEquation(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return "Real roots:", root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return "Equal roots:", root
    else:
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return "Complex roots:", root1, root2

# Example usage:
a = 1
b = -3
c = 2
roots = solveQuadraticEquation(a, b, c)
print(*roots)
