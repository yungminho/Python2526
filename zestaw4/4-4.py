# Napisać iteracyjną wersję funkcji fibonacci(n)
# obliczającej n-ty wyraz ciągu Fibonacciego.

def fib(n):
    if n < 0:
        raise ValueError('liczba musi być dodatnia')
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def main():
    for n in range(0, 20):
        print(f'{n}: {fib(n)}')
if __name__ == '__main__':
    main()