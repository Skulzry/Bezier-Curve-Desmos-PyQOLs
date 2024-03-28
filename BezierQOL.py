import math
import sympy as sp

def IterationsQuery():
    try:
        return int(input("Iterations? "))
    except:
        return IterationsQuery()

def generate_bezier_x_expression(control_points):
    expression = ""
    n = len(control_points) - 1
    t = sp.symbols('t')

    for i in range(n + 1):
        coefficient = nCr(n, i)
        t_term = f"{t}^{i}" if i > 0 else "1"
        one_minus_t_term = f"(1 - {t})^{n-i}" if (n - i) > 0 else "1"
        control_point = f"t_{{a{i+1}x}}"  # Adjust index for control point naming
        bernstein_poly = f"{coefficient} \\cdot {t_term} \\cdot {one_minus_t_term} \\cdot {control_point}"
        if i < n:
            expression += f"{bernstein_poly} + "
        else:
            expression += bernstein_poly

    return expression


def generate_bezier_y_expression(control_points):
    expression = ""
    n = len(control_points) - 1
    t = sp.symbols('t')

    for i in range(n + 1):
        coefficient = nCr(n, i)
        t_term = f"{t}^{i}" if i > 0 else "1"
        one_minus_t_term = f"(1 - {t})^{n-i}" if (n - i) > 0 else "1"
        control_point = f"t_{{a{i+1}y}}"  # Adjust index for control point naming
        bernstein_poly = f"{coefficient} \\cdot {t_term} \\cdot {one_minus_t_term} \\cdot {control_point}"
        if i < n:
            expression += f"{bernstein_poly} + "
        else:
            expression += bernstein_poly

    return expression

def ittrLoop(ittr,j,letters):
    for i in range(0, ittr):
        print("p_{"+str(i+1)+letters[j]+"}=L_{erp}\left(p_{"+str(i+1)+letters[j-1]+"},p_{"+str(i+2)+letters[j-1]+"},T\\right)")
    if not ittr <= 1:
            ittrLoop(ittr-1,j+1,letters)

def ittrLnLoop(ittr,j,letters):
    for i in range(0, ittr):
        print("L_{ineFromPoints}\left(p_{"+str(i+1)+letters[j]+"}.x,p_{"+str(i+2)+letters[j]+"}.x,p_{"+str(i+1)+letters[j]+"}.y,p_{"+str(i+2)+letters[j]+"}.y,x,y\\right)")
    if not ittr <= 1:
            ittrLnLoop(ittr-1,j+1,letters)

def nCr(n, r):
    return math.comb(n, r)

iterations = IterationsQuery()
print("")
#with open("''Alphabet''.txt", "r") as f:
#        alphabet = f.read().split()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
control_points_x = []  # Example control points
control_points_y = []  # Example control points
for i in range(0, iterations):
    control_points_x.append(str(i))
    control_points_y.append(str(i))
bezier_expression_x = generate_bezier_x_expression(control_points_x)
bezier_expression_y = generate_bezier_y_expression(control_points_y)
print("B_{x}(t)="+bezier_expression_x)
print("")
print("B_{y}(t)="+bezier_expression_y)
print("")
for i in range(0, iterations):
    print("p_{"+str(i+1)+"a}=\\left(t_{a"+str(i+1)+"x},t_{a"+str(i+1)+"y}\\right)")
ittrLoop(iterations-1,1,alphabet)
print("")
for i in range(0, iterations-1):
    print("L_{ineFromPoints}\\left(t_{a"+str(i+1)+"x},t_{a"+str(i+2)+"x},t_{a"+str(i+1)+"y},t_{a"+str(i+2)+"y},x,y\\right)")
ittrLnLoop(iterations-2,1,alphabet)
print("")
for i in range(0, iterations):
    print("t_{a"+str(i+1)+"x}=0")
    print("t_{a"+str(i+1)+"y}=0")
