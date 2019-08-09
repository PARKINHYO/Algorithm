from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_tree(node, target):
    if node == None: return
    if node.data == target[0]:
        if target[1] == '.':
            if target[2] == '.':
                return
            else:
                new_node = Node(target[2])
                node.right = new_node
        else:
            new_node = Node(target[1])
            node.left = new_node

            if target[2] == '.':
                return
            else:
                new_node = Node(target[2])
                node.right = new_node
        return

    search_tree(node.left, target)
    search_tree(node.right, target)


def preorder_traverse(node):
    if node == None: return
    print(node.data, end='')
    preorder_traverse(node.left)
    preorder_traverse(node.right)


def inorder_traverse(node):
    if node == None: return
    inorder_traverse(node.left)
    print(node.data, end='')
    inorder_traverse(node.right)


def postorder_traverse(node):
    if node == None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end='')


root = None


def init_tree(l):
    global root

    if root == None:
        new_node = Node(l[0])
        root = new_node

        if l[1] == '.':
            if l[2] == '.':
                return
            else:
                new_node = Node(l[2])
                root.right = new_node
        else:
            new_node = Node(l[1])
            root.left = new_node

            if l[2] == '.':
                return
            else:
                new_node = Node(l[2])
                root.right = new_node

    else:
        search_tree(root, l)


if __name__ == '__main__':
    N = int(stdin.readline())
    for i in range(N):
        my_node = list(stdin.readline().split())
        init_tree(my_node)

    preorder_traverse(root)
    print()
    inorder_traverse(root)
    print()
    postorder_traverse(root)
    print()
