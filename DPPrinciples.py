# Important References
# https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
# https://www.youtube.com/watch?v=5dRGRueKU3M


# Overlapping subproblems: 3 approach

# O(2^n)
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


print(fib_recursive(40))


# O(n)  Efficient for larger input
def fib_memoize_or_top_down(n, mem):
    if mem[n] is not 0:
        return mem[n]
    else:
        mem[n] = fib_memoize_or_top_down(n-1, mem) + fib_memoize_or_top_down(n-2, mem)
        return mem[n]


n = 40
mem = [0] * (n+1)
mem[1] = 1
mem[2] = 1
print(fib_memoize_or_top_down(n, mem))


# O(n)  For simplicity and small input sizes
def fib_bottom_up(n):
    mem = [0] * (n+1)
    mem[1] = 1
    mem[2] = 1
    if n == 1 or n == 2:
        return 1

    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2]

    return mem[n]


print(fib_bottom_up(40))
