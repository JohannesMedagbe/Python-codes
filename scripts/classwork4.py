def compute_salary(paste_sales, powder_sales, name):
    """Compute the total monthly salary of salesman provided paste_sales, powder_sales and names. Retainer, commisions on paste and powder are constant.
    """
    retainer=25000
    com_paste=0.1
    com_powder=0.2
    salary= retainer + paste_sales*com_paste + powder_sales*com_powder
    return name, salary

def compute_salary2(paste_sales, powder_sales):
    """Compute the total monthly salary of salesman provided paste_sales, powder_sales and names. Retainer, commisions on paste and powder are constant.
    """
    retainer=25000
    com_paste=0.1
    com_powder=0.2
    name=input("Enter the salesman name:")
    salary= retainer + paste_sales*com_paste + powder_sales*com_powder
    return name, salary

def is_triangle(a, b, c):
    """
    Check if lengths a, b, and c can form a degenerate triangle by checking if greatest is inferior or equal to the sum of the others
    """
    maxi_length=max(a, b, c)
    if maxi_length==a:
        return maxi_length<=b+c
    elif maxi_length==b:
        return maxi_length<=a+c
    elif maxi_length==c:
        return maxi_length<=b+c

def input_triangle(is_triangle):
    """
    Get lengths from the keyboard and check if they can from triangle using is_triangle
    """
    x=input("Enter your sticks lengths:")
    y=x.split()
    z=[]
    for i in y:
        j=int(float(i))
        z.append(j)
    a, b, c = z
    print(a)
    print(b)
    print(c)
    return is_triangle(a, b, c)

