############################################################################################################################################
# Name: trees_graphs.py
# Description: This file has all the functions and classes which are related to trees and graphs.
# References: -
# Date: 10/5/2016
############################################################################################################################################

class binary_tree_node(object):
    '''
    This is the individual node of a binary tree. It has following fields  - data, parent node link, left child node link and right child node link.
    '''
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def node_data(self):
        return self.data

    @node_data.setter
    def node_data(self, data):
        self.data = data

    @property
    def node_parent(self):
        return self.parent

    @node_parent.setter
    def node_parent(self, value):
        self.parent = value

    @property
    def node_left(self):
        return self.left

    @node_left.setter
    def node_left(self, value):
        self.left = value

    @property
    def node_right(self):
        return self.right

    @node_right.setter
    def node_right(self, value):
        self.right = value



class binary_tree(object):
    '''
    This is a binary tree representation. It uses binary_tree_node as individual node elements. It has a link to root of the tree.
    '''
    def __init__(self):
        '''
        constructor of the binary tree
        '''
        self.tree_root = None

    def preorder(self):
        '''
        This will print nodes of tree in the order Root Left Right
        '''
        self.preorder_recursive(self.tree_root)

    def preorder_recursive(self, node):
        '''
        Given a node, it will print the nodes of subtree in the order Root Left Right
        params: node - This is the root of the subtree whose preorder needs to be printed.
        '''
        if node is not None:
            print node.node_data
            self.preorder_recursive(node.node_left)
            self.preorder_recursive(node.node_right)

    def postorder(self):
        '''
        This will print the nodes of a tree in the order Left Right Root
        '''
        self.postorder_recursive(self.tree_root)

    def postorder_recursive(self, root):
        '''
        Given a node, it will print the subtree of the node in the order Left Right Root
        params: root - THis will act as the root of the subtree for which postorder has to be implemented.
        '''
        if root is not None:
            self.postorder_recursive(root.node_left)
            self.postorder_recursive(root.node_right)
            print root.node_data

    def inorder_recursive(self, root):
        '''
        Given a node, it will print the subtree of the root in the order Left Root Right. It will print in ascending order
        params: root - This will act as the root of the subtree whose inorder has to be printed. 
        '''
        if root is not None:
            self.inorder_recursive(root.node_left)
            print root.node_data
            self.inorder_recursive(root.node_right)

    def inorder(self):
        '''
        This will print the inorder of the tree that is Left Root Right. It basically prints in ascending order
        '''
        self.inorder_recursive(self.tree_root)

    def findnode(self, item, root = None):
        '''
        This will find the node in the tree which has data as item.
        params: item - value which needs to be used to search the node.
        return: node which has the data as item. If not found None
        '''
        if root is None:
            root = self.tree_root
        while root is not None:
            if root.node_data == item:
                return root
            elif root.node_data > item:
                root = root.node_left
            else:
                root = root.node_right
        
        return None

    def addnode(self, item):
        '''
        THis function will add the given item to the appropiate place in the tree. A new node will be created for this item and then added to its location.
        param: item - value that needs to be added to the tree.
        '''
        root = self.tree_root
        prevNode = None
        while root is not None:
            if root.node_data > item:
                prevNode = root
                root = root.node_left
            else:
                prevNode = root
                root = root.node_right
        new_node = binary_tree_node(item, prevNode)
        if prevNode is not None:
            
            if prevNode.node_data > item:
                prevNode.node_left = new_node
            else:
                prevNode.node_right = new_node
        else:
            self.tree_root = new_node

    def findMaximum_pernode(self, node):
        '''
        This function will get the node having the maximum value under the subtree whose root is passed node.
        params: node - will act as the root of the subtree whose maximum value needs to be obtained.
        return: a node whose value is maximum among the subtree
        '''
        root = node
        while root.node_right is not None:
            root = root.node_right

        return root

    def findMaximumNode(self):
        '''
        This function will get the maximum value present in the whole tree.
        params: -
        return: node which has the maximum value
        '''
        return self.findMaximum_pernode(self.tree_root)

    def findMinimum_pernode(self, node):
        '''
        This function will get the minimum value present in the sub tree whose root is the passed node.
        params: node - root of the subtree whose minimum value needs to be found.
        return: a node containing the minimum value for the subtree
        '''
        root = node
        while root.node_left is not None:
            root = root.node_left
        return root

    def findMinimumNode(self):
        '''
        This function will get the node which has the minimum value among all the nodes in the tree.
        params: - 
        return: node which has minimum value among all the nodes in the tree.
        '''
        return self.findMinimum_pernode(self.tree_root)

    def findSuccessor_overall(self, node):
        '''
        This function will get the successor node that is node having next greater value than the passed in nodes data. Here context is whole tree
        params: node - whose successor needs to be found.
        return: node having next greater value than the node's value.
        '''
        succ_or = None
        if node is not None:
            succ_or = self.findsuccessor(node)
            if succ_or is None:
                succ_or = node.node_parent
        return succ_or

    def findPredecessor_overall(self, node):
        '''
        This function will get the predecessor node that is node having next lesser value than the passed in nodes data. Here context is whole tree
        params: node - whose predecessor needs to be found.
        return: node having next lesser value than the node's value.
        '''
        pred_or = None
        if node is not None:
            pred_or = self.findpredecesor(node)
            if pred_or is None:
                pred_or = node.node_parent
        return pred_or

    def findsuccessor(self, node):
        '''
        This function will get the successor node for the given subtree(whose root is passed node). Successor means next greater value.
        params: node - node whose successor has to be found. Also this acts as the root of the subtree.
        return: None if no successor found that is no right child. Else node having next great value.
        '''
        if node is not None:
            if node.node_right is not None:
                temp = self.findMinimum_pernode(node.node_right)
                if temp is not None:
                    return temp
                else:
                    return node.node_right
        return None

    def findpredecesor(self, node):
        '''
        This function will get the predecessor node for the given subtree(whose root is passed node). Predecessor means next lesser value.
        params: node - node whose predecessor has to be found. Also this acts as the root of the subtree.
        return: None if no predecessor found that is no left child. Else node having next less value.
        '''
        if node is not None:
            if node.node_left is not None:
                temp = self.findMaximum_pernode(node.node_left)
                if temp is not None:
                    return temp
                else:
                    return node.node_left

        return None

    def isLeaf(self, node):
        '''
        Checks if the given node is a leaf node or not
        param: node - node which needs to be verified whether it is leaf node
        return: true if it is a leaf node else false
        '''
        if node.node_left is None and node.node_right is None:
            return True
        else:
            return False

    def isRoot(self, node):
        '''
        Checks if the given node is a root node or not. (can be compared directly to tree_root)
        param: node - node which needs to be verified whether it is root or not.
        return: true if it is a root node else false.
        '''
        if node.node_parent is None:
            return True
        else:
            return False
    
    def delnode(self, item, root=None):
        '''
        This funciton will delete the given item. It will first find the node of the item. If the given item is a leaf then directly delete.
        Else check if node has right child. If yes then find the successor of the node. Replace with the current node with the successor.
        Else get the predeccesor of the child. Replace the predecessor with the current node.
        param: item - node having this value needs to be deleted.
        return: - 
        '''
        if root == None:
            root = self.tree_root

        node = self.findnode(item, root)
        if node is not None:
            if node.node_right is None and node.node_left is None:
                if node.node_parent is not None:
                    if node.node_parent.node_left == node:
                        node.node_parent.node_left = None
                    else:
                        node.node_parent.node_right = None

                if node == self.tree_root:
                    self.tree_root = None
            elif node.node_left is None or node.node_right is None:
                child = None
                if node.node_left is not None:
                    child = node.node_left
                else:
                    child = node.node_right

                if node.node_parent.node_left == node:
                    node.node_parent.node_left = child
                    child.node_parent = node.node_parent
                else:
                    node.node_parent.node_right = child
                    child.node_parent = node.node_parent
            else:
                succ_or = self.findsuccessor(node)
                node.node_data = succ_or.node_data
                self.delnode(node.node_data, node.node_right)








