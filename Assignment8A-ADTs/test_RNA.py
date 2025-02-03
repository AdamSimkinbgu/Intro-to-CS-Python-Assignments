from unittest import *
from Errors import *
from RNA import RNA


class TestRNA(TestCase):
    def setUp(self) -> None:
        self.seq = "AUGUUUCCCUAG"
        self.obj = RNA(self.seq)

    def test_init(self):
        self.assertRaises(NotNucleotideError, RNA, "AAAUCCCGUAG")
        self.assertRaises(NotNucleotideError, RNA, "AUGUCCCGGGU")
        self.assertRaises(NotNucleotideError, RNA, "AUGUCCGGGU")
        self.assertRaises(NotNucleotideError, RNA, "AUGTCCCGGGU")
        self.assertRaises(NotNucleotideError, RNA, "AUGUUUUAACCCUAG")

    def test_calculate_mass(self):
        mass = self.obj.calculate_mass()
        self.assertEqual(40203.4, mass)

    def test_mutate(self):

        # Input validation
        self.assertRaises(InputNotValidError, self.obj.mutate, 4, "T")
        self.assertRaises(InputNotValidError, self.obj.mutate, -1, "U")
        self.assertRaises(InputNotValidError, self.obj.mutate, 20, "U")
        self.assertRaises(InputNotValidError, self.obj.mutate, "20", "U")
        self.assertRaises(InputNotValidError, self.obj.mutate, 2, [])

        self.obj.mutate(5, "A")
        self.assertEqual("AUGUUACCCUAG", str(self.obj))

        self.obj.mutate(2, "C")
        self.assertEqual("AUCUUACCCUAG", str(self.obj))

        self.obj.mutate(11, "U")
        self.assertEqual("AUCUUACCCUAU", str(self.obj))

    def test_validate_sequence(self):
        obj_1 = RNA("AUGUUUCCCUAG")

        obj_1.mutate(0, "U")
        self.assertFalse(obj_1.validate_sequence())

        obj_1.mutate(0, "A")
        obj_1.mutate(9, "C")
        self.assertFalse(obj_1.validate_sequence())

        obj_1.mutate(9, "U")
        self.assertTrue(obj_1.validate_sequence())

    def test_rna_generator(self):
        obj_2 = RNA("AUGUUUCCCUAG").RNA_generator()

        self.assertEqual("AUG", next(obj_2))
        self.assertEqual("UUU", next(obj_2))
        self.assertEqual("CCC", next(obj_2))
        self.assertEqual("UAG", next(obj_2))


if __name__ == "__main__":
    main()
