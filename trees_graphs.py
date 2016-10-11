############################################################################################################################################
# Name: trees_graphs.py
# Description: This file has all the functions and classes which are related to trees and graphs.
# References: -
# Date: 10/5/2016
############################################################################################################################################

import numpy as ny

class binary_tree_node(object):
    '''
    This is the individual node of a binary tree. It has following fields  - data, parent node link, left child node link and right child node link.
    '''
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance_factor = 0
        self.level = 0

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

    @property
    def node_balance_factor(self):
        return self.balance_factor

    @node_balance_factor.setter
    def node_balance_factor(self, value):
        self.balance_factor = value

    @property
    def node_level(self):
        return self.level

    @node_level.setter
    def node_level(self, value):
        self.level = value



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

    def findTreeheight(self):
        '''
        This function will give you the height of the BST tree
        params: -
        return: height of the tree.
        '''
        self.findnodeheight(self.tree_root)

    def findnodeheight(self, root):
        '''
        This function will give you the height of the Binary Search sub tree which is rooted at passed node.
        params: root - node which acts as the root of the subtree and whose height needs to be calculated.
        return: height of the root in the tree.
        '''
        right_child_height = 0
        left_child_height = 0

        if root is not None:
            if root.node_right is not None:
                right_child_height = self.findnodeheight(root.node_right) 

            if root.node_left is not None:
                left_child_height = self.findnodeheight(root.node_left)

        return max(left_child_height, left_child_height) + 1


class simpleChainedHashTable(object):
    '''
    This is a simple hashtable. It uses linked list to avoid collision.  
    Its complexity of find is O(1) and for insert it is asympotically O(1)
    '''
    def __init__(self, size=10, hashfunc=hash):
        '''
        THis is the constructor of this class. User can provide the initial capacity of the hashtable.
        By default it uses size as 10 and default hashfunction as inbuilt hash
        params: size - initial capacity of the hashtable
                hashfunc - Function used to find the index in the hashtable for the passed key.
        returns: - 
        '''
        self.actual_storage = []
        self.size = size
        self.count = 0
        self.threshold = 0.8
        self.stepsize = 10
        self.hashfunc = hashfunc
        for i in range(0, self.size):
            self.actual_storage.append([])

    def increaseCapacity(self):
        '''
        This function will be used increase the capacity of the hashtable when the number of elements in the hashtable 
        crosses certain threshold. Not only we need to increase the capacity we need to rehash the existing key, value pairs
        to the new hashtable.
        params: - 
        return: - 
        '''
        new_size = self.size + self.stepsize
        new_array = []
        for i in range(0, new_size):
            new_array.append([])

        for i in range(0, self.size):
            for (p_key, p_value) in self.actual_storage[i]:
                index = self.hashfunc(p_key)%new_size
                new_array[index].append((p_key, p_value))

        self.size = new_size
        self.actual_storage = new_array

    def setitem(self, key, value):
        '''
        This function is used to insert the key value pair into the hash table. If key is already present, then modify the value
        with the new one.
        params: key - this will be used to find the index of the hashtable
                value - this is value to be stored in hashtable
        return: - 
        '''
        index = self.hashfunc(key)%self.size
        if self.actual_storage[index].__len__() == 0:
            self.actual_storage[index].append((key, value))
            self.count += 1
        else:
            it = 0
            bFound = False
            for (p_key, p_value) in self.actual_storage[index]:
                if p_key == key:
                    self.actual_storage[index][it] = (key, value)
                    bFound = True
                    break
                it += 1
            if bFound is False:
                self.actual_storage[index].append((key, value))
                self.count += 1

        if float(self.count)/self.size >= self.threshold:
            self.increaseCapacity()

    def getItem(self, key):
        '''
        This function is used to get the value for the provided key. If not found then 
        it raise an exception.
        params: key - key whose value needs to be retreived.
        return: value corresponding to the key.
        '''
        value = None
        index = self.hashfunc(key)%self.size
        bFound = False
        for (p_key,p_value) in self.actual_storage[index]:
            if p_key == key:
                value = p_value
                bFound = True
                break

        if bFound is False:
            raise Exception('key not found')

        return value

    def delItem(self, key, value=None):
        '''
        This function is used to delete the key, value pair corresponding to the key.
        params: key - whose corresponding entry needs to be deleted.
        return: - 
        '''
        index = self.hashfunc(key)%self.size
        it = 0
        tobeDel = []
        for (p_key, p_value) in self.actual_storage[index]:
            if p_key == key:
                if value is not None:
                    if p_value == value:
                        tobeDel.append(it)
                else:
                    tobeDel.append(it)
            it += 1
        for i in tobeDel:
            del self.actual_storage[index][i]
            self.count -= 1

    def display(self):
        '''
        This function will display all the contents of the the hashtable.
        params: - 
        return: - 
        '''
        print '===================================================================='
        for i in range(0, self.size):
            if self.actual_storage[i].__len__() == 0:
                print str(i), '--> []'
            else:
                mystr = str(i) + ' --> ['
                vstr = ''
                for (pkey, pvalue) in self.actual_storage[i]:
                    vstr = vstr + '('+str(pkey)+','+str(pvalue)+'),'
                vstr = vstr[:-1]
                mystr = mystr + vstr + ']'
                print mystr



