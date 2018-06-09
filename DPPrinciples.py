# O(n^2)
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


print(fib_recursive(40))


# O(n)
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


# O(n)
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




