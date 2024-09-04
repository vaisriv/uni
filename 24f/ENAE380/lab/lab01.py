"""
This is your template for lab1. Implement all questions in the appropriate 
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""

import textstat


class Lab1(object):
    def average(self):
        """
        Finds the average of two numbers.


        Inputs
        ------
        num1 : int
                First input from user

        num2 : int
                Second input from user


        Outputs
        -------
        avg: float
                The average of the two numbers input by user
        """

        num1 = int(input("Input num1: "))
        num2 = int(input("Input num2: "))

        avg = float((num1 + num2) / 2)

        print(avg)

    def money(self):
        """
        Converts cents into quantities of 1, 4, and 15 cent coins.

        Inputs
        ------
        cents : int
                The number of cents to convert

        Outputs
        -------
        fifteens : int
                The number of 15-cent coins

        fours : int
                The number of 4-cent coins

        ones : int
                The number of 1-cent coins
        """

        cents = int(input("How many cents to convert? "))

        fifteens = int(cents / 15)
        fours = int((cents % 15) / 4)
        ones = int((cents % 15) % 4)

        print(
            "Fifteens: "
            + str(fifteens)
            + ", Fours: "
            + str(fours)
            + ", Ones: "
            + str(ones)
        )

    def lyrics(self):
        """
        Displays the lyrics of a selected artist's song and calculates its readability.

        Inputs
        ------
        artist : str
                The name of the artist

        Outputs
        -------
        title : str
                The song title of the selected artist

        lyrics : str
                The song lyrics of the selected artist

        ease : float
                The Flesch Reading Ease score of the lyrics

        grade : float
                The Flesch-Kincaid Grade Level of the lyrics
        """

        titles = dict(
            [
                ("Lake Street Dive", "Twenty-Five"),
                ("Bob Dylan", "Mr. Tambourine Man"),
                ("Taylor Swift", "Invisible String"),
                ("George Gershwin", "Someone to Watch Over Me"),
            ]
        )

        songs = dict(
            [
                (
                    "Lake Street Dive",
                    """
                    [Verse 1]
                    There was a time when I imagined us forever
                    I can't quite remember how I thought we'd work it out
                    I guess I would move to California or you to Boston
                    And I'd learn to like to stay at home or you'd learn to like going out

                    [Chorus]
                    And although the stories that I tell myself about us now
                    Don't take me to the grave
                    I'll be an old woman with somebody else by my side
                    But I will always be in love with you in my memories
                    When we were twenty-five

                    [Verse 2]
                    I always think of you whеn I drink affogatos
                    'Cause that summer, we would havе them every afternoon
                    The hot and cold was such a perfect combination
                    Melt all together, bittersweet and creamy, and always gone to soon

                    [Chorus]
                    But all the joy we had and love we gave away back then
                    Well, it never went to waste
                    'Cause I'll be an old woman with somebody else by my side
                    But I will always be in love with how you loved me
                    When we were twenty-five
                    [Outro]
                    Mmm
                    Mmm
                    """,
                ),
                (
                    "Bob Dylan",
                    """
                    [Chorus]
                    Hey, Mr. Tambourine Man, play a song for me
                    I'm not sleepy, and there is no place I'm going to
                    Hey, Mr. Tambourine Man, play a song for me
                    In the jingle jangle mornin' I'll come followin' you

                    [Verse 1]
                    Though I know that evening's empire has returned into sand
                    Vanished from my hand
                    Left me blindly here to stand, but still not sleeping
                    My weariness amazes me, I am branded on my feet
                    I have no one to meet
                    And my ancient empty street's too dead for dreaming

                    [Chorus]
                    Hey, Mr. Tambourine Man, play a song for me
                    I'm not sleepy, and there is no place I'm going to
                    Hey, Mr. Tambourine Man, play a song for me
                    In the jingle jangle mornin' I'll come followin' you

                    [Verse 2]
                    Take me on a trip upon your magic swirlin' ship
                    My senses have been stripped, my hands can't feel to grip
                    My toes too numb to step, wait only for my boot heels
                    To be wandering
                    I'm ready to go anywhere, I'm ready for to fade
                    Into my own parade, cast your dancin' spell my way
                    I promise to go under it
                    [Chorus]
                    Hey, Mr. Tambourine Man, play a song for me
                    I'm not sleepy, and there is no place I'm going to
                    Hey, Mr. Tambourine Man, play a song for me
                    In the jingle jangle mornin' I'll come followin' you

                    [Verse 3]
                    Though you might hear laughing, spinning, swinging madly across the sun
                    It's not aimed at anyone, it's just escaping on the run
                    And but for the sky there are no fences facing
                    And if you hear vague traces of skipping reels of rhyme
                    To your tambourine in time, it's just a ragged clown behind
                    I wouldn't pay it any mind
                    It's just a shadow you're seeing that he's chasing

                    [Chorus]
                    Hey, Mr. Tambourine Man, play a song for me
                    I'm not sleepy, and there is no place I'm going to
                    Hey, Mr. Tambourine Man, play a song for me
                    In the jingle jangle mornin' I'll come followin' you

                    [Instrumental Bridge]

                    [Verse 4]
                    And take me disappearing through the smoke rings of my mind
                    Down the foggy ruins of time, far past the frozen leaves
                    The haunted, frightened trees, out to the windy beach
                    Far from the twisted reach of crazy sorrow
                    Yes, to dance beneath the diamond sky with one hand waving free
                    Silhouetted by the sea, circled by the circus sands
                    With all memory and fate driven deep beneath the waves
                    Let me forget about today until tomorrow
                    [Chorus]
                    Hey, Mr. Tambourine Man, play a song for me
                    I'm not sleepy, and there is no place I'm going to
                    Hey, Mr. Tambourine Man, play a song for me
                    In the jingle jangle mornin' I'll come followin' you
                    """,
                ),
                (
                    "Taylor Swift",
                    """
                    [Verse 1]
                    Green was the color of the grass
                    Where I used to read at Centennial Park
                    I used to think I would meet somebody there
                    Teal was the color of your shirt
                    When you were sixteen at the yogurt shop
                    You used to work at to make a little money

                    [Chorus]
                    Time, curious time
                    Gave me no compasses, gave me no signs
                    Were there clues I didn't see?
                    And isn't it just so pretty to think
                    All along there was some
                    Invisible string
                    Tying you to me?
                    Ooh-ooh-ooh-ooh

                    [Verse 2]
                    Bad was the blood of the song in the cab
                    On your first trip to LA
                    You ate at my favorite spot for dinner
                    Bold was the waitress on our three-year trip
                    Getting lunch down by the Lakes
                    She said I looked like an American singer
                    [Chorus]
                    Time, mystical time
                    Cutting me open, then healing me fine
                    Were there clues I didn't see?
                    And isn't it just so pretty to think
                    All along there was some
                    Invisible string
                    Tying you to me?
                    Ooh-ooh-ooh-ooh

                    [Bridge]
                    A string that pulled me
                    Out of all the wrong arms, right into that dive bar
                    Something wrapped all of my past mistakes in barbed wire
                    Chains around my demons
                    Wool to brave the seasons
                    One single thread of gold
                    Tied me to you

                    [Verse 3]
                    Cold was the steel of my axe to grind
                    For the boys who broke my heart
                    Now I send their babies presents
                    Gold was the color of the leaves
                    When I showed you around Centennial Park
                    Hell was the journey, but it brought me heaven
                    [Chorus]
                    Time, wondrous time
                    Gave me the blues and then purple-pink skies
                    And it's cool, baby, with me
                    And isn't it just so pretty to think
                    All along there was some
                    Invisible string
                    Tying you to me?
                    Ooh-ooh-ooh-ooh
                    Me
                    Ooh-ooh-ooh-ooh

                    [Outro]
                    (Ah-ah-ah)
                    (Ah-ah-ah)
                    """,
                ),
                (
                    "George Gershwin",
                    """
                    [Verse]
                    There's a saying old says that love is blind
                    Still we're often told "seek and ye shall find"
                    So I'm going to seek a certain girl I've had in mind
                    Looking everywhere, haven't found her yet
                    She's the big affair I cannot forget
                    Only girl I ever think of with regret
                    I'd like to add her initials to my monogram
                    Tell me where's the shepherd for this lost lamb

                    [Chorus]
                    There's a somebody I'm longing to see
                    I hope that she turns out to be
                    Someone to watch over me

                    I'm a little lamb who's lost in a wood
                    I know I could always be good
                    To one who'll watch over me

                    Although I may not be the man some girls think of
                    As handsome to my heart
                    She carries the key

                    Won't you tell her please to put on some speed
                    Follow my lead, oh how I need
                    Someone to watch over me
                    Someone to watch over me
                    """,
                ),
            ]
        )

        artist = input(
            "Which artist do you want? (Lake Street Dive/Bob Dylan/Taylor Swift/George Gershwin)\n> "
        )

        song = songs[artist]
        title = titles[artist]
        ease = textstat.flesch_reading_ease(song)
        grade = textstat.flesch_kincaid_grade(song)

        out = """
            Artist: {}
            Title: {}
            Reading Ease: {}
            Grade Level: {}
        """
        print(out.format(artist, title, ease, grade))

    def interest(self):
        """
        Calculates compound interest.

        Inputs
        ------
        principal : float
                The initial principal amount

        interest : float
                The annual interest rate as a decimal

        years : int
                The number of years the interest is applied

        freq : int
                The compounding frequency per year

        Outputs
        -------
        final : float
                The final amount after interest is applied

        earned : float
                The interest earned on the principal amount
        """

        principal = float(input("Enter the principal amount: "))
        interest = float(input("Enter the interest rate: "))
        years = int(input("Enter the number of years: "))
        freq = int(input("Enter the compounding frequency per year: "))

        final = float(principal * pow((1 + interest / freq), (years * freq)))
        earned = float(final - principal)

        out = """
            Principal Amount: ${:.2f}
            Annual Interest Rate: {:.2f}%
            Time (in years): {:.2f}
            Compounding Frequency: {} time(s) per year
            Final Amount: ${:.2f}
            Interest Earned: ${:.2f}
        """

        print(out.format(principal, interest * 100, years, freq, final, earned))

    def coffee(self):
        """
        Attempts to guess user's coffee preference.

        Inputs
        ------
        temp : str
                Indicates whether it is hot or cold outside

        time : str
                Indicates whether it is morning or evening

        yawn : str (optional)
                Indicates if the user is yawning a lot
                (only asked if it is morning and hot outside)

        job : str (optional)
                Asks if the user is the parent of a toddler, coming from a workout, or just tired
                (only asked if user is yawning)

        heretogo : str (optional)
                Asks if the order is for here or to go
                (only asked if the user is not yawning)

        alert : str (optional)
                Asks if the user alerted the barista before ordering
                (only asked if the order is for here)

        nyc : str (optional)
                Asks if the user is from NYC or visiting
                (only asked if it is morning and cold outside)

        board : str (optional)
                Asks if the user checked the board of rotating specialty coffees
                (only asked if user is a local/NYC resident)

        smoke : str (optional)
                Asks if the user is a smoker
                (only asked if the user has checked the specialty coffee board)

        age : str (optional)
                Asks if the user is a millennial
                (only asked if the user is not a smoker)

        study : str (optional)
                Asks if the user is carrying a laptop or a lot of books
                (only asked if it is evening)

        Outputs
        -------
        drink : str
                The guessed coffee drink based on user input
        """

        temp = input("Is it hot or cold out? ").lower()
        time = input("Is it morning or evening? ").lower()

        if "morning" in str(time):
            if "hot" in str(temp):
                yawn = input("Are you yawning a lot? ").lower()
                if "y" in str(yawn):
                    job = input(
                        "Are you the parent of a toddler, coming from a workout, or just tired? "
                    ).lower()
                    if "parent" in str(job):
                        print("Double shot iced latte with a straw")
                    elif "workout" in str(job):
                        print("Cold brew")
                    elif "tired" in str(job):
                        print("Double espresso")
                    else:
                        print("I could not understand your input. Please try again!")
                elif "n" in str(yawn):
                    heretogo = input("For here or to go? ").lower()
                    if "h" in str(heretogo):
                        alert = input(
                            "Did you alert the barista before ordering that the sugar is out? "
                        ).lower()
                        if "y" in str(alert):
                            print("Iced Mocha")
                        elif "n" in str(alert):
                            print("Cappuccino")
                        else:
                            print(
                                "I could not understand your input. Please try again!"
                            )
                    elif "go" in str(heretogo):
                        print("Large iced latte")
                    else:
                        print("I could not understand your input. Please try again!")
                else:
                    print("I could not understand your input. Please try again!")
            elif "cold" in str(temp):
                nyc = input("Are you from NYC or visiting? ").lower()
                if "visit" in str(nyc):
                    print("Coffee with cream & sugar")
                elif ("local" in str(nyc)) | ("nyc" in str(nyc)):
                    board = input(
                        "Did you check out the board of rotating specialty coffees? "
                    ).lower()
                    if "some" in str(board):
                        print("Soy latte")
                    elif ("what" in str(board)) | ("n" in str(board)):
                        print("Bodega drip coffee")
                    elif ("course" in str(board)) | ("y" in str(board)):
                        smoke = input("Are you a smoker?").lower()
                        if "y" in str(smoke):
                            print("Americano")
                        elif "n" in str(smoke):
                            age = input("Are you a **Millennial**? ").lower()
                            if "y" in str(age):
                                print("Flat White")
                            elif "n" in str(age):
                                print("Cortado")
                            else:
                                print(
                                    "I could not understand your input. Please try again!"
                                )
                        else:
                            print(
                                "I could not understand your input. Please try again!"
                            )
                    else:
                        print("I could not understand your input. Please try again!")
                else:
                    print("I could not understand your input. Please try again!")
            else:
                print("I could not understand your input. Please try again!")
        elif "evening" in str(time):
            study = input(
                "Are you carrying your laptop or a lot of books with you? "
            ).lower()
            if "y" in str(study):
                if "hot" in str(temp):
                    print("Iced vanilla red eye")
                elif "cold" in str(temp):
                    print("Large latte or cappuccino")
                else:
                    print(
                        "I could not understand your inital weather input. Please try again!"
                    )
            elif "n" in str(study):
                if "hot" in str(temp):
                    print("Iced chai latte")
                elif "cold" in str(temp):
                    print("Herbal tea or hot chocolate")
                else:
                    print(
                        "I could not understand your inital weather input. Please try again!"
                    )
            else:
                print("I could not understand your input. Please try again!")
        else:
            print("I could not understand your input. Please try again!")


test = Lab1()
# test.average()
# test.money()
# test.lyrics()
# test.interest()
test.coffee()