class avl_tree(object):
    '''
    This is an avl tree. Its a self balancing tree. It makes sure that depth of the tree remains almost balanced. Basically leaves should be at the same distance from 
    the root. Either n or n-1
    '''
    def __init__(self):
        self.tree_root = None

    def inorder(self):
        '''
        THis is the funciton used by the outside world to display the contents of the tree in ascending order.
        It prints in Left Root Right order.
        params: - 
        return: - 
        '''
        print '================================================================================'
        self.inorder_rec(self.tree_root)

    def inorder_rec(self, root):
        '''
        This funciton will display the contents of the tree in the inorder that is acending order - Left Root Right.
        params: root - Starting point of the tree from where inorder has to be started.
        return: - 
        '''
        if root is not None:
            self.inorder_rec(root.node_left)
            print 'data = '+str(root.node_data) + ' Level = '+str(root.node_level) + ' Balance Factor = '+str(root.node_balance_factor)
            self.inorder_rec(root.node_right)

    def insert(self, item):
        '''
        THis is the funciton outside world uses to insert a new item inside the tree. But it intern calls insert_rec_node.
        params: item - number to be inserted inside the tree.
        return: - 
        '''
        new_node = binary_tree_node(data=item)
        if self.tree_root is None:
            self.tree_root = new_node
        else:
            self.insert_rec_node(self.tree_root, new_node)

    def rebalance_tree(self, root):
        '''
        THis function will rebalance the tree by performing either right rotation, left-right rotation, left rotation or right left rotation to
        correct the left-left case, left right case, right right case or right left case. Once rebalanced for this node. It will recalucate the 
        balance factors of the nodes below it.
        params: root - node which is the starting node of the portion which needs to be rebalanced.
        return: - 
        '''
        if root.node_balance_factor > 1:
            if root.node_left.node_balance_factor == 1: #Left-Left Case
                z = root
                y = root.node_left
                x = root.node_left.node_left
                t1 = root.node_left.node_left.node_left
                t2 = root.node_left.node_left.node_right
                t3 = root.node_left.node_right
                t4 = root.node_right

                #Right Rotation
                y.node_parent = z.node_parent
                y.node_right = z
                z.node_parent = y
                z.node_left = t3
                if t3 is not None:
                    t3.node_parent = z

                root = y
                if root.node_parent is None:
                    self.tree_root = y
                else:
                    root.node_parent.node_left = root

            else:                                       #Left-Right Case
                z = root
                y = root.node_left
                x = root.node_left.node_right
                t1 = root.node_left.node_left
                t2 = root.node_left.node_right.node_left
                t3 = root.node_left.node_right.node_right
                t4 = root.node_right

                #Left-Right Rotation
                x.node_parent = z.node_parent
                x.node_left = y
                x.node_right = z
                y.node_parent = x
                z.node_parent = x
                y.node_right = t2
                if t2 is not None:
                    t2.node_parent = y
                z.node_left = t3
                if t3 is not None:
                    t3.node_parent = z

                root = x
                if root.node_parent is None:
                    self.tree_root = x
                else:
                    root.node_parent.node_left = root

        else:
            if root.node_right.node_balance_factor == -1: #Right-Right Case
                z = root
                y = root.node_right
                x = root.node_right.node_right
                t1 = root.node_left
                t2 = root.node_right.node_left
                t3 = root.node_right.node_right.node_left
                t4 = root.node_right.node_right.node_right

                #Left rotation
                y.node_parent = z.node_parent
                y.node_left = z
                z.node_parent = y
                z.node_right = t2
                if t2 is not None:
                    t2.node_parent = z

                root = y
                if root.node_parent is None:
                    self.tree_root = y
                else:
                    root.node_parent.node_right = root

            else:                                         #Right-Left Case
                z = root
                y = root.node_right
                x = root.node_right.node_left
                t1 = root.node_left
                t2 = root.node_right.node_left.node_left
                t3 = root.node_right.node_left.node_right
                t4 = root.node_right.node_right

                #Right Left rotation
                x.node_parent = z.node_parent
                x.node_left = z
                x.node_right = y
                z.node_parent = x
                y.node_parent = x
                z.node_right = t2
                if t2 is not None:
                    t2.node_parent = z
                y.node_left = t3
                if t3 is not None:
                    t3.node_parent = y

                root = x
                if root.node_parent is None:
                    self.tree_root = x
                else:
                    root.node_parent.node_right = root

        return root


    def insert_rec_node(self, root, new_node):
        '''
        THis function will insert a node to the subtree whose root is given in a recursive call. As it inserts it will also calculate the balance factor
        and if it is violating then rebalancing is done.
        params: root - subtrees root, under whom new_node needs to be added.
                new_node - This is the node to be added to the subtree whose root is given.
        return: -
        '''
        if root.node_left is None and root.node_right is None:
            if root.node_data < new_node.node_data:
                root.node_right = new_node
                new_node.node_parent = root
                root.node_level = new_node.node_level + 1
                root.node_balance_factor = -(new_node.node_level+1)
            else:
                root.node_left = new_node
                new_node.node_parent = root
                root.node_level = new_node.node_level + 1
                root.node_balance_factor = new_node.node_level+1
        else:
            if root.node_data < new_node.node_data:
                if root.node_right is not None:
                    self.insert_rec_node(root.node_right, new_node)
                else:
                    root.node_right = new_node
                    new_node.node_parent = root
            else:
                if root.node_left is not None:
                    self.insert_rec_node(root.node_left, new_node)
                else:
                    root.node_left = new_node
                    new_node.node_parent = root
                    
            if root.node_left is not None and root.node_right is not None:
                root.node_level = max(root.node_left.node_level, root.node_right.node_level) + 1

                root.node_balance_factor = root.node_left.node_level - root.node_right.node_level
            else:
                if root.node_left is None:
                    root.node_level = root.node_right.node_level + 1
                    root.node_balance_factor = -(root.node_right.node_level+1)
                else:
                    root.node_level = root.node_left.node_level + 1
                    root.node_balance_factor = root.node_left.node_level+1

        if root.node_balance_factor > 1 or root.node_balance_factor < -1:
            root = self.rebalance_tree(root)
            self.calculate_balance_factor(root)

    #def update_level_balance_factor(self


    def calculate_balance_factor(self, node=None):
        '''
        This function will help to calculate the balance factor of a node. If it violates any then 
        it will call rebalance function.
        params: node - node whose level/height and balance factor needs to be calculated.
        return: -
        '''
        if node == None:
            node = self.tree_root

        if node.node_left is None and node.node_right is None:
            node.node_level = 0
            node.node_balance_factor = 0
        else:
            if node.node_left is not None:
                self.calculate_balance_factor(node.node_left)
            if node.node_right is not None:
                self.calculate_balance_factor(node.node_right)

            if node.node_right is not None and node.node_left is not None:
                node.node_level = max(node.node_right.node_level, node.node_left.node_level) + 1
                node.node_balance_factor = node.node_left.node_level - node.node_right.node_level
            else:
                if node.node_right is None:
                    node.node_level = node.node_left.node_level + 1
                    node.node_balance_factor = node.node_left.node_level+1
                else:
                    node.node_level = node.node_right.node_level + 1
                    node.node_balance_factor = -(node.node_right.node_level +1)
        
        if node.node_balance_factor > 1 or node.node_balance_factor < -1:
            node = self.rebalance_tree(node)

