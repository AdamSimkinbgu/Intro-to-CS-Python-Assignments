###################################### ---Q1B--- ######################################
from BinarySearchTree import BinarySearchTree

def complement_BST_DNA(sequence_BST: BinarySearchTree):
    """
    Using the API, creates an inorder sorted list of nodes. inverting the list and replacing each letter with the
    complement nucleotide. and returning it as a string.
    :param sequence_BST [BinarySearchTree] - A given root of a BST.
    :return [str] of the complement strand as required by the assignment.
    """
    l1 = BinarySearchTree.inorder(sequence_BST)
    l2 = ''
    for letter in l1[::-1]:
        argument = (lambda x: 'T' if x == 'A' else 'A' if x == 'T' else 'G' if x == 'C' else 'C' if x == 'G' else None)(letter[1])
        l2 += argument
    return l2

