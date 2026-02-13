# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
# która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie,
# czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_sequence(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)): total += sum_sequence(item)
        elif isinstance(item, (int, float)): total += item
    return total

def main():
    sequence = [1, [1, 2, [1, 2, [(1,[5,4]), [('a', 3.3, 4)]]]], 3, 4] # expected 31.3
    print(sum_sequence(sequence))

if __name__ == '__main__':
    main()