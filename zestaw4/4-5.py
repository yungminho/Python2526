# Napisać funkcję odwracanie(L, left, right)
# odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place).
# Rozważyć wersję iteracyjną i rekurencyjną.

def reverse_iterative(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def reverse_recursive(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_recursive(L, left + 1, right - 1)

def main():
    L1 = [1, 2, 3, 4, 5]
    L2 = [1, 2, 3, 4, 5]
    print(f'Lista: {L1} ')

    reverse_recursive(L1, 1, len(L1) - 2)
    print(f'Rekurencyjnie (first + 1, last - 1): {L1}')
    reverse_iterative(L2, 0, len(L2) - 1)
    print(f'Iteracyjnie (first, last): {L2}')

if __name__ == '__main__':
    main()