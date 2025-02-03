from DNA import DNA
from Errors import DNASequenceError, RNAToProteinError
from RNA import RNA

RNA_to_Protien = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                  "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                  "UAU": "Y", "UAC": "Y",
                  "UGU": "C", "UGC": "C", "UGG": "W",
                  "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                  "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                  "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                  "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                  "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                  "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                  "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                  "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                  "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                  "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                  "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                  "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }


class FastaFileReader:
    """
    An execution class, using DNA, RNA and Nucleotides classes to transcript DNA to RNA and translate RNA to
    amino acids. The transcript and the translation are stored in new files created (or appended to) in the WD.
    """
    def __init__(self, pathway):
        """
        Tries to initialize a reading from a file, creating a dictionary attribute. If fails, throws FILENOTFOUND error.
        :param pathway [str] - String of a given path to a file
        """
        try:  #  Try to open a file using a given file
            temp_dict = {}
            with open(pathway, 'r') as f:
                list_of_sentences = f.readlines()
                for line in list_of_sentences:
                    if line[0] == '>':
                        current_key = line[1:-1]
                        temp_dict[current_key] = ''
                        continue
                    if line[-1] != '\n':
                        temp_dict[current_key] += line  #  if line does not contain '\n' to append, does this
                        continue
                    temp_dict[current_key] += line[:line.index('\n')]  # inserting the sequence to the dictionary
            self.sequences_dict = temp_dict
        except FileNotFoundError:
            raise FileNotFoundError("The file path that was given is invalid or incorrect")

    def transcript(self, sequence_details):
        """
        Using a given key (as string), reaches a value of sequence to transcript from DNA to RNA. If successful,
        appends the transcribed sequence to a file in the WD. The function operates one key at a time.
        :param sequence_details [str] - A string containing the key to a dictionary.
        :return A boolean statement.
        """
        dict_value = self.sequences_dict.get(sequence_details)
        dict_value = RNA(dict_value)
        is_good = dict_value.validate_sequence()
        if is_good == False:
            return False
        with open('sequence_transcription.fna', 'a') as a:
            a.write(f'>{sequence_details}\n')
            index = 1
            for letter in str(dict_value):
                a.write(letter)
                if index % 70 == 0:
                    a.write('\n')
                index += 1
            a.write('\n')
        return True

    def translate(self, sequence_details):
        """
        Using a given key (as string), reaches a value of sequence to translate from RNA to amino acids. This is
        done using the given dictionary at the top of the file. First, the function tries to cast the sequence
        to DNA, if successful, tries to cast the DNA to RNA. If successful again, validates the sequence using the
        validate_sequence function in the RNA class. Finally, translates the RNA triplets into amino acids and appends
        it to a file in the WD. If no errors occur, returns True. otherwise, returns False.
        The function operates one key at a time.
        :param sequence_details [str] - A string containing the key to a dictionary.
        :return A boolean statement.
        """
        triplets_to_translate = self.sequences_dict[sequence_details]
        try:
            seq_to_process = DNA(triplets_to_translate)
            try:
                seq_to_process = RNA(str(seq_to_process))
                ola = seq_to_process.validate_sequence()
                if ola == False:
                    raise RNAToProteinError
            except RNAToProteinError:
                return False
            except DNASequenceError:
                return False
        except DNASequenceError:
            return False
        returned_value = str(seq_to_process)
        with open('sequence_translation.faa', 'a') as b:
            b.write(f'>{sequence_details}\n')
            index = 1
            for i in range(0, len(returned_value) - 3, 3):
                val = RNA_to_Protien.get(returned_value[i: i + 3])
                b.write(val)
                if index % 70 == 0:
                    b.write('\n')
                index += 1
            b.write('stop')
            b.write('\n')
        return True

