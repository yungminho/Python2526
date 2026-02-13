# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją,
# wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):
    flattened = []
    for item in sequence:
        if isinstance(item, (list, tuple)): flattened.extend(flatten(item))
        else: flattened.append(item)

    return flattened

def main():
    sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
    print(flatten(sequence))

if __name__ == '__main__':
    main()