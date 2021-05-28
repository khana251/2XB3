class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return self == self.parent.right

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        if not self.parent == None:
            return self.parent.get_brother()
        return None

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        l = self.left
        if not l.right == None:
            self.left = l.right
        else:
            self.left = None
        l.right = self
        l.colour = self.colour
        self.colour = "R"
        if not self.parent == None:
            l.parent = self.parent
            if self.is_right_child():
                self.parent.right = l
            elif self.is_left_child():
                self.parent.left = l
        else:
            l.parent = None
        self.parent = l
        
    def rotate_left(self):
        r = self.right
        if not r.left == None:
            self.right = r.left
        else:
            self.right = None
        r.left = self 
        r.colour = self.colour
        self.colour = "R"
        if not self.parent == None:
            r.parent = self.parent
            if self.is_right_child():
                self.parent.right = r
            elif self.is_left_child():
                self.parent.left = r
        else:
            r.parent = None
        self.parent = r
        
class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
        # elif value > node.value:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        elif node.parent.is_red() and node.is_red():
            if not node.get_uncle() == None and not node.uncle_is_black():
                node.parent.colour = "B"
                node.get_uncle().colour = "B"
                node.parent.parent.colour="R"
            elif not node == None:
                if node.is_left_child():
                    if node.parent.is_left_child() and not node.parent.parent == None:
                        node.parent.parent.rotate_right()

                    elif node.parent.is_right_child():
                        node.parent.rotate_right()
                        node.parent.rotate_left()

                elif node.is_right_child():
                    if node.parent.is_left_child():
                        node.parent.rotate_left()
                        node.parent.rotate_right()

                    elif (node.parent.is_right_child() and not node.parent.parent == None):
                        node.parent.parent.rotate_left()

                self.find_root()
        self.root.make_black()
        if not node.parent == None:
            self.fix(node.parent)
        
    def find_root(self):
        while not self.root.parent == None:
            self.root = self.root.parent
            
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
class BST:

    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        # else:
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
                node.right.parent = node
            else:
                self.__insert(node.right, value)
    

