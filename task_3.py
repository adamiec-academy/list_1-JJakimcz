def envelope(n):
    a=0
    b=(2*n-3)
    print("*" * (2*n+1))
    for _ in range((n-1)):
        print("*"+ " " * a + "*" + " " * b + "*" + " " * a + "*")
        a=a+1
        b=b-2
    print("*"+ " " * a + "*" + " " * a +"*")
    for _ in range((n-1)):
        a=a-1
        b=b+2
        print("*"+ " " * a + "*" + " " * b + "*" + " " * a + "*")
    print("*" * (2*n+1))
