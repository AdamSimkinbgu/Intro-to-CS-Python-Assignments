from Errors import NotNucleotideError, DNASequenceError
from Nucleotides import Nucleotides


class RNA(Nucleotides):

    def verified_DNA_to_RNA(self):
        """ This method is used to check whether a DNA sequence is valid to be transcribed as RNA - Never understood
            whether it's needed or not, haven't seen a reason to implement its use here. """
        if len(self._nucleotides_sequence) % 3 != 0 or len(self._nucleotides_sequence) < 6:
            raise DNASequenceError('The given sequence is not valid to the requirements of a valid DNA.')
        if (('TGA' or 'TAA' or 'TAG') in [str(self._nucleotides_sequence)[i:i + 3] for i in range(0, len(self._nucleotides_sequence) - 3, 3)]) or not (str(self._nucleotides_sequence)[-3:] in ('TGA' or 'TAA' or 'TAG')):
            raise DNASequenceError('Either the end triplets are incompatible or they appear before the end of the sequence.')
        if str(self._nucleotides_sequence)[:3] != 'ATG':
            raise NotNucleotideError('At lease one nucleotide is not correct in DNA')
        return True

    def __init__(self, sequence):
        super().__init__(sequence)
#        self.verified_DNA_to_RNA()
        index = 0
        temp_sequence = str(self._nucleotides_sequence)
        for letter in temp_sequence:
            if letter == 'T':
                self._nucleotides_sequence.delete(index)
                self._nucleotides_sequence.insert(index, 'U')
                index += 1
            else:
                index += 1

    def calculate_mass(self):
        """
        Calculates the mass of an RNA strand.
        :return [float] RNA mass
        """
        total_mass = 0
        for main_strand_letter in str(self._nucleotides_sequence):
            total_mass += self._nucleotides_mass.get(main_strand_letter, 0)
        total_mass += 70 * self._nucleotides_mass.get('A')
        return total_mass

    def mutate(self, mutation_position, nucleotide_letter):
        """
        A simpler version or the DNA mutate function, allowing only one nucleotide to be replaced and allowing only
        replacements.
        :param mutation_position [int] - A selected position to mutate
        :param nucleotide_letter [str] - The letter to replace with the letter in the sequence.
        :return None, the function works in place to change the attributes of a give instance of the class.
        """
        nucleotides_length = len(self._nucleotides_sequence)
        if 0 <= mutation_position < nucleotides_length:
            self._nucleotides_sequence[mutation_position] = nucleotide_letter

    def RNA_generator(self):
        """
        A generator, iterating over each triplet of nucleotides in an RNA sequence.
        :return [str] - An iteration of nucleotides.
        """
        for nucleotide in [str(self._nucleotides_sequence)[i:i + 3] for i in range(0, len(self._nucleotides_sequence), 3)]:
            yield nucleotide
        raise StopIteration("You've reached the end of the iteration cycle.")

    def validate_sequence(self):
        """
        A method to test the validity of a given sequence to be translated to amino acids.
        :return [bool]
        """
        temp = str(self._nucleotides_sequence)
        for i in range(0, len(temp) - 3, 3):
            if temp[i:i + 3] in ['UGA', 'UAG', 'UAA']:
                return False
        if not temp[-3:] in ['UGA', 'UAG', 'UAA']:
            return False
        if temp[:3] != 'AUG' or "T" in temp:
            return False
        return True

