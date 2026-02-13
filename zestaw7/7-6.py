import random


def alternating_zeroes_and_ones_generator():
    while True:
        yield 0
        yield 1

def random_direction_generator():
    directions = ['N', 'S', 'E', 'W']

    while True:
        yield random.choice(directions)

def weekdays_generator():
    while True:
        for weekday in range(7):
            yield weekday

def main():
    generator_zeroes_and_ones = alternating_zeroes_and_ones_generator()
    generator_random_direction = random_direction_generator()
    generator_weekdays = weekdays_generator()

    print("Ciąg 0/1")
    for _ in range(10):
        print(next(generator_zeroes_and_ones), end=" ")

    print("\nBłądzenie przypadkowe")
    for _ in range(10):
        print(next(generator_random_direction), end=" ")

    print("\nDni tygodnia")
    for _ in range(10):
        print(next(generator_weekdays), end=" ")

if __name__ == "__main__":
    main()
