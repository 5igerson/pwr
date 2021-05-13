
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def add(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            self._add(self.root,val)

    def _add(self,curr,val):
        if self.root==None:
            self.root=Node(val)
        else:
            if val<curr.value:
                if curr.left==None:
                    curr.left=Node(val)
                else:
                    self._add(curr.left,val)
            else:
                if curr.right==None:
                    curr.right=Node(val)
                else:
                    self._add(curr.right,val)                

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,curr):
        if curr!=None:
            self._print_tree(curr.left)
            print(str(curr.value))
            self._print_tree(curr.right)

def fill_tree(tree,num_of_els=5,max_val=1000):
    from random import randint
    for k in range(num_of_els):
        curr_element=randint(0,max_val)
        tree.add(curr_element)
    return tree


tree=BST()
tree=fill_tree(tree)
tree.print_tree()
