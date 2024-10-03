# Vai Srivastava - 0106

import random
import time


class Lab2(object):
    def bubble_sort(self, my_list):
        """
        implements bubble sort to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of unsorted elements

        Returns
        -------
        list
            sorted list in ascending order
        """
        n = len(my_list)
        # loop through list
        for i in range(n):
            # swap check
            swapped = False
            # final set is sorted, so skip
            for j in range(0, n - i - 1):
                # swap if j+1>j
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    swapped = True
                # if there's nothing left to swap, then we are done
            if not swapped:
                break
        return my_list

    def selection_sort(self, my_list):
        """
        implements selection sort to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of unsorted elements

        Returns
        -------
        list
            sorted list in ascending order
        """
        n = len(my_list)
        # loop through list
        for i in range(n):
            # set current element as minimum
            min_index = i
            # find minimum in unsorted part
            for j in range(i + 1, n):
                if my_list[j] < my_list[min_index]:
                    min_index = j
            # swap minimum with first unsorted element
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
        return my_list

    def insertion_sort(self, my_list):
        """
        implements insertion sort to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of unsorted elements

        Returns
        -------
        list
            sorted list in ascending order
        """
        # loop through list starting from index 1
        for i in range(1, len(my_list)):
            key = my_list[i]
            # shift elements greater than key to the right
            j = i - 1
            while j >= 0 and key < my_list[j]:
                my_list[j + 1] = my_list[j]
                j -= 1
            my_list[j + 1] = key
        return my_list

    def merge_sort(self, my_list):
        """
        implements merge sort to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of unsorted elements

        Returns
        -------
        list
            sorted list in ascending order
        """
        if len(my_list) > 1:
            # find the middle index
            mid = len(my_list) // 2
            # split list into left and right halves
            left_half = my_list[:mid]
            right_half = my_list[mid:]

            # recursively sort both halves
            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            # merge sorted halves
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    my_list[k] = left_half[i]
                    i += 1
                else:
                    my_list[k] = right_half[j]
                    j += 1
                k += 1

            # copy remaining elements from left_half
            while i < len(left_half):
                my_list[k] = left_half[i]
                i += 1
                k += 1

            # copy remaining elements from right_half
            while j < len(right_half):
                my_list[k] = right_half[j]
                j += 1
                k += 1

        return my_list

    def sorting_test(self):
        """
        runs sorting tests for different algorithms on arrays of varying sizes.

        Returns
        -------
        None
            the results are printed to the console and saved in "SortingTests.csv".
        """

        # array sizes to test
        arr_sizes = [8, 200, 500, 1000, 10000]

        # sorting functions, their names, and execution times
        sorts = {
            "funcs": [  # sorting functions
                self.bubble_sort,
                self.selection_sort,
                self.insertion_sort,
                self.merge_sort,
            ],
            "names": [  # function names
                "Bubble Sort",
                "Selection Sort",
                "Insertion Sort",
                "Merge Sort",
            ],
            "times": [
                0.0,
                0.0,
                0.0,
                0.0,
            ],  # execution times
        }

        # open CSV file for writing results
        with open("SortingTests.csv", "w") as file:
            # write sorting names to CSV
            names = str(",").join(sorts["names"])
            print(names)
            file.write(names + str("\n"))

            # run 100 tests
            for test_num in range(100):
                print("Test Number: " + str(test_num + 1))

                # test sorting functions on arrays of different sizes
                for size in arr_sizes:
                    # create random array of given size
                    arr = [random.randint(0, size) for _ in range(size)]

                    # time each sorting function
                    for i in range(len(sorts["funcs"])):
                        start = time.time()
                        sorted = sorts["funcs"][i](arr.copy())
                        end = time.time()
                        sorts["times"][i] = float(end - start)

                    # write times to CSV
                    tests = str(",").join(map(str, sorts["times"]))
                    print(tests)
                    file.write(tests + str("\n"))

    def readFile(self, filename):
        """
        reads a file of numbers, sorts them using merge sort, and writes the sorted numbers to "SortedNumbers.txt".

        Parameters
        ----------
        filename : str
            name of the file to read from (should contain one number per line)
        """
        # open input file
        with open(filename) as file_in:
            # read numbers from file, skipping first line
            nums = [int(x) for x in file_in.readlines()[1:]]

        # sort numbers using merge_sort
        sorted = self.merge_sort(nums)

        # open output file
        with open("SortedNumbers.txt", "w") as file_out:
            # write label "Sorted Numbers"
            file_out.write("Sorted Numbers\n")

            # prepare sorted numbers with newlines
            sorted_out = [num + str("\n") for num in list(map(str, sorted))]

            # write sorted numbers to file
            file_out.writelines(sorted_out)

    def vigenere(self):
        """
        encodes a plaintext message using the Vigenère cipher with a keyword.

        Returns
        -------
        None
            the encoded message is printed to the console.
        """
        plaintext = input("Provide plaintext message:\n")
        keyword = input("Provide keyword:\n")

        # store encoded characters
        ciphertext = []

        # position in keyword
        keyword_index = 0

        # iterate over plaintext characters
        for p in plaintext:
            if p.isalpha():
                # get current keyword character
                k = keyword[keyword_index % len(keyword)]
                # encode character
                encoded_char = (
                    lambda p, k: chr(
                        ((ord(p) - ord("A") + ord(k) - ord("A")) % 26) + ord("A")
                    )
                )(p.upper(), k.upper())
                ciphertext.append(encoded_char)
                # increment keyword index
                keyword_index += 1
            else:
                # keep non-alphabetic characters
                ciphertext.append(p)

        # print encoded message
        print("".join(ciphertext).lower())

    def decrypt(self):
        """
        attempts to decrypt a Vigenère cipher using words from a dictionary.

        Returns
        -------
        str
            the decrypted message, or None if no valid decryption was found.
        """

        # load cipher text and valid words
        with open("cipher.txt") as cipher, open("validwords.txt") as valid:
            cipher_text = cipher.read()
            keywords = set(word.lower() for word in valid.read().splitlines())

        # try each keyword
        for keyword in keywords:
            decrypted_text = []
            keyword_index = 0

            # decrypt cipher text with current keyword
            for char in cipher_text:
                if char.isalpha():
                    # get current keyword character
                    key_char = keyword[keyword_index % len(keyword)].upper()
                    # decrypt character
                    decoded_char = chr(
                        ((ord(char.upper()) - ord(key_char) + 26) % 26) + ord("A")
                    )
                    decrypted_text.append(decoded_char)
                    # increment keyword index
                    keyword_index += 1
                else:
                    # keep non-alphabetic characters
                    decrypted_text.append(char)

            # form decrypted message
            decrypted_message = "".join(decrypted_text)

            # get first 5-letter word
            decrypted_words = decrypted_message.split()
            first_five_letter_word = next(
                (word for word in decrypted_words if len(word) == 5), None
            )

            # check if word is valid
            if first_five_letter_word and first_five_letter_word.lower() in keywords:
                clear()
                correct = input(
                    f"Does the following look like a valid decryption? (Y/N):\n {decrypted_message}\n> "
                )
                if correct == "Y":
                    clear()
                    print(
                        f"Valid decryption found using keyword '{keyword}': {decrypted_message}"
                    )
                    return decrypted_message

        print("No valid decryption found.")

    def race(self):
        """
        simulates a race between two runners (tortoise and hare) and prints the race progress.

        Returns
        -------
        None
            the race progress and winner are printed to the console.
        """

        # create runners
        racers = [
            Runner("tortoise", "green", 2, "🐢"),  # speed 2
            Runner("hare", "grey", 8, "🐇"),  # speed 8
        ]

        # track finish status
        finished = [False]

        # racetrack visuals
        track_top = "┌" + "─" * 48 + "┐"
        track_bot = "└" + "─" * 48 + "┘"

        clear()  # clear console

        # countdown before race
        for i in range(3):
            print(str(3 - i) + "... ")
            time.sleep(1)

        print("GO!")  # start race

        # race loop
        while not any(finished):
            time.sleep(1)
            clear()
            print(track_top)

            # update racer positions
            for racer in racers:
                if len(racer.visual) < 50:
                    # move racer forward
                    spaces = " " * random.randint(1, racer.speed)
                    racer.visual = spaces + racer.visual
                print(racer.visual)

            print(track_bot)

            # check for finish
            finished = [len(racer.visual) >= 50 for racer in racers]

        # announce winner
        winner = racers[0].name if finished[0] else racers[1].name
        print(winner + " has won the race!")


