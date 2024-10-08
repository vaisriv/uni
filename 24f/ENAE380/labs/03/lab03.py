# Vai Srivastava - 0106
"""
This is your template for lab3. Implement all questions in the appropriate
function. Implement helper functions as needed with
a short (one-line) description of their purpose.
"""


def two_bit(A: list, B: list) -> list:
    """
    Multiplies two 2-bit binary numbers represented as lists of bits (LSB to MSB).

    Parameters
    ----------
    A: list of int
        Bits of the first number, [LSB, MSB]
    B: list of int
      Bits of the second number, [LSB, MSB]

    Returns
    -------
    list of int
      4-bit product of A and B (LSB to MSB)
    """
    # Partial products
    U = [
        AND(A[0], B[0]),  # U[0] = A0 * B0
        AND(A[0], B[1]),  # U[1] = A0 * B1
        AND(A[1], B[0]),  # U[2] = A1 * B0
        AND(A[1], B[1]),  # U[3] = A1 * B1
    ]

    # Sum and carry bits
    V = [
        U[0],  # V[0] = U[0]
        XOR(U[1], U[2]),  # V[1] = U[1] ⊕ U[2]
        AND(U[1], U[2]),  # V[2] = U[1] ∧ U[2]
        U[3],  # V[3] = U[3]
    ]

    C = [
        V[0],  # C[0] = V[0]
        V[1],  # C[1] = V[1]
        XOR(V[2], V[3]),  # C[2] = V[2] ⊕ V[3]
        AND(V[2], V[3]),  # C[3] = V[2] ∧ V[3]
    ]

    return C


def conversion():
    """
    Converts between integer and 4-bit binary representations using sign magnitude,
    one's complement, and two's complement methods.

    Prompts the user to input either an integer or a 4-bit binary number,
    and outputs the corresponding representations.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # Prompt the user to choose between integer or binary input
    validinput = False
    intorbin = ""
    while not validinput:
        intorbin = input(
            "Do you want to input an integer or a binary number? (int/bin)\n> "
        )
        validinput = "int" in intorbin or "bin" in intorbin
        if not validinput:
            print("Invalid input, please try again!")

    signmag = 0
    onescomp = 0
    twoscomp = 0
    if "bin" in intorbin:
        # Handle binary input
        bits = list()
        validinput = False
        while not validinput:
            bits = str(input("Input a four bit number:\n> "))
            validinput = len(bits) == 4 and all(x in "01" for x in bits)
            if not validinput:
                print("Invalid input, please input 4 bits (each being either 0 or 1).")

        # Determine the sign based on the first bit (sign bit)
        sign = -1 if int(bits[0]) else 1

        # Compute the sign-magnitude value
        signmag = sign * (int(bits[1]) * 4 + int(bits[2]) * 2 + int(bits[3]))

        # Compute the one's complement value
        if sign == 1:
            onescomp = signmag
        else:
            onescomp = sign * (
                (not int(bits[1])) * 4 + (not int(bits[2])) * 2 + (not int(bits[3]))
            )

        # Compute the two's complement value
        twoscomp = onescomp - 1

    elif "int" in intorbin:
        # Handle integer input
        num = 0
        validinput = False
        while not validinput:
            num = int(input("Input an integer:\n> "))
            validinput = num <= 7 and num >= -8
            if not validinput:
                print(
                    "Input out of range of all, please try again (with a number between -8 and +7)."
                )

        # Determine the magnitude and sign of the number
        is_negative = num < 0
        magnitude = abs(num)
        n = magnitude

        # Convert the magnitude to a 3-bit binary string
        magnitude_bits = str((n >> 2) & 1) + str((n >> 1) & 1) + str(n & 1)

        # Set the sign bit ('1' for negative, '0' for positive)
        sign_bit = "1" if is_negative else "0"

        # Compute the sign-magnitude and one's complement representations
        if abs(num) <= 7:
            signmag = sign_bit + magnitude_bits
            if is_negative:
                inverted_magnitude_bits = "".join(
                    "1" if b == "0" else "0" for b in magnitude_bits
                )
                onescomp = "1" + inverted_magnitude_bits
            else:
                onescomp = "0" + magnitude_bits
        else:
            signmag = "Out of range"
            onescomp = "Out of range"

        # Compute the two's complement representation
        if is_negative:
            twoscomp_value = (1 << 4) - magnitude
            twoscomp_bits = ['0'] * 4
            for i in range(3, -1, -1):
                twoscomp_bits[i] = str(twoscomp_value % 2)
                twoscomp_value = twoscomp_value // 2
            twoscomp = ''.join(str(i) for i in twoscomp_bits)
        else:
            twoscomp = "0" + magnitude_bits

    # Output the results
    print(
        f"Sign Magnitude: '{signmag}'\nOne's Complement: '{onescomp}'\nTwo's Complement: '{twoscomp}'"
    )


def dec2float():
    """
    Converts a decimal number to its 8-bit floating point binary representation.

    The floating point format:
    - Sign bit: 1 bit
    - Exponent: 3 bits (biased by +3)
    - Mantissa: 4 bits

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    validinput = False
    dec = 0
    while not validinput:
        dec = float(input(
            "Input a decimal number within the range of an 8-bit float\n> "
        ))
        validinput = abs(dec) <= 31.0 and abs(dec) >= 0.125
        if not validinput:
            print("Input out of representable range (|number| must be between 0.125 and 31.0) or was not a number. Please try again!")

    # Determine the sign bit
    sign_bit = '0' if dec >= 0 else '1'

    # Work with the absolute value
    N = abs(dec)

    # Initialize exponent e
    e = 0

    # Normalize N to be in [1.0, 2.0)
    # If N >= 2.0, divide N by 2, increment e
    # If N < 1.0, multiply N by 2, decrement e

    if N == 0:
        # Handle zero input separately (should not happen due to validation)
        exponent_bits_str = '000'
        mantissa = '0000'
    else:
        # Normalize N
        while N >= 2.0:
            N /= 2.0
            e += 1
        while N < 1.0:
            N *= 2.0
            e -= 1

        # Now N is in [1.0, 2.0)

        # Compute the biased exponent
        exponent_bias = 3
        exponent_bits = e + exponent_bias

        # Check for overflow and underflow
        if exponent_bits < 0:
            print("Underflow error: number too small to represent.")
            return
        elif exponent_bits > 7:
            print("Overflow error: number too large to represent.")
            return

        # Convert exponent_bits to a 3-bit binary string manually
        exponent_bits_str = ''
        for i in range(2, -1, -1):
            bit = (exponent_bits >> i) & 1
            exponent_bits_str += str(bit)

        # Compute the mantissa bits (4 bits)
        fraction = N - 1.0  # Since N = 1.f
        mantissa = ''
        for _ in range(4):
            fraction *= 2
            if fraction >= 1.0:
                mantissa += '1'
                fraction -= 1.0
            else:
                mantissa += '0'

    # Assemble the final binary string
    output = sign_bit + exponent_bits_str + mantissa

    print(f"Floating point representation: {output}")


