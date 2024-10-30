class Nodotree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.leaves = 0

    def insert(self, value):
        if self.root is None:
            self.leaves += 1
            self.root = Nodotree(value)
        else:
            self.insertLeaf(value, self.root)

    def insertLeaf(self, value, root):
        if value < root.value:
            if root.left is None:
                self.leaves += 1
                root.left = Nodotree(value)
            else:
                self.insertLeaf(value, root.left)
        elif value > root.value:
            if root.right is None:
                self.leaves += 1
                root.right = Nodotree(value)
            else:
                self.insertLeaf(value, root.right)

    def search(self, value, root=None, count=0):
        if self.leaves > count:
            if root is None:
                root = self.root
            if root.value == value:
                return root
            elif value < root.value:
                return self.search(value, root.left, count = count+1)
            elif value > root.value:
                return self.search(value, root.right, count = count+1)
        else:
            False

    def searchFather(self, value, root=None, count=0):
        if self.leaves > count:
            if root is None:
                root = self.root
            if root.left and root.left.value == value:
                return root
            elif root.right and root.right.value == value:
                return root
            elif value < root.value:
                return self.searchFather(value, root.left, count = count+1)
            elif value > root.value:
                return self.searchFather(value, root.right, count = count+1)
        else:
            False

    def delete(self, value, root=None):
        if self.searchFather(value):
            father = self.searchFather(value)
            if father.right.value == value:
                print(father.right.value)
                father.right.value == None
            elif father.left.value == value:
                print(father.left.value)
                father.left.value == None  
        else:
            self.root = None

    def path(self, tipo_caminhamento="infixLeft"):
        if tipo_caminhamento == "infixLeft":
            self.infixLeft(self.root)
        elif tipo_caminhamento == "preFixLeft":
            self.preFixLeft(self.root)
        elif tipo_caminhamento == "posFixLeft":
            self.posFixLeft(self.root)
        elif tipo_caminhamento == "infixRight":
            self.infixRight(self.root)
        elif tipo_caminhamento == "preFixRight":
            self.preFixRight(self.root)
        elif tipo_caminhamento == "posFixRight":
            self.posFixRight(self.root)

    def infixLeft(self, root):
        if root is not None:
            self.infixLeft(root.left)
            print(root.value, end=" ")
            self.infixLeft(root.right)

    def preFixLeft(self, root):
        if root is not None:
            print(root.value, end=" ")
            self.preFixLeft(root.left)
            self.preFixLeft(root.right)

    def posFixLeft(self, root):
        if root is not None:
            self.posFixLeft(root.left)
            self.posFixLeft(root.right)
            print(root.value, end=" ")

    def infixRight(self, root):
        if root is not None:
            self.infixRight(root.right)
            print(root.value, end=" ")
            self.infixRight(root.left)

    def preFixRight(self, root):
        if root is not None:
            print(root.value, end=" ")
            self.preFixRight(root.right)
            self.preFixRight(root.left)

    def posFixRight(self, root):
        if root is not None:
            self.posFixRight(root.right)
            self.posFixRight(root.left)
            print(root.value, end=" ")

tree = BinaryTree()
    
tree.insert(50)
tree.insert(10)
tree.insert(30)
tree.insert(60)
tree.insert(20)
    
print("Caminho infixado a esquerda:")
tree.path("infixLeft")
    
print("\nCaminho pré-fixado a esquerda:")
tree.path("preFixLeft")
    
print("\nCaminho pós-fixado a esquerda:")
tree.path("posFixLeft")

print("\nCaminho infixado a direita:")
tree.path("infixRight")
    
print("\nCaminho pré-fixado a direita:")
tree.path("preFixRight")
    
print("\nCaminho pós-fixado a direita:")
tree.path("posFixRight")
    
print("\nBusca:", tree.search(2))   

print("\nBusca pai:", tree.searchFather(60).value)    

tree.delete(60)

print("\nCaminho pós-fixado a direita:")
tree.path("posFixRight")