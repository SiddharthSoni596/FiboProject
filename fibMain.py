#Title: fibonacci

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# done 1
print(fibonacci(35))


