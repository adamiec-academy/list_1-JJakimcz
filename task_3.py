def envelope(n):
    z=0
    a=0
    b=n+1
    print((2*n+1)*"*", end = '')
    print()
    for _ in range(n-1):
        print("*" + a * " " + "*" + b * " " + "*" + a * " " + "*")
        a=a+1
        b=b-2
    print("*" + (n-1) * " " + "*" + (n-1) * " " + "*") 
    for _ in range(n-1):
        a=a-1
        b=b+2
        print("*" + a * " " + "*" + b * " " + "*" + a * " " + "*")   
 
    print((2*n+1)*"*", end = '')
