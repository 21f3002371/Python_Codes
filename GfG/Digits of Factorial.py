# Stirling Approximation
def factorial_digits_count(n):
    import math
    # Stirling’s approximation
    return int(n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2) + 1

count = factorial_digits_count(8430)
print("Approx number of digits in 8430! =", count)
