from math import sqrt

def parameters_circle(x1,y1,x2,y2,x3,y3):
# WHERE: 
# x1 = x-coordinate of point 1
# y1 = y-coordinate of point 1
# x2 = x-coordinate of point 2
# y2 = y-coordinate of point 2
# x3 = x-coordinate of point 3
# y3 = y-coordinate of point 3    
    
    #Solving for Parameters
    x12 = x1-x2
    x13 = x1-x3
    y12 = y1-y2
    y13 = y1-y3
    y31 = y3-y1
    y21 = y2-y1
    x31 = x3-x1
    x21 = x2-x1
    
    dx13 = (x1**2)-(x3**2)
    dy13 = (y1**2)-(y3**2)
    dx21 = (x2**2)-(x1**2)
    dy21 = (y2**2)-(y1**2)
    
    a = ((dx13*y12)+(dy13*y12)+(dx21*y13)+(dy21*y13)) // (2*((x31*y12)-(x21*y13)))
    b = ((dx13*x12)+(dy13*x12)+(dx21*x13)+(dy21*x13)) // (2*((y31*x12)-(y21*x13)))
    c = (-(x1**2)-(y1**2)-(2*a*x1)-(2*b*y1))
    
    #General eqn of circle: x^2 + y^2 + 2*a*x + 2*b*y + c = 0
    #Standard eqn of circle: (x^2 - h) + (y^2 - k) = r^2
    #Center:(h = -a, k = -b)
    h = -a
    k = -b
    
    #Radius
    r = round(sqrt((h**2)+(k**2)-c), 4)
    
    #Vector[D,E,F]
    D = a*2
    E = b*2
    F = c
    
    #Outputs
    print('Center: (',h,',',k,')')
    print('Radius: ', r)
    print('Vector [D,E,F]:',[D,E,F])