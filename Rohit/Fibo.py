def fibonacci_sequence(n):
    a, b = 0, 1
    result = []
    while n > 0:
        result.append(a)
        a, b = b, a + b
        n -= 1
    return result
