import time

start = time.time()

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(35))

end = time.time()


print("Time consumed :",int(end)-int(start)," secs" )
