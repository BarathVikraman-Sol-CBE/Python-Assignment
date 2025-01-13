""" Program to find the roots of a quadratic equation """

# Import necessary modules
import math
import cmath

from typing import Tuple

def solve_quad(a:float, b:float, c:float) -> Tuple[float|None|complex ,float|None|complex] :
    """
    Function to solve quadratic equation.

    Args :
        a : value of a
        b : value of b
        c : value of c

    Returns :
        Roots of the quadratic equation if any
    """

    if a == 0.0 :
        print("Given Linear equation.Only quadratic equations are supported.")
        return None,None

    D : float = (b**2) - (4*a*c) # discriminant value

    if D > 0:
        root1 : float = (-b + math.sqrt(D)) / (2*a)
        root2 : float = (-b - math.sqrt(D)) / (2*a)
        return root1,root2
    elif D == 0:
        root : float = -b / (2*a)
        return root, 
    else:
        root1 : complex = (-b + cmath.sqrt(D)) / (2*a)
        root2 : complex = (-b - cmath.sqrt(D)) / (2*a)
        return root1,root2

def main() -> None:

    a : float = float(input("Enter the value of a : "))
    b : float = float(input("Enter the value of b : "))
    c : float = float(input("Enter the value of c : "))

    roots : Tuple[float,float] = solve_quad(a,b,c)

    print("The roots are", roots)


if __name__ == "__main__":
    main()        
