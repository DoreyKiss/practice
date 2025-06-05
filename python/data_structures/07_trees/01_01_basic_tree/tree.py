class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None


class Tree:
    def __init__(self, root: Node, name: str = "") -> None:
        self.root: Node = root
        self.name: str = name


node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

myTree = Tree(node, "Ryan's Tree")

print(myTree.name)
if myTree.root.right and myTree.root.right.right:
    print(myTree.root.right.right.data)
if myTree.root.left:
    print(myTree.root.left.data)
