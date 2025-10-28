# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

def find_elements(seq1, seq2):
    return list(set(seq1) & set(seq2)), list(set(seq2) | set(seq1))

def main():
    seq1 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']
    seq2 = [3, 4, 5, 6, 7, 'c', 'd', 'e', 'f']
    same_elements, all_elements = find_elements(seq1, seq2)
    print(f'Wspólne: {same_elements} | Wszystkie: {all_elements}')

if __name__ == '__main__':
    main()