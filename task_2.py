def chess_board(n,k):

    for _ in range(n):
        for _ in range(k):
            for _ in range(n):
                print((" " * k) + ("#" * k), end="")
            print()

        for _ in range(k):
            for _ in range(n):    
                print(("#" * k) + (" " * k), end="")
            print()
