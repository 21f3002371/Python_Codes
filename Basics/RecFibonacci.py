
def fibonaccisequence(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fibonaccisequence(n-1)+ fibonaccisequence(n-2))
n = int(input())
Fibo = [fibonaccisequence(i) for i in range(n)]
print(Fibo)