# Wypisać w pętli liczby od 0 do 30
# z wyjątkiem liczb podzielnych przez 3.
# Użyć pętli for lub while.


def print_numbers(num_range, modulo):
    return " ".join(str(i) for i in range(num_range) if i % modulo != 0)


def main():
    expected = '1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29'
    assert print_numbers(30, 3) == expected

if __name__ == '__main__':
    main()