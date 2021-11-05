from timeit import default_timer as timer
class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def findIterative(root, data):
    '''
    Method to find data in BST
    Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode:
        if data == currentNode.data:
            return 'El numero encontrado es:',currentNode.data
        elif data < currentNode.data:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return 'No se encontro el numero', data

def insertNode(root, node):
    '''
    Insert a node in BST
    '''
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def buildBSTFromArray(list):
    '''
    Build Binary Search Tree
    from Array
    :return:
    '''
    root = None
 
    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root

'''
///////////////////////////
obteniendo el archivo txt
////////////////////////////
'''
f= open('bst.txt','r')
mensaje= f.read()

'''
///////////////////////////
Combirtiendo del archivo txt de string a entero
////////////////////////////
'''
b = [int(x) for x in mensaje.split()]

'''
///////////////////////////
Colocamos en una variable al metedo buildBSTFromArray()
////////////////////////////
'''
v = buildBSTFromArray(b)

'''
///////////////////////////
Calculamos el tiempo de busqueda de tres datos
////////////////////////////
'''
start = timer()
dato=findIterative(v, 9353)
print(dato)
dato2=findIterative(v, 9453)
print(dato2)
dato3=findIterative(v, 9001)
print(dato3)
end =timer()
delay= end-start
print("> time {} ". format(delay))

'''
///////////////////////////
Se realiza la impresion del arbol
////////////////////////////
'''
import tree as t
t.printLevelOrder(v)

