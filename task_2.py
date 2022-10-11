def kwadratszach(n,k):
    for _ in range(k):
        print("#", end = '')

def kwadratpusty(n,k):
    for _ in range(k):
        print(" ", end = '')

def l1(n,k):
    for _ in range(k):          
        print()
        for _ in range(n):
            kwadratszach(n,k)
            kwadratpusty(n,k)

def l2(n,k):
    for _ in range(k):          
        print()
        for _ in range(n):
            kwadratpusty(n,k)
            kwadratszach(n,k)

def chess_board(n,k):
    i=0
    for _ in range(n):
        i=i+1
        if i==n+1:
            break
        else:
            l1(n,k)
            l2(n,k)
