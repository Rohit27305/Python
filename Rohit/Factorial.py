def factorial(ans , n):
    if n == 0:
        return ans

    ans = n * factorial(ans , n-1)
    return ans

n = int(input("Enter a number : "))

ans = 0
if n > 1:
    ans = factorial(1,n)

print(f"Factorial of {n} : {ans}")
