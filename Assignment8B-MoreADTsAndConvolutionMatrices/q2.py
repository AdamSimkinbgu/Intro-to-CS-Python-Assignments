###################################### ---Q2--- ######################################
from BinarySearchTree import TreeNode
from BinaryTree import BinaryTree
from Stack import Stack


def print_right_view(binary_tree):
    """
    An algorithm of RSV to the binary tree. Using 2 lists, able to track the current level the algorithm is currently
    looking at, and adding to it from the left side of the tree to the right side. each item also adds its right and
    left nodes to the list of the next level. each cycle the right most item of the last level is added to a list of
    results. By doing this algorithm, a list of values, each of each level height of the tree is added to it.
    :param binary_tree [BinaryTree] - A given BinaryTree class root.
    :return [list] of RSV nodes in order.
    """
    result = []
    current_level = [binary_tree.root]
    if not current_level or current_level[0] == None:
        return result
    while current_level:
        result.append(current_level[-1].val)
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current_level = next_level
    return result


    # VVV another version VVV

    # res_list = []
    # queue = Stack()
    # queue.push(binary_tree.root)
    #
    # while queue:
    #     right_view = None
    #     queue_len = len(queue)
    #     for _ in range(queue_len):
    #         temp_queue = Stack()
    #         while not queue.is_empty():
    #             temp_queue.push(queue.pop())
    #         temp = temp_queue.pop()
    #         while not temp_queue.is_empty():
    #             queue.push(temp_queue.pop())
    #         # print(f'before push: {queue}')   # a few prints to follow the algorithms path
    #         if temp != None :
    #             right_view = temp
    #             if temp.left:
    #                 queue.push(temp.left)
    #                 # print(f'after second push: {queue}')
    #             if temp.right:
    #                 queue.push(temp.right)
    #                 # print(f'after first push: {queue}')
    #
    #
    #     if right_view != None:
    #         # print(f'temp to add: {right_view.val}')
    #         res_list.append(right_view.val)
    #
    # return res_list











    #### Code grave yard

    # g_queue = Stack()
    # result = []
    #
    # def inorder_rec(curr_node, queue, h):
    #     if curr_node is not None:
    #         if curr_node.left is not None:
    #             queue.push(curr_node.left.val)
    #         if curr_node.right is not None:
    #             queue.push(curr_node.right.val)
    #
    #         inorder_rec(curr_node.left, queue, h + 1)
    #         inorder_rec(curr_node.right, queue, h + 1)
    #         if not queue.is_empty():
    #             result.append(queue.pop())
    #
    # inorder_rec(binary_tree.root, g_queue, h=0)
    # return result







    # def inorder_right_rec(curr_node, h):
    #     if curr_node is not None:
    #         inorder_right_rec(curr_node.right, h + 1)
    #         if h not in dicto.keys():
    #             res.append(curr_node.val)
    #             dicto[h] = (curr_node.key, curr_node.val)
    #         inorder_right_rec(curr_node.left, h + 1)
    #
    # res = []
    # dicto = {}
    # inorder_right_rec(binary_tree.root, h=0)
    # return res[::-1]


