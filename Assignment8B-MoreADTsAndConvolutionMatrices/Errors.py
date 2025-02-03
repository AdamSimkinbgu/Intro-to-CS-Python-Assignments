class NotNucleotideError(Exception):
    """ Used to indicate a bad nucleotide - bad input of any sort """
    pass

class DNASequenceError(Exception):
    """ Used to indicate a bad DNA sequence - invalid appearance of DNA """
    pass

class RNAToProteinError(Exception):
    """ Used to indicate a bad RNA that can't be translated to amino acids - invalid appearance of DNA """
    pass

class InputNotValidError(Exception):
    """ Used to indicate a bad input - a message would clarify the cause """
    pass