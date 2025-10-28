# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.
# Przykładowy prostokąt składający się 2 × 4 pól ma postać:
#
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+

def generate_rectangle(width, height):
    width_part = "+"
    width_part += ''.join("---+" for _ in range(width))

    height_part = ""
    height_unit = "|"
    height_part += ''.join(f"{height_unit:4}" for i in range(width + 1))

    rectangle = ""
    for i in range(height):
        rectangle += width_part + "\n" + height_part + "\n"

    rectangle += width_part

    return rectangle


def main():
    rectangle = generate_rectangle(4, 2)
    print(rectangle)


if __name__ == "__main__":
    main()