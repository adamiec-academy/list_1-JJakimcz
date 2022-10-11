def linia_gd(n):
    for _ in range(n):
        print(" ", end = '')
    for _ in range(n):
        print("*", end = '')
    print()
    
def linia_sr(n):
    for _ in range(n*3):
        print("*", end = '')
    print()

def cross(n):
    for _ in range(n):
        linia_gd(n)
    for _ in range(n):
        linia_sr(n)
    for _ in range(n):
        linia_gd(n)
    
