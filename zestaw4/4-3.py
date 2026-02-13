# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    if n < 0:
        raise ValueError('silnia musi być dodatnie')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    for n in range(10):
        print(f'Factorial({n}) = {factorial(n)}')

if __name__ == '__main__':
    main()