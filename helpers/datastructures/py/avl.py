#!/usr/bin/env python3


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1
        self.bf = 0
    
    def contains(self, value):
        """Returns a boolean indicating whether the tree contains value"""
        node = self
        while node is not None:
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            else:
                return True
        return False
    
    def inorder(self):
        """Generator generating the inorder traversal of the tree"""
        if self.left:
            yield from self.left.inorder()
        yield self.value
        if self.right:
            yield from self.right.inorder()
    
    def min(self):
        """Get the minimum node in the tree"""
        node = self
        while node.left:
            node = node.left
        return node
    
    def max(self):
        """Get the maximum node in the tree"""
        node = self
        while node.right:
            node = node.right
        return node

    def update(self):
        """Update the balance factor of a node"""
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)
        self.bf = right_height - left_height

    def right_rotate(self):
        """Balance operation"""
        new_parent = self.left
        self.left = new_parent.right
        new_parent.right = self
        self.update()
        new_parent.update()
        return new_parent
    
    def left_rotate(self):
        """Balance operation"""
        new_parent = self.right
        self.right = new_parent.left
        new_parent.left = self
        self.update()
        new_parent.update()
        return new_parent

    def leftleft(self):
        """Balance operation"""
        return self.right_rotate()
    
    def leftright(self):
        """Balance operation"""
        self.left = self.left.left_rotate()
        return self.leftleft()
    
    def rightright(self):
        """Balance operation"""
        return self.left_rotate()
    
    def rightleft(self):
        """Balance operation"""
        self.right = self.right.right_rotate()
        return self.rightright() 

    def balance(self):
        """Rebalance the tree using the balance operations"""
        if self.bf == -2:
            if self.left.bf <= 0:
                return self.leftleft()
            else:
                return self.leftright()
        elif self.bf == 2:
            if self.right.bf >= 0:
                return self.rightright()
            else:
                return self.rightleft()
        return self
    
    def clone(self):
        new_node = Node(self.value)
        if self.left:
            new_node.left = self.left.clone()
        if self.right:
            new_node.right = self.right.clone()
        return new_node


class AVLTree:
    NULL_NODE = Node(None)

    def __init__(self):
        self.root = None
        self.size = 0
    
    def __add__(self, other):
        if self.size > other.size:
            to_clone = self
            get_from = other
        else:
            to_clone = other
            get_from = self
        clone = to_clone.clone()
        for node in get_from.inorder():
            clone.insert(node)
        return clone
    
    def __str__(self):
        return " ".join(map(str, self.inorder()))

    def insert(self, value):
        """Insert the value into the tree O(lg n)"""
        if self.root is None:
            self.root = Node(value)
            self.size = 1
            return self.root
        inserted = self._insert(self.root, value)
        # if this does not hold true then the value was already
        # contained within the tree
        if inserted is not AVLTree.NULL_NODE:
            self.size += 1
            self.root = inserted
        return inserted

    def contains(self, value):
        """Returns a boolean indicating whether the tree contains the value O(lg n)"""
        if self.root is None:
            return False
        return self.root.contains(value)
    
    def remove(self, value):
        """Remove value from the tree if it exists O(lg n)"""
        if self.root is None:
            return self.NULL_NODE
        removed = self._remove(self.root, value)
        if removed and removed.value:
            self.size -= 1
            self.root = removed
            return True
        else:
            return False
    
    def inorder(self):
        """Generator generating the tree values via. an inorder traversal O(lg n)""" 
        if self.root:
            yield from self.root.inorder()
        else:
            raise ValueError("cannot perform inorder traversal"
                             " of an empty tree")
    
    def peek_max(self):
        """Get the maximum value in the tree"""
        if self.root:
            return self.root.max().value
        raise ValueError("cannot perform peek_max on an empty tree")
    
    def peek_min(self):
        """Get the minimum value in the tree"""
        if self.root:
            return self.root.min().value
        raise ValueError("cannot perform peek_min on an empty tree")
    
    def delete_max(self):
        """Delete the maximum value in the tree"""
        max_val = self.peek_max()
        self.remove(max_val)
        return max_val
    
    def delete_min(self):
        """Delete the minimum value in the tree"""
        min_val = self.peek_min()
        self.remove(min_val)
        return min_val

    def clone(self):
        """Clone the tree"""
        if self.root:
            new_tree = AVLTree()
            new_tree.root = self.root.clone()
            new_tree.size = self.size
            return new_tree
        raise ValueError("cannot clone an empty tree")

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if node.value < value:
            inserted = self._insert(node.right, value)
            if inserted is not AVLTree.NULL_NODE:
                node.right = inserted
            else:
                return AVLTree.NULL_NODE
        elif node.value > value:
            inserted = self._insert(node.left, value)
            if inserted is not AVLTree.NULL_NODE:
                node.left = inserted
            else:
                return AVLTree.NULL_NODE
        else:
            return AVLTree.NULL_NODE
        node.update()
        return node.balance()
    
    def _remove(self, node, value):
        if not node:
            return AVLTree.NULL_NODE
        if node.value < value:
            deleted = self._remove(node.right, value)
            if deleted is not AVLTree.NULL_NODE:
                node.right = deleted
        elif node.value > value:
            deleted = self._remove(node.left, value)
            if deleted is not AVLTree.NULL_NODE:
                node.left = deleted
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # node has both a left and a right subtree
            if node.left.height > node.right.height:
                successor = node.left.max()
                node.value = successor.value
                replacement = self._remove(node.left, successor.value)
                if replacement is AVLTree.NULL_NODE:
                    return replacement
                node.left = replacement
            else:
                successor = node.right.min()
                node.value = successor.value
                replacement = self._remove(node.right, successor.value)
                if replacement is AVLTree.NULL_NODE:
                    return replacement
                node.right = replacement
        node.update()
        return node.balance()
