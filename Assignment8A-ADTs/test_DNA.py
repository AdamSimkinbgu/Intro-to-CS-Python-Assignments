from unittest import TestCase, main
import pytest
from Errors import *
from DNA import DNA


class TestDNA(TestCase):
    def setUp(self) -> None:
        self.seq = "ATGTTTCCCTAG"
        self.obj = DNA(self.seq)

    def test_init(self):
        self.assertRaises(NotNucleotideError, DNA, "ATGTTTCCCGGGU")
        self.assertRaises(NotNucleotideError, DNA, "AAATTTCCCUTAG")

    def test_str(self):
        self.assertEqual("ATGTTTCCCTAG", str(self.obj))

    def test_len(self):
        self.assertEqual(12, len(self.obj))

    def test_complement(self):
        new_seq = str(self.obj.complement())
        self.assertEqual("CTAGGGAAACAT", new_seq)

    def test_calculate_mass(self):
        mass = self.obj.calculate_mass()
        self.assertEqual(11685.799999999997, mass)

    def test_mutate(self):

        # Test input
        self.assertRaises(InputNotValidError, self.obj.mutate, "deletion", 4, "ATUG")
        self.assertRaises(ValueError, self.obj.mutate, "deletion", 4, "ATG")
        self.assertRaises(InputNotValidError, self.obj.mutate, "addition", -1, "TGATT")
        self.assertRaises(InputNotValidError, self.obj.mutate, "replacement", 55, "AAAA")
        self.assertRaises(InputNotValidError, self.obj.mutate, "replacement", 5, "ACGACGGCATTTGGGAAATAATCGCAAAA")

        # Test addition
        self.obj.mutate("addition", 0, "ACG")
        self.assertEqual("ACGATGTTTCCCTAG", str(self.obj.nucleotides_sequence))

        # Test replacement
        self.obj.mutate("replacement", 3, "CTT")
        self.assertEqual("ACGCTTTTTCCCTAG", str(self.obj.nucleotides_sequence))

        # Test deletion
        self.obj.mutate("deletion", 4, "TTT")
        self.assertEqual("ACGCTTCCCTAG", str(self.obj.nucleotides_sequence))


if __name__ == "__main__":
    main()