class simpleOpenHashTable(object):
    '''
    THis is a dictionary which follows the concept of open hashing.
    '''
    def __init__(self, size=10, hashfunc=hash):
        self.actualArray = []
        self.size = size
        self.loadFactor = 0.8
        self.count = 0
        self.hashfunc = hashfunc
        
        for i in range(0, size):
            self.actualArray.append(None)

    def increaseCapacity(self):
        '''
        This function will increase the size of the array on violation of load factor condition. It also rebuilds the hashtable after increasing 
        the size as now index will be different.
        params: - 
        return: - 
        '''
        new_size = self.size + 10
        new_array = []

        for i in range(0, new_count):
            new_array.append(None)

        for i in range(0, self.size):
            tup = self.actualArray[i]
            for j in range(0, new_size):
                index = (self.hashfunc(tup[0])+j)%new_size
                if new_array[index] is None:
                    new_array[index] = tup
                    break

        self.count = new_size
        self.actualArray = new_array

    def __setitem__(self, key, value):
       '''
       THis function will set a new item to the dictionary. After inserting new element or updating existing one, it will check the load balance.
       If it is more than that then it will rebuild the dictionaryd with new size.
       params: key - item used for finding the index in the array.
               value - actual item to be stored.
       return: -
       '''
       if self.__contains__(key):
           for i in range(0, self.size):
               index = (self.hashfunc(key)+i)%self.size
               xtuple = self.actualArray[index]
               if xtuple[0] == key:
                   self.actualArray[index] = (key,value)
                   break
       else:
           for i in range(0, self.size):
               index = (self.hashfunc(key)+i)%self.size
               if self.actualArray[index] is None or self.actualArray[index] == (ny.Infinity, ny.Infinity):
                   self.actualArray[index] = (key, value)
                   self.count += 1
                   break
       if float(self.count)/self.size >= self.loadFactor:
            self.increaseCapacity

    def __contains__(self, key):
        '''
        This function will check whether given key exists in the dictionary. If it is present then it will return true else false.
        params: key - key to be searched in the dictionary.
        return: if present true else false
        '''
        for i in range(0, self.size):
            index = (self.hashfunc(key)+i)%self.size
            if self.actualArray[index] is None:
                return False
            else:
                if self.actualArray[index][0] == key:
                    return True
        return False

    def __getitem__(self, key):
        '''
        This function will get the item from the array based on the key. If not present then it will return None
        params: key - value used to find the item.
        return: if found then item else None
        '''
        for i in range(0, self.size):
            index = (self.hashfunc(key)+i)%self.size
            if self.actualArray[index] is None:
                return None
            else:
                if self.actualArray[index][0] == key:
                    return self.actualArray[index][1]
        return None

    def __delitem__(self, key):
        '''
        This function will delete the item present in the dictionary.
        params: key - value used to find the item to be deleted.
        return: -
        '''
        for i in range(0, self.size):
            index = (self.hashfunc(key)+i)%self.size
            if self.actualArray[index] is None:
                break
            else:
                if self.actualArray[index][0] == key:
                    self.actualArray[index] = (ny.Infinity, ny.Infinity)
                    break



