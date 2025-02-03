from unittest import TestCase, main
from FastaFileReader import *


class TestFastaFileReader(TestCase):
    def setUp(self) -> None:
        self.fasta_file = FastaFileReader("sequence_example.fna")

    def test_init(self):
        self.assertRaises(FileNotFoundError, FastaFileReader, "sequence.example.tx")
        self.assertRaises(FileNotFoundError, FastaFileReader, "sequence.exampl.txt")
        # print(self.fasta_file.sequences_dict.keys())

    def test_transcript(self):
        self.assertTrue(self.fasta_file.transcript('NC_000011.10:c5249857-5248269 HBG1 [organism=Homo sapiens]'
                                                   ' [GeneID=3047] [chromosome=11]'))

        self.assertFalse(self.fasta_file.transcript('NC_000011.10:c5249857-5248269 HBG1 [organism=Homo sapiens]'
                                                    ' [GeneID=307] [chromosome=11]'))

    def test_translate(self):
        self.assertTrue(self.fasta_file.translate('NC_000011.10:c5249857-5248269 HBG1 [organism=Homo sapiens]'
                                                  ' [GeneID=3047] [chromosome=11]'))

        self.assertFalse(self.fasta_file.translate('NC_000011.10:c5249857-5248269 HBG1 [organism=Homo sapiens]'
                                                   ' [GeneID=307] [chromosome=11]'))


if __name__ == "__main__":
    main()
