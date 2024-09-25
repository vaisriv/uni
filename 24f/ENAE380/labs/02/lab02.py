# Vai Srivastava - 0106
"""
This is your template for lab2. Implement all questions in the appropriate
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""

import random, time


class Lab2(object):
    def bubble_sort(self, my_list):
        """
        Implements the Bubble Sort algorithm to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of elements to sort

        Returns
        -------
        list
            sorted list in ascending order
        """
        n = len(my_list)
        # Traverse through all elements in the list
        for i in range(n):
            # Flag to check if a swap occurred in the inner loop
            swapped = False
            # Last i elements are already sorted, so we can skip them
            for j in range(0, n - i - 1):
                # Swap if the element is greater than the next element
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    swapped = True
            # If no two elements were swapped in the inner loop, then the list is sorted
            if not swapped:
                break
        return my_list

    def selection_sort(self, my_list):
        """
        Implements the Selection Sort algorithm to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of elements to sort

        Returns
        -------
        list
            sorted list in ascending order
        """
        n = len(my_list)
        # Traverse through all list elements
        for i in range(n):
            # Assume the current element is the minimum
            min_index = i
            # Find the minimum element in the remaining unsorted array
            for j in range(i + 1, n):
                if my_list[j] < my_list[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element of the unsorted part
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
        return my_list

    def insertion_sort(self, my_list):
        """
        Implements the Insertion Sort algorithm to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of elements to sort

        Returns
        -------
        list
            sorted list in ascending order
        """
        # Traverse through 1 to len(my_list)
        for i in range(1, len(my_list)):
            key = my_list[i]
            # Move elements of my_list[0...i-1], that are greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < my_list[j]:
                my_list[j + 1] = my_list[j]
                j -= 1
            my_list[j + 1] = key
        return my_list

    def merge_sort(self, my_list):
        """
        Implements the Merge Sort algorithm to sort a list in ascending order.

        Parameters
        ----------
        my_list : list of int
            list of elements to sort

        Returns
        -------
        list
            sorted list in ascending order
        """
        if len(my_list) > 1:
            # Finding the mid of the array
            mid = len(my_list) // 2
            # Dividing the elements into 2 halves
            left_half = my_list[:mid]
            right_half = my_list[mid:]

            # Recursive call on each half
            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            # Copy data to the temporary arrays left_half and right_half
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    my_list[k] = left_half[i]
                    i += 1
                else:
                    my_list[k] = right_half[j]
                    j += 1
                k += 1

            # Checking if any element was left in left_half
            while i < len(left_half):
                my_list[k] = left_half[i]
                i += 1
                k += 1

            # Checking if any element was left in right_half
            while j < len(right_half):
                my_list[k] = right_half[j]
                j += 1
                k += 1

        return my_list

    def sorting_test(self):
        """
        Runs sorting tests for different sorting algorithms on arrays of varying sizes.

        The function tests several sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort,
        Merge Sort) using arrays of various sizes, measuring and recording their execution times.
        Results are written to a CSV file for further analysis.

        Returns
        -------
        None
            The results are printed to the console and saved in "SortingTests.csv".
        """

        # List of array sizes to test the sorting algorithms on
        arr_sizes = [8, 200, 500, 1000, 10000]

        # Dictionary containing the sorting functions, their names, and a list to store execution times
        sorts = {
            "funcs": [  # Sorting functions to be tested
                self.bubble_sort,
                self.selection_sort,
                self.insertion_sort,
                self.merge_sort,
            ],
            "names": [  # Names of the sorting functions for labeling
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
            ],  # List to store the execution times of each function
        }

        # Open the CSV file for writing the results
        with open("SortingTests.csv", "w") as file:
            # Write the names of the sorting algorithms as the first row in the CSV file
            names = str(", ").join(sorts["names"])
            print(names)  # Print the sorting names to the console
            file.write(names + str("\n"))  # Write the sorting names to the CSV file

            # Run 100 tests for each array size
            for test_num in range(100):
                print(
                    "Test Number: " + str(test_num + 1)
                )  # Print the current test number

                # Test each sorting function on arrays of different sizes
                for size in arr_sizes:
                    # Create an array of the given size filled with random integers
                    arr = [random.randint(0, size) for _ in range(size)]

                    # Time each sorting function using a copy of the random array
                    for i in range(len(sorts["funcs"])):
                        start = time.time()  # Start the timer
                        sorted = sorts["funcs"][i](
                            arr.copy()
                        )  # Sort a copy of the array
                        end = time.time()  # End the timer
                        sorts["times"][i] = float(
                            end - start
                        )  # Record the elapsed time

                    # Convert the recorded times to a comma-separated string and write to the file
                    tests = str(", ").join(map(str, sorts["times"]))
                    print(tests)  # Print the execution times to the console
                    file.write(
                        tests + str("\n")
                    )  # Write the execution times to the CSV file

    def readFile(self, filename):
        """
        Reads a file containing numbers, sorts them using merge sort, and writes the sorted
        numbers to a new file called "SortedNumbers.txt". The first line of the output file
        will contain the label "Sorted Numbers", followed by each number on a new line.

        Parameters
        ----------
        filename : str
            The name of the file to read from (should contain one number per line).
        """
        # Open the input file in read mode
        with open(filename) as file_in:
            # Read the lines from the file starting from the second line (skipping header if present)
            # Convert each line (which is a string) into an integer, using list comprehension
            nums = [
                int(x) for x in file_in.readlines()[1::]
            ]  # [1::] skips the first line

        # Sort the list of numbers using the merge_sort function
        sorted = self.merge_sort(nums)

        # Open the output file in write mode (it will create a new file or overwrite the existing one)
        with open("SortedNumbers.txt", "w") as file_out:
            # Write the label "Sorted Numbers" on the first line of the output file
            file_out.write("Sorted Numbers\n")

            # Convert each sorted number into a string and add a newline character to each number
            # Create a list where each number is followed by a newline character
            sorted_out = [num + str("\n") for num in list(map(str, sorted))]

            # Write the list of sorted numbers to the output file
            file_out.writelines(sorted_out)

    def vigenere(self):
        """
        Encodes a plaintext message using the Vigenère cipher with a keyword.

        The function prompts the user for a plaintext message and a keyword. It encodes
        the message by shifting each alphabetic character based on the corresponding
        character in the keyword. Non-alphabetic characters are not modified, and the
        keyword advances only for alphabetic characters.

        Returns
        -------
        None
            The encoded message is printed to the console.
        """
        plaintext = input("Provide plaintext message:\n")
        keyword = input("Provide keyword:\n")

        # List to store the encoded characters
        ciphertext = []

        # Track the position in the keyword
        keyword_index = 0

        # Iterate over each character in the plaintext
        for p in plaintext:
            if p.isalpha():
                # Use the current character of the keyword (loop back if necessary)
                k = keyword[keyword_index % len(keyword)]
                # Encode the alphabetic character
                encoded_char = (
                    lambda p, k: chr(
                        ((ord(p) - ord("A") + ord(k) - ord("A")) % 26) + ord("A")
                    )
                )(p.upper(), k.upper())
                ciphertext.append(encoded_char)
                # Only increment keyword_index when an alphabetic character is encoded
                keyword_index += 1
            else:
                # Non-alphabetic characters are added to ciphertext unchanged
                ciphertext.append(p)

        # Join the list of encoded characters into a string
        print("".join(ciphertext).lower())

    def decrypt(self):
        """
        Attempts to decrypt a Vigenère cipher using a dictionary of valid words.
        
        The function reads a cipher text from 'cipher.txt' and tries to decrypt it by
        attempting each 5-letter word from 'validwords.txt' as the potential keyword.
        After decoding with each keyword, the function checks if the first 5-letter word
        in the decrypted message is a valid word from the dictionary. If a valid decryption
        is found, the function prints and returns the decrypted message.

        Returns
        -------
        str
            The successfully decrypted message, or None if no valid decryption was found.
        """

        def load_file(filename):
            """
            Helper function to load the contents of a file.

            Parameters
            ----------
            filename : str
                Name of the file to be loaded.

            Returns
            -------
            str or list of str
                Contents of the file, either as a string (for cipher) or list of words (for dictionary).
            """
            with open(filename, "r") as file:
                return file.read().splitlines()

        # Load the cipher text and valid words dictionary
        cipher_text = load_file("cipher.txt")[0]  # Cipher is a single line
        valid_words = set(load_file("validwords.txt"))  # Store valid words as a set for fast lookup

        # Try each 5-letter word from the dictionary as a possible keyword
        for keyword in valid_words:
            decrypted_text = []
            keyword_index = 0

            # Decrypt the cipher text using the current keyword
            for char in cipher_text:
                if char.isalpha():
                    # Use the current character of the keyword (loop back if necessary)
                    key_char = keyword[keyword_index % len(keyword)].upper()
                    # Decrypt the alphabetic character by reversing the cipher shift
                    decoded_char = (lambda c, k: chr(((ord(c) - ord(k)) % 26) + ord('A')))(char.upper(), key_char)
                    decrypted_text.append(decoded_char)
                    # Increment keyword index only for alphabetic characters
                    keyword_index += 1
                else:
                    # Non-alphabetic characters are added to decrypted text unchanged
                    decrypted_text.append(char)

            # Join the decrypted characters into a full string
            decrypted_message = ''.join(decrypted_text)

            # Extract the first 5-letter word from the decrypted message
            decrypted_words = decrypted_message.split()
            first_five_letter_word = next((word for word in decrypted_words if len(word) == 5), None)

            # Check if the first 5-letter word is valid
            if first_five_letter_word and first_five_letter_word.lower() in valid_words:
                print(f"Valid decryption found using keyword '{keyword}': {decrypted_message}")
                return decrypted_message

        print("No valid decryption found.")

    def race(self):
        """
        Simulates a race between two runners (tortoise and hare) and prints the race progress on the console.

        The race proceeds in real-time, with each runner's position updated based on their speed attribute.
        The track is displayed using special characters, and the race ends when either racer reaches the finish line.
        The winner is announced at the end.

        Returns
        -------
        None
            The function prints the race progress and the winner to the console.
        """

        # Create two runners, a tortoise and a hare, with different speeds and visuals
        racers = [
            Runner("tortoise", "green", 2, "🐢"),  # Tortoise moves slowly (speed 2)
            Runner("hare", "grey", 8, "🐇"),  # Hare moves faster (speed 8)
        ]

        # Track which racers have finished the race
        finished = [False]

        # Visual representation of the top and bottom of the racetrack
        track_top = "┌" + "─" * 48 + "┐"
        track_bot = "└" + "─" * 48 + "┘"

        clear()  # Clear the console to start the race countdown

        # Countdown before the race begins
        for i in range(3):
            print(str(3 - i) + "... ")  # Print countdown numbers (3... 2... 1...)
            time.sleep(1)  # Wait for 1 second between each countdown

        print("GO!")  # Start the race

        # Main loop for the race, runs until one racer reaches the finish line
        while not any(finished):
            time.sleep(1)  # Pause for a second between each step of the race
            clear()  # Clear the console for updated race progress
            print(track_top)  # Print the top border of the racetrack

            # Update the position of each racer and print their visuals on the track
            for racer in racers:
                if (
                    len(racer.visual) < 50
                ):  # Racer hasn't reached the finish line (track length is 50)
                    # Move the racer forward by adding spaces based on their speed
                    spaces = " " * random.randint(1, racer.speed)
                    racer.visual = spaces + racer.visual  # Update racer's position
                print(racer.visual)  # Print the racer's position on the track

            print(track_bot)  # Print the bottom border of the racetrack

            # Check if any racer has finished (i.e., their visual exceeds the track length)
            finished = [False if len(racer.visual) < 50 else True for racer in racers]

        # Determine the winner based on which racer finished first
        winner = racers[0].name if finished[0] else racers[1].name
        print(winner + " has won the race!")  # Announce the winner


class Animal:
    """
    Represents a basic animal with a name, color, and visual representation.

    Attributes
    ----------
    name : str
        The name of the animal.
    color : str
        The color of the animal.
    visual : str
        A visual representation of the animal
        Note: Must be a single line of ascii
        Default: "----{ ,_ ,'>" (A picture of a mouse)
    """

    def __init__(self, name, color, visual="----{ ,_ ,'>"):
        """
        Initializes an Animal instance with a name, color, and optional visual.

        Parameters
        ----------
        name : str
            The name of the animal.
        color : str
            The color of the animal.
        visual : str
            A visual representation of the animal
            Note: Must be a single line of ASCII
            Default: "----{ ,_ ,'>" (A picture of a mouse)
        """
        self.name = name  # Animal's name
        self.color = color  # Animal's color
        self.visual = visual  # Visual representation of the animal

    def speak(self):
        """
        Returns a generic greeting sound for the animal.

        Returns
        -------
        str
            A generic "hello" string.
        """
        return "hello"  # Generic greeting sound


class Runner(Animal):
    """
    Represents a runner that inherits from the Animal class and includes a speed attribute.

    Attributes
    ----------
    name : str
        The name of the runner.
    color : str
        The color of the runner.
    speed : int
        The speed of the runner, which determines how many spaces they move each turn.
    visual : str
        A visual representation of the runner.
        Note: Must be a single line of ASCII
    """

    def __init__(self, name, color, speed, visual):
        """
        Initializes a Runner instance with a name, color, speed, and visual.

        Parameters
        ----------
        name : str
            The name of the runner.
        color : str
            The color of the runner.
        speed : int
            The speed of the runner, which determines how far they move each turn.
        visual : str
            A visual representation of the runner (e.g., "🐢" for tortoise).
            Note: Must be a single line of ASCII
        """
        super().__init__(
            name, color, visual
        )  # Call the parent class (Animal) constructor
        self.speed = speed  # Set the runner's speed


def clear():
    """
    Clears the console screen by printing ANSI escape codes.

    This function uses ANSI escape codes to clear the screen and reset the cursor position.
    It works on most Unix-like systems and is used here to refresh the screen during the race simulation.

    Returns
    -------
    None
    """

    # Print ANSI escape codes to clear the terminal screen and reset the cursor position
    # "\033c" resets the terminal, and "\033[3J" clears the scrollback buffer.
    # 'end=""' ensures there is no automatic newline after clearing.
    print("\033c\033[3J", end="")


if __name__ == "__main__":
    test = Lab2()
    test.decrypt()
