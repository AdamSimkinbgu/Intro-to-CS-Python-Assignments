from abc import ABC, abstractmethod
from Errors import NotNucleotideError
from LinkedList import LinkedList


class Nucleotides(ABC):
    """
    An abstract class the inherits to DNA and RNA classes which are in WD.
    """
    _nucleotides_mass = {}  # The dict of nucleotides masses, empty at first - a function at the end fills it up.

    def __init__(self, sequence):
        """
        Receives a string of letters and checks whether it has only allowed chars. If valid, creates linked list
        attribute "nucleotides_sequence".
        :param sequence [str] - A string of letters representing DNA/RNA contents - denied if given invalidly.
        """
        if not isinstance(sequence, str):
            raise TypeError('The sequence must be a string!')
        if sequence is None:  #  if a sequence is passed from the "FastaFileReader" class incorrectly, sequence will be None.
            raise KeyError("It seems the key you've entered does not appear in the file.")
        for letter in sequence:
            if letter not in ['A', 'T', 'G', 'C', 'U']:
                raise NotNucleotideError('At lease one nucleotide is not correct and cannot be "Nucleotides"')
        linked_list = LinkedList()
        for letter in sequence:
            linked_list.add_at_end(letter)
        self._nucleotides_sequence = linked_list
        str_sequence = str(self._nucleotides_sequence)
        self._nucleotides_number = {letter: str_sequence.count(letter) for letter in set(str(self._nucleotides_sequence))}

    def __str__(self):
        return str(self._nucleotides_sequence)

    def __len__(self):
        return len(str(self._nucleotides_sequence))

    def get_number_nucleotides(self):
        """
        Returns a dictionary containing the number of occurrences of nucleotides in a given strand
        """
        return self._nucleotides_number

    """ A couple of abstract, passed down the line to be implemented. Static functions provide the base variables 
        required for the questions in the assignment. """
    @abstractmethod
    def calculate_mass(self):
        pass

    @abstractmethod
    def mutate(self):
        pass

    @staticmethod
    def get_nuc_dict():
        return Nucleotides._nucleotides_mass

    @staticmethod
    def create_nuc_dict(dictionary):
        """
        Creates a dictionary for the nucleotide masses in a given file (must be in WD).
        :param dictionary [dict] - An empty dict to be filled with nucleotide masses information.
        :return None.
        """
        if not dictionary:
            with open("NucleotideMW.txt", 'r') as f:
                f.readline()
                temp = f.readline().split(" ")
                while temp != ['']:
                    dictionary[temp[0].split("(")[1][0]] = float(temp[2].split(f'\n')[0])
                    temp = f.readline().split(" ")

    create_nuc_dict(_nucleotides_mass)  #  calls the creation of the mass dictionary

