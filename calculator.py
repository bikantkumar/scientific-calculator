
# ADVANCED SCIENTIFIC CALCULATOR
# Python Mini Project

import math
import cmath
import statistics
import fractions
import sympy as sp

# Store previous answers and calculator settings
Ans = 0
PreAns = 0
angle_mode = "Deg"

# Main calculator menu
while True:
    print("\n========== SCIENTIFIC CALCULATOR ==========")
    print("1. Basic Arithmetic")
    print("2. Powers and Roots")
    print("3. Logarithms and Exponential")
    print("4. Trigonometry")
    print("5. Hyperbolic Functions")
    print("6. Factorial, nPr and nCr")
    print("7. Fractions")
    print("8. Statistics")
    print("9. Equation Solver")
    print("10. Integration and Differentiation")
    print("11. Complex Numbers")
    print("12. Matrix Operations")
    print("13. Number System Conversion")
    print("14. Prime Factorization")
    print("15. Function Table")
    print("16. Change Angle Mode")
    print("17. Recall Ans and PreAns")
    print("0. Exit")
    print("\n =================================")

    choice = input("Enter your choice: ")

    try:

        # Basic arithmetic and percentage
        if choice == "1":
            print("Use +, -, *, /, %, **, brackets, pi, Ans and PreAns")
            expression = input("Enter expression: ")
            expression = expression.replace("^", "**")

            result = eval(
                expression,
                {"__builtins__": {}},
                {"math": math, "pi": math.pi,
                 "e": math.e, "Ans": Ans, "PreAns": PreAns}
            )

            if isinstance(result, complex) or not math.isfinite(result):
                raise ValueError("Invalid result")

            PreAns, Ans = Ans, result
            print("Answer:", Ans)

        # Powers and roots
        elif choice == "2":
            x = float(input("Enter number: "))
            n = float(input("Enter root value: "))

            if n == 0:
                raise ValueError("Root cannot be zero")

            print("Square:", x ** 2)
            print("Cube:", x ** 3)
            print("Power (x^n):", x ** n)

            if x >= 0:
                print("Square Root:", math.sqrt(x))
            else:
                print("Square Root:", "Not a real number")

            print("Cube Root:", math.copysign(abs(x) ** (1/3), x))

            if x >= 0:
                print("Nth Root:", x ** (1/n))
            elif n.is_integer() and int(n) % 2 != 0:
                print("Nth Root:", -((-x) ** (1/n)))
            else:
                print("Nth Root: Not a real number")

        # Logarithms and exponential functions
        elif choice == "3":
            x = float(input("Enter positive number: "))

            if x <= 0:
                raise ValueError("Number must be positive")

            print("Log base 10:", math.log10(x))
            print("Natural Log:", math.log(x))
            print("Exponential e^x:", math.exp(x))
            print("Pi:", math.pi)
            print("Euler's Number:", math.e)

        # Trigonometric functions
        elif choice == "4":
            x = float(input("Enter angle: "))

            if angle_mode == "Deg":
                angle = math.radians(x)
            elif angle_mode == "Gra":
                angle = x * math.pi / 200
            else:
                angle = x

            print("Sin:", math.sin(angle))
            print("Cos:", math.cos(angle))
            print("Tan:", math.tan(angle))
            print("Sin Inverse:", math.asin(max(-1, min(1, math.sin(angle)))))
            print("Cos Inverse:", math.acos(max(-1, min(1, math.cos(angle)))))
            print("Tan Inverse:", math.atan(math.tan(angle)))

        # Hyperbolic functions
        elif choice == "5":
            x = float(input("Enter number: "))

            print("Sinh:", math.sinh(x))
            print("Cosh:", math.cosh(x))
            print("Tanh:", math.tanh(x))
            print("Asinh:", math.asinh(x))

            if x >= 1:
                print("Acosh:", math.acosh(x))
            else:
                print("Acosh: Invalid input")

            if abs(x) < 1:
                print("Atanh:", math.atanh(x))
            else:
                print("Atanh: Invalid input")

        # Factorial, permutation and combination
        elif choice == "6":
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))

            if n < 0 or r < 0 or r > n:
                raise ValueError("Invalid values")

            print("Factorial:", math.factorial(n))
            print("Permutation:", math.perm(n, r))
            print("Combination:", math.comb(n, r))

        # Fraction conversion
        elif choice == "7":
            x = input("Enter fraction or decimal: ")

            f = fractions.Fraction(x)
            print("Fraction:", f)
            print("Decimal:", float(f))
            print("Numerator:", f.numerator)
            print("Denominator:", f.denominator)

        # Statistical calculations
        elif choice == "8":
            data = list(map(float, input(
                "Enter numbers separated by spaces: "
            ).split()))

            if not data:
                raise ValueError("Enter at least one number")

            print("Mean:", statistics.mean(data))
            print("Median:", statistics.median(data))

            if len(data) > 1:
                print("Population SD:", statistics.pstdev(data))
                print("Sample SD:", statistics.stdev(data))

        # Quadratic and polynomial equation solver
        elif choice == "9":
            x = sp.symbols('x')
            expression = input("Enter equation (example: x**2-5*x+6): ")
            equation = sp.sympify(expression)
            print("Roots:", sp.solve(equation, x))

        # Integration and differentiation
        elif choice == "10":
            x = sp.symbols('x')
            expression = sp.sympify(input("Enter function in x: "))

            print("Differentiation:", sp.diff(expression, x))
            print("Integration:", sp.integrate(expression, x))

            a = float(input("Enter lower limit: "))
            b = float(input("Enter upper limit: "))

            print("Definite Integration:",
                  sp.integrate(expression, (x, a, b)))

        # Complex number calculations
        elif choice == "11":
            a = complex(input("Enter first complex number (a+bj): "))
            b = complex(input("Enter second complex number (a+bj): "))

            print("Addition:", a + b)
            print("Subtraction:", a - b)
            print("Multiplication:", a * b)
            print("Division:", a / b if b != 0 else "Cannot divide by zero")
            print("Magnitude:", abs(a))
            print("Conjugate:", a.conjugate())
            print("Polar Form:", cmath.polar(a))

        # Matrix operations
        elif choice == "12":
            print("Enter four values for each 2x2 matrix")

            A = sp.Matrix([
                [float(input("A11: ")), float(input("A12: "))],
                [float(input("A21: ")), float(input("A22: "))]
            ])

            B = sp.Matrix([
                [float(input("B11: ")), float(input("B12: "))],
                [float(input("B21: ")), float(input("B22: "))]
            ])

            print("Matrix Addition:\n", A + B)
            print("Matrix Multiplication:\n", A * B)
            print("Determinant of A:", A.det())

            if A.det() != 0:
                print("Inverse of A:\n", A.inv())
            else:
                print("Inverse does not exist")

        # Binary, octal, decimal and hexadecimal conversion
        elif choice == "13":
            n = int(input("Enter decimal integer: "))

            print("Binary:", bin(n))
            print("Octal:", oct(n))
            print("Hexadecimal:", hex(n))
            print("Decimal:", int(n))

        # Prime factorization
        elif choice == "14":
            n = int(input("Enter positive integer: "))

            if n < 1:
                raise ValueError("Enter a positive integer")

            print("Prime Factors:", sp.factorint(n))

        # Generate function table
        elif choice == "15":
            x = sp.symbols('x')
            expression = sp.sympify(input("Enter function f(x): "))
            start = float(input("Enter starting value: "))
            end = float(input("Enter ending value: "))
            step = float(input("Enter step size: "))

            if step <= 0 or end < start:
                raise ValueError("Invalid range or step")

            print("\nX\tF(X)")
            value = start

            while value <= end + step * 1e-10:
                answer = expression.subs(x, value)
                print(round(value, 4), "\t", answer.evalf())
                value += step

        # Change angle mode
        elif choice == "16":
            mode = input("Enter Deg, Rad or Gra: ").capitalize()

            if mode in ["Deg", "Rad", "Gra"]:
                angle_mode = mode
                print("Angle Mode Changed:", angle_mode)
            else:
                print("Invalid angle mode")

        # Recall previous answers
        elif choice == "17":
            print("Ans:", Ans)
            print("PreAns:", PreAns)

        # Exit calculator
        elif choice == "0":
            print("Thank you for using Scientific Calculator!")
            break

        else:
            print("Invalid choice. Try again.")

    except Exception as error:
        print("Calculation Error:", error)
