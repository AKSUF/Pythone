def fibonacci(n):
    fib_series=[0,1]
    for i in range(2,n):
        next_term=fib_series[i-1]+fib_series[i-2]
        fib_series.append(next_term)
    return fib_series
num_terms=10
fibonacci_series=fibonacci(num_terms)
print("Fibonacci series up to",num_terms,"terms:")
for term in fibonacci_series:
    print(term)
