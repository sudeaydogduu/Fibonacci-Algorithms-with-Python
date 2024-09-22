def fibonacci_recur_memo(n, F):
    golden_ratio = (1+(5)**(1/2)) / 2
    if F[n] == None:
        if n==0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        elif n == 2:
            return 1
        elif 3 <= n <= 78:
            F[n] = round(golden_ratio * fibonacci_recur_memo(n-1, F))
        else:
            return fibonacci_recur_memo(n - 1, F) + fibonacci_recur_memo(n - 2, F)
    return F[n]
n = 10
print(fibonacci_recur_memo(n,[None]*(n+1)))