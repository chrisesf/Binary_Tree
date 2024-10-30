class NodoArvore:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def insertRoot(self, value):
        if self.raiz is None:
            self.raiz = NodoArvore(value)
        else:
            self.insertLeaf(value, self.raiz)

    def insertLeaf(self, value, root):
        if value < root.value:
            if root.left is None:
                root.left = NodoArvore(value)
            else:
                self.insertLeaf(value, root.left)
        elif value > root.value:
            if root.right is None:
                root.right = NodoArvore(value)
            else:
                self.insertLeaf(value, root.right)

    def search(self, value, root=None):
        if root is None:
            root = self.raiz
        if root.value == value:
            return root
        elif value < root.value:
            return self.search(value, root.left)
        else:
            return self.search(value, root.right)

    def path(self, tipo_caminhamento="central"):
        if tipo_caminhamento == "central":
            self.center(self.raiz)
        elif tipo_caminhamento == "pre":
            self.pre_fixed(self.raiz)
        elif tipo_caminhamento == "pos":
            self.pos_fixed(self.raiz)
        else:
            print("Tipo de caminhamento inválido")

    def center(self, root):
        if root is not None:
            self.center(root.left)
            print(root.value, end=" ")
            self.center(root.right)

    def pre_fixed(self, root):
        if root is not None:
            print(root.value, end=" ")
            self.pre_fixed(root.left)
            self.pre_fixed(root.right)

    def pos_fixed(self, root):
        if root is not None:
            self.pos_fixed(root.left)
            self.pos_fixed(root.right)
            print(root.value, end=" ")

arvore = ArvoreBinaria()
    
arvore.insertRoot(50)
arvore.insertRoot(10)
arvore.insertRoot(60)
arvore.insertRoot(20)
    
print("Caminhamento central:")
arvore.path("central")
    
print("\nCaminhamento pré-fixado:")
arvore.path("pre")
    
print("\nCaminhamento pós-fixado:")
arvore.path("pos")
    
print("\nBusca:")
print(arvore.search(20).value)
    
    