class BTreeNode(object):
    def __init__(self, degree):
        self.degree = degree
        self.arkeys = []
        self.archildren = []
        self.parent = None
        self.isLeaf = True

    @property
    def node_parent(self):
        return self.parent

    @node_parent.setter
    def node_parent(self, value):
        self.parent = value

    @property
    def node_isLeaf(self):
        return self.isLeaf

    @node_isLeaf.setter
    def node_isLeaf(self, value):
        self.isLeaf = value

    @property
    def node_degree(self):
        return self.degree

    @node_degree.setter
    def node_degree(self, value):
        self.degree = value

    @property
    def node_keys(self):
        return self.arkeys

    @node_keys.setter
    def node_keys(self, value):
        self.arkeys = value

    @property
    def node_children(self):
        return self.archildren

    @node_children.setter
    def node_children(self, value):
        self.archildren = value

        

class BTree(object):
    '''
    This class will create a btree. It is generalized to have any degree of 'B' value.
    '''
    def __init__(self):
        '''
        Constructor of the class. It has only one member tree root. rest all are from the btree node which represents each node in this tree
        '''
        self.tree_root = None

    def inorder(self):
        '''
        This function is the interface given to outside world to display the element of the tree in inorder - Left Root Right way.
        params: -
        return: - 
        '''
        self.inorder_rec(self.tree_root)

    def inorder_rec(self, root):
        '''
        This function will print the elements in the subtree whose root is root in an inorder fassion - Left Root Right.
        params: root - Node whose subtree needs to be displayed in inorder.
        return: - 
        '''
        if root.node_isLeaf:
            for i in range(0, len(root.node_keys)):
                print root.node_keys[i]
        else:
            for i in range(0, len(root.node_keys)):
                self.inorder_rec(root.node_children[i])
                print root.node_keys[i]
            root.inorder_rec(root.node_children[i])

    def insert(self, element):
        '''
        This interface can be used for inserting a new element into the tree. It intern uses insert_rec a recursive function.
        params: - element - This is the element is to be inserted to tree.
        return: -
        '''
        self.insert_rec(self, self.tree_root, element)

    def split(self, node):
        '''
        This function is used to split a filled up node. When node keys capacity exceeds the 2B-2 condition, this function will be called.
        It will split the node into two new nodes. If it does not have a parent then it will form a new root for the tree, else add a new key 
        to the parent node. This will be recursively done from leaf till root.
        params: node - This is the node to be splitted into two.
        return - 
        '''
        mid_index = node.node_degree/2
        new_node1 = BTreeNode(node.node_degree)
        new_node2 = BTreeNode(node.node_degree)
        i = 0
        while i < mid_index:
            new_node1.node_keys.append(node.node_keys[i])
            if node.node_isLeaf is False:
                new_node1.node_children.append(node.node_children[i])
                node.node_children[i].node_parent = new_node1
            i += 1
        if node.node_isLeaf is False:
            new_node1.node_children.append(node.node_children[i])
            node.node_children[i].node_parent = new_node1
        i += 1
        while i < len(node.node_keys):
            new_node2.node_keys.append(node.node_keys[i])
            if node.node_isLeaf is False:
                new_node2.node_children.append(node.node_children[i])
                node.node_children[i].node_parent = new_node2
            i += 1

        if node.node_isLeaf is False:
            new_node2.node_children.append(node.node_children[i])
            node.node_children[i].node_parent = new_node2

        if node.node_parent is None:
            parent_node = BTreeNode(node.node_degree)
            parent_node.node_isLeaf = False
            parent_node.node_keys.append(node.node_keys[mid_index])
            new_node1.node_parent = parent_node
            new_node2.node_parent = parent_node
            parent_node.node_children.append(new_node2)
            parent_node.node_children.append(new_node1)
            self.tree_root = parent_node
        else:
            element = node.node_keys[mid_index]

            i = 0
            while(i < node.node_parent.node_keys.__len__()):
                if node.node_parent.node_keys[i] > element:
                    break
                i += 1

            del node.node_children[i]
            node.node_parent.node_keys.insert(i, element)
            node.node_children.insert(i, new_node2)
            node.node_children.insert(i, new_node1)

            new_node2.node_parent = node.node_parent
            new_node1.node_parent = node.node_parent

            if len(node.node_parent.node_keys ) > 2*node.node_parent.node_degree - 2:
                self.split(node.node_parent)

    def insert_rec(self, root, element):
        '''
        This function is used to add an element to a particular node. If by addition it crosses the limit of keys then it will call the
        split function to split the node into 2.
        params: root - node where new element needs to be added.
                element - new element to be added to tree.
        return: - 
        '''
        if root.node_isLeaf:
            i = 0
            while i < root.node_keys.__len__():
                if root.node_keys[i] > element:
                    break
                i += 1
            ls = []
            if i == root.node_keys.__len__():
                root.node_keys.append(element)
            else:
                root.node_keys.insert(i, element)

            if root.node_keys.__len__() >= 2*root.node_degree - 2:
                self.split(root)

        else:
            i = 0
            while i < len(root.node_keys):
                if element < root.node_keys[i]:
                    self.insert_rec(root.node_children[i], element)
                    break
                i += 1
            if i == root.noe_keys.__len__():
                self.insert_rec(root.node_children[i], element)

       



            











