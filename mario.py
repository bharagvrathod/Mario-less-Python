from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        width = height + 1
        if height > 0 and height <= 8:
            break

    for i in range(1, height + 1):
        num_hashes = i
        num_spaces = width - num_hashes - 1

        print(" " * num_spaces, end="")
        print("#" * num_hashes)


if __name__ == "__main__":
    main()