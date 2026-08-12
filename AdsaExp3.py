class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert node into BST
def insert_node(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)

    return root


# Pre-order: Root -> Left -> Right
def preorder(node):
    if node is None:
        return

    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


# In-order: Left -> Root -> Right
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


# Post-order: Left -> Right -> Root
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


# Main program
root = None

n = int(input("Enter number of nodes: "))

print("Enter the values:")

for i in range(n):
    data = int(input())
    root = insert_node(root, data)


print("\nPre-order Traversal:")
preorder(root)

print("\n\nIn-order Traversal:")
inorder(root)

print("\n\nPost-order Traversal:")
postorder(root)

print()
