from DoublyLinkedList import DoublyLinkedList
from Errors import NotNucleotideError, DNASequenceError, InputNotValidError
from Nucleotides import Nucleotides


class DNA(Nucleotides):
    def __init__(self, sequence):   # todo to check the sequences here so that the correct error are raised
        """
        Using a given sequence, passes it to Nucleotides for initialization, then checks whether nucleotide 'U' is
        present in the sequence. If so, raises DNASequenceError.
        :param sequence [str] - A string of letters representing DNA contents - denied if given invalidly.
        """
        super().__init__(sequence)
        temp_sequence = str(self._nucleotides_sequence)
        for letter in temp_sequence:
            if letter == 'U':
                raise DNASequenceError("DNA sequence must contain only 'A', 'T', 'C', 'G'.")


    def complement(self):
        """
        Creates a doublylist representing the complement strand of DNA as instructed in the assignment letter.
        :return
        """
        complement_strand = DoublyLinkedList()
        main_strand_seq = str(self._nucleotides_sequence)
        for letter in main_strand_seq:
            argument = (lambda x: 'T' if x == 'A' else 'A' if x == 'T' else 'G' if x == 'C' else 'C' if x == 'G' else None)(letter)
            if argument:
                complement_strand.push(argument)
        return complement_strand

    def calculate_mass(self):
        """
        Calculates the mass of the strands with the dict of masses in Nucleotides.
        :return A float of the total mass.
        """
        total_mass = 0
        compliment_strand_to_calc = DNA.complement(self)
        for main_strand_letter in str(self._nucleotides_sequence):
            total_mass += self._nucleotides_mass.get(main_strand_letter, 0)
        for compliment_strand_letter in str(compliment_strand_to_calc):
            total_mass += self._nucleotides_mass.get(compliment_strand_letter, 0)
        return total_mass


    def mutate(self, mutation_type, mutation_position, nucleotides_mutation):
        """
        This function is the pure embodiment of satan himself. in only! ONLY! 24 lines of code, you are able to
        command the addition of new DNA nucleotides to the sequence, replace the selected nucleotides or completely
        destroy selected nucleotides using evil magic called "loops" (shush! don't tell the witch in the forest!)
        eRRorS WiLL oCuRE iF inDEx OR NuCLeoTIdes MuTAtiOn Is INcoRRect
        #Funny how it does mark these as typos ¯\_(ツ)_/¯
        ## this is the result of too many hours of non sleep coding, sounds fun!
        # If I had a little more time, I would've broken the code to smaller segments.
        :param mutation_type [str] - A selected mode of mutation.
        :param mutation_position [int] - A selected position to mutate
        :param nucleotides_mutation [str] - The sequence to manipulate the sequence with.
        :return None, the function works in place to change the attributes of a give instance of the class.
        """
        try:
            DNA(nucleotides_mutation)
        except DNASequenceError:
            raise InputNotValidError('The mutation is invalid due to the sequence it contains.')
        if 0 <= mutation_position < len(self._nucleotides_sequence):
            if mutation_type == 'addition':
                if mutation_position == len(self._nucleotides_sequence) - 1:
                    for letter in nucleotides_mutation:
                        self._nucleotides_sequence.add_at_end(letter)
                elif mutation_position == 0:
                    for letter in nucleotides_mutation[::-1]:
                        self._nucleotides_sequence.add_at_start(letter)
                else:
                    for letter in nucleotides_mutation[::-1]:
                        self._nucleotides_sequence.insert(mutation_position, letter)
            elif mutation_type == 'replacement':
                if len(self._nucleotides_sequence) > len(nucleotides_mutation):
                    for _ in nucleotides_mutation:
                        self._nucleotides_sequence.delete(mutation_position)
                    for letter in nucleotides_mutation[::-1]:
                        self._nucleotides_sequence.insert(mutation_position, letter)
                else:
                    raise ValueError('Your inputs are incompatible with the laws of nature, you mutant')
            elif mutation_type == 'deletion':
                temp_mut_seq = DoublyLinkedList()
                for letter in str(self._nucleotides_sequence)[mutation_position: mutation_position + len(nucleotides_mutation)]:
                    temp_mut_seq.append(letter)
                if str(temp_mut_seq) == nucleotides_mutation:
                    if len(self._nucleotides_sequence) - (mutation_position + len(nucleotides_mutation)) >= 0:
                        for _ in nucleotides_mutation:
                            self._nucleotides_sequence.delete(mutation_position)
                    else:
                        raise ValueError('The selected nucleotide and/or index are surpassing the index limit.')
                else:
                    raise ValueError('The input nucleotide is not compatible with the nucleotide in the sequence')
        else:
            raise InputNotValidError('The index you are trying manipulate is out the bounds of the sequence.')
