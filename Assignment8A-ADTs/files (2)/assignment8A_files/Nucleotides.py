from abc import ABC, abstractmethod


class Nucleotides(ABC):

    def __init__(self, sequence):
        pass

    @abstractmethod
    def calculate_mass(self):
        pass

    @abstractmethod
    def mutate(self):
        pass
