def fibonacci_iterative(n):
    golden_ratio = (1+(5)**(1/2)) / 2
    list_f = [None] * (n + 1)
    list_f[0] = 1
    list_f[1] = 1
    list_f[2] = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif 3 <= n <= 78:
        for i in range(3,n+1):
            list_f[i] = round(golden_ratio*list_f[i-1])
        return liste[n]
    else:
        for i in range(3, n + 1):
            result = list_f[0] + list_f[1]
            list_f[0] = list_f[1]
            list_f[1] = result
        return result


print(fibonacci_iterative(10))