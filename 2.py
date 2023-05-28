A = int(input("input A: "))

fib_prev = 0
fib_curr = 1
n = 2

while fib_curr < A:
    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next
    n += 1

if fib_curr == A:
    print(A, " is ", n, " in fib")
else:
    print('no')