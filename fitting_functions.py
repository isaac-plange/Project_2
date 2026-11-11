def linear(m,x,b):
    return m*x+b
def slope_units(x_units, y_units):
    if len(x_units) and len(y_units):
        y_units=y_units.rstrip('s')
        x_units=x_units.rstrip('s')
    return y_units+'/'+ x_units
def print_equation(m,b,y_units,x_units):
    s=slope_units(x_units,y_units)
    print('The equation of the line is y =',m,s,'x +',b,y_units)

    