class Animal:
    """
    represents a basic animal with a name, color, and visual representation.

    Attributes
    ----------
    name : str
        name of the animal
    color : str
        color of the animal
    visual : str
        visual representation (single line of ASCII)
        default: "----{ ,_ ,'>"
    """

    def __init__(self, name, color, visual="----{ ,_ ,'>"):
        """
        initializes an Animal with name, color, and optional visual.

        Parameters
        ----------
        name : str
            name of the animal
        color : str
            color of the animal
        visual : str, optional
            visual representation (single line of ASCII), default is "----{ ,_ ,'>"
        """
        self.name = name  # set name
        self.color = color  # set color
        self.visual = visual  # set visual

    def speak(self):
        """
        returns a generic greeting.

        Returns
        -------
        str
            a generic "hello" string
        """
        return "hello"  # return greeting


class Runner(Animal):
    """
    represents a runner animal with a speed attribute.

    Attributes
    ----------
    name : str
        name of the runner
    color : str
        color of the runner
    speed : int
        speed of the runner (spaces moved per turn)
    visual : str
        visual representation (single line of ASCII)
    """

    def __init__(self, name, color, speed, visual):
        """
        initializes a Runner with name, color, speed, and visual.

        Parameters
        ----------
        name : str
            name of the runner
        color : str
            color of the runner
        speed : int
            speed of the runner (spaces moved per turn)
        visual : str
            visual representation (single line of ASCII)
        """
        super().__init__(name, color, visual)  # initialize parent class
        self.speed = speed  # set speed


def clear():
    """
    clears the console screen using ANSI escape codes.

    Returns
    -------
    None
    """

    # clear screen using ANSI escape codes
    print("\033c\033[3J", end="")


if __name__ == "__main__":
    test = Lab2()
    test.decrypt()
