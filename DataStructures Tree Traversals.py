"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    #Write your code here
    if root!=None:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)

def preOrder(root):
    if root != None:
        print root.data,
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root !=None:
        postOrder(root.left)
        postOrder(root.right)
        print root.data
                    