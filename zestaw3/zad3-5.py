# Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.
#
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12

def measure_generator(length):
    measure = '|'
    measure += ''.join('....|' for i in range(length))
    numbers = '0'
    numbers += ''.join(f'{i+1:5}' for i in range(length))

    return f'{measure}\n{numbers}'

def main():
    print(measure_generator(30))

if __name__ == '__main__':
    main()