def factorial(n):
    silnia = 1
    if n != 0:
        while n > 1:
            silnia = silnia * n
            n = n - 1
    return silnia


def report():
    for n in range(101):
        print(f"{n : >3}! is {len(str(factorial(n))) : >3} digits long")