def float2dec():
    """
    Converts an 8-bit floating point binary representation to its decimal equivalent.

    The floating point format:
    - Sign bit: 1 bit
    - Exponent: 3 bits (biased by +3)
    - Mantissa: 4 bits

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    binary_input = []
    validinput = False
    while not validinput:
        binary_input = input("Input an 8-bit binary floating point number:\n> ").strip()
        validinput = len(binary_input) == 8 and all(x in '01' for x in binary_input)
        if not validinput:
            print("Invalid input. Please enter 8 bits consisting of 0s and 1s.")

    # Extract the sign bit
    sign_bit = binary_input[0]
    sign = -1 if sign_bit == '1' else 1

    # Extract the exponent bits and compute exponent value
    exponent_bits = binary_input[1:4]
    exponent = 0
    for bit in exponent_bits:
        exponent = exponent * 2 + int(bit)
    exponent_bias = 3
    e = exponent - exponent_bias  # Adjust for bias

    # Extract the mantissa bits and compute mantissa value
    mantissa_bits = binary_input[4:]
    mantissa = 0.0
    fraction = 0.5
    for bit in mantissa_bits:
        if bit == '1':
            mantissa += fraction
        fraction /= 2.0

    # Reconstruct the decimal number
    N = sign * (1.0 + mantissa) * (2 ** e)

    print(f"Decimal value: {N}")


def AND(a: int, b: int) -> int:
    """
    Performs logical AND operation on two bits.

    Parameters
    ----------
    a : int
        First bit (0 or 1).
    b : int
        Second bit (0 or 1).

    Returns
    -------
    int
        Result of a AND b (0 or 1).
    """
    return int(a and b)


def OR(a: int, b: int) -> int:
    """
    Performs logical OR operation on two bits.

    Parameters
    ----------
    a : int
        First bit (0 or 1).
    b : int
        Second bit (0 or 1).

    Returns
    -------
    int
        Result of a OR b (0 or 1).
    """
    return int(a or b)


def NOT(a: int) -> int:
    """
    Performs logical NOT operation on a bit.

    Parameters
    ----------
    a : int
        The bit to invert (0 or 1).

    Returns
    -------
    int
        Inverted bit (1 if a is 0, 0 if a is 1).
    """
    return int(not a)


def NAND(a: int, b: int) -> int:
    """
    Performs logical NAND operation on two bits.

    NAND is the negation of the AND operation.

    Parameters
    ----------
    a : int
        First bit (0 or 1).
    b : int
        Second bit (0 or 1).

    Returns
    -------
    int
        Result of NOT(a AND b) (0 or 1).
    """
    return NOT(AND(a, b))


def NOR(a: int, b: int) -> int:
    """
    Performs logical NOR operation on two bits.

    NOR is the negation of the OR operation.

    Parameters
    ----------
    a : int
        First bit (0 or 1).
    b : int
        Second bit (0 or 1).

    Returns
    -------
    int
        Result of NOT(a OR b) (0 or 1).
    """
    return NOT(OR(a, b))


def XOR(a: int, b: int) -> int:
    """
    Performs logical XOR (exclusive OR) operation on two bits.

    The result is 1 if the bits are different, and 0 if they are the same.

    Parameters
    ----------
    a : int
        First bit (0 or 1).
    b : int
        Second bit (0 or 1).

    Returns
    -------
    int
        Result of a XOR b (0 or 1).
    """
    return OR(AND(a, NOT(b)), AND(NOT(a), b))


def XNOR(a: int, b: int) -> int:
    """
    Performs logical XNOR (exclusive NOR) operation on two bits.

    The result is 1 if the bits are the same, and 0 if they are different.

    XNOR is the negation of the XOR operation.

    Parameters
    ----------
    a : int
        First bit (0 or 1).
    b : int
        Second bit (0 or 1).

    Returns
    -------
    int
        Result of NOT(a XOR b) (0 or 1).
    """
    return NOT(XOR(a, b))


# if __name__ == "__main__":
#     conversion()
#     dec2float()
#     float2dec()
