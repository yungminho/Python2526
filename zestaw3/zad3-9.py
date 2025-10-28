# Mamy daną listę sekwencji (listy lub krotki)
# różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
# spodziewany wynik [0,4,3,7,18].

def sequence_sum(sequence):
    return [sum(seq) for seq in sequence]

def main():
    sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    expected = [0,4,3,7,18]
    assert sequence_sum(sequence) == expected

if __name__ == "__main__":
    main()