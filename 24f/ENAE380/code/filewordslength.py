def count_string_lengths(strings):
    length_counts = {}

    # Iterate over each string in the list
    for s in strings:
        length = len(s)  # Get the length of the string
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    # Print the results
    for length in sorted(length_counts):
        print(f"{length}: {length_counts[length]}")


if __name__ == "__main__":
    with open("cipher.txt") as file:
        words = file.read().split(" ")

    count_string_lengths(words)
