import unittest
import lab03


def bits_to_int(bits):
    """Converts a list of bits (LSB to MSB) to an integer."""
    return sum(bit << idx for idx, bit in enumerate(bits))


def int_to_bits(n, length):
    """Converts an integer to a list of bits (LSB to MSB) of given length."""
    return [(n >> i) & 1 for i in range(length)]


class TestTwoBitMultiplier(unittest.TestCase):
    def test_all_combinations(self):
        """Tests all possible combinations of two 2-bit binary numbers."""
        possible_bits = [[0, 0], [1, 0], [0, 1], [1, 1]]
        for a_bits in possible_bits:
            for b_bits in possible_bits:
                with self.subTest(a_bits=a_bits, b_bits=b_bits):
                    expected = self.compute_expected(a_bits, b_bits)
                    result = lab03.two_bit(a_bits, b_bits)
                    self.assertEqual(
                        result, expected, f"Failed for inputs {a_bits} and {b_bits}"
                    )

    @staticmethod
    def compute_expected(a_bits, b_bits):
        """Computes the expected product as a list of 4 bits (LSB to MSB)."""
        a = bits_to_int(a_bits)
        b = bits_to_int(b_bits)
        product = a * b
        return int_to_bits(product, 4)


# Run the tests
if __name__ == "__main__":
    unittest.main()
