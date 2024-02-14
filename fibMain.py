#Title: fibonacci

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# tryin to merge
# done 2 in pandey feature branch
print(fibonacci(35))


