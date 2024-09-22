def fibonacci_recur(n):
    golden_ratio = (1 + (5) ** (1 / 2)) / 2
    if n == 0:
        return 0
    elif n == 1:
        return 1

    elif n == 2:
        return 1

    elif 3 <= n <= 78:
        return round(golden_ratio * fibonacci_recur(n - 1))

    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


print(fibonacci_recur(3))