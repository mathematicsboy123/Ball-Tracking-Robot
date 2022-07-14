import math

def solve_triangle(a, b, c):
    pi = math.pi
    cosA = ((c*c) + (b*b) - (a*a)) / (2*(b)*(c))
    cosC = ((a*a) + (b*b) - (c*c)) / (2*(a)*(b))
    ans = [(math.acos(cosA))/(2*pi)*360, (math.acos(cosC))/(2*pi)*360]

    return ans

def solver(distance):
    arm2 = 13
    arm3 = 14
    base_angle = None
    top_angle = None
    angles = solve_triangle(arm3, arm2, distance)

    base_angle = angles[0]
    top_angle = angles[1]

    return [base_angle, top_angle + 3]

if __name__ == "__main__":
    ans = solver(10)
    print(ans)
