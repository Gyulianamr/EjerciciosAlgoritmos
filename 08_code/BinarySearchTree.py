# Implement binary search trees using Tree and Node classes
# Nodes contain a key and some data

from LinkStack import *

class BinarySearchTree(object):  # A binary search tree class

# To preserve node integrity, node keys and children links should
# not be accessible from the caller, so we make the entire
# Node class hidden, but leave its attributes public for ease
# of manipulating them in the Tree class

   class __Node(object):         # A node in a binary search tree
      def __init__(              # Constructor takes a key that is
            self,                # used to determine the position
            key,                 # inside the search tree,
            data,                # the data associated with the key
            left=None,           # and a left and right child node
            right=None,
            ):         # if known
         self.key  = key         # Copy parameters to instance
         self.data = data        # attributes of the object
         self.leftChild = left
         self.rightChild = right

      def __str__(self):         # Represent a node as a string 
         return "{" + str(self.key) + ", " + str(self.data) + "}"

   def __init__(self):        # The tree organizes nodes by their
      self.__root = None      # keys.  Initially, it is empty.
   
   def isEmpty(self):         # Check for empty tree
      return self.__root is None

   def root(self):            # Get the data and key of the root node
      if self.isEmpty():      # If the tree is empty, raise exception
         raise Exception("No root node in empty tree")
      return (                # Otherwise return root data and its key
         self.__root.data, self.__root.key)
   #
   def __find(self, goal, find_shallow=False):
    """Busca un nodo con una clave igual a 'goal' en el árbol.
    Si 'find_shallow' es True, devuelve la coincidencia más superficial.
    Si 'find_shallow' es False, devuelve la coincidencia más profunda.
    También devuelve el padre del nodo encontrado.
    """
    current = self.__root  # Comienza la búsqueda desde la raíz del árbol.
    parent = self          # El nodo padre inicial es la propia clase (en caso de estar vacía).
    last_match = None      # Rastrea el último nodo que coincide con la clave.
    last_match_parent = None  # Guarda el padre del último nodo coincidente.

    while current:  # Recorre el árbol hasta que no haya más nodos.
        if goal == current.key:  # Si la clave coincide con el nodo actual:
            last_match = current       # Actualiza el último nodo coincidente.
            last_match_parent = parent # Actualiza su padre.
            if find_shallow:           # Si buscamos el más superficial:
                return last_match, last_match_parent  # Devuelve inmediatamente.

        # Actualiza el padre y avanza hacia el siguiente nodo según la clave buscada.
        parent = current
        if goal < current.key:  # Si la clave buscada es menor, avanza hacia la izquierda.
            current = current.leftChild
        else:                   # Si la clave buscada es mayor o igual, avanza hacia la derecha.
            current = current.rightChild

    # Si no hay coincidencias, devuelve None junto con el último padre visitado.
    # Si hay coincidencias, devuelve la más profunda encontrada.
    return (last_match, last_match_parent) if last_match else (None, parent)


   def search(self, key, find_shallow=False):
    """
    Busca un nodo en el árbol que contenga la clave especificada y devuelve su dato asociado.
    De forma predeterminada, devuelve el dato del nodo más profundo entre los nodos con la misma clave.
    Si 'find_shallow' es True, devuelve el dato del nodo más superficial.
    """
    # Llama a la función interna __find para localizar el nodo con la clave especificada.
    # Devuelve el nodo más profundo por defecto, o el más superficial si find_shallow=True.
    node, _ = self.__find(key, find_shallow=find_shallow)
    # Si se encuentra un nodo, devuelve su atributo 'data'.
    # Si no existe ningún nodo con la clave, devuelve None.
    return node.data if node else None


#

   def insert(self, key, data):
      # Encuentra el nodo y su padre
      node, parent = self.__find(key)  #busca si existe un nodo con esa clave
      new_node = self.__Node(key, data)

      if not node:  # Si no existe un nodo con esta clave
         if parent is self: 
               self.__root = new_node  # Inserta como la raíz si el árbol está vacío
         elif key < parent.key:
               parent.leftChild = new_node
         else:
               parent.rightChild = new_node
      else:  # Maneja el caso de duplicados
         # Encuentra el nodo duplicado más profundo y añade el nuevo nodo como hijo izquierdo
         while node.leftChild:          #Mientras el nodo tenga un hijo izquierdo, 
               node = node.leftChild    #baja al hijo izquierdo para encontrar el duplicado más profundo.
         node.leftChild = new_node

      return True




   def inOrderTraverse(       # Visit all nodes of the tree in-order
         self, function=print): # and apply a function to each node
      self.__inOrderTraverse( # Call recursive version starting at
         self.__root, function=function) # root node

   def __inOrderTraverse(     # Visit a subtree in-order, recursively
         self, node, function): # The subtree's root is node
      if node:                # Check that this is real subtree
         self.__inOrderTraverse( # Traverse the left subtree
            node.leftChild, function)
         function(node)       # Visit this node
         self.__inOrderTraverse( # Traverse the right subtree
            node.rightChild, function)

   def traverse_rec(self,         # Traverse the tree recursively in
                traverseType="in"): # pre, in, or post order
      if traverseType in [    # Verify type is an accepted value and
            'pre', 'in', 'post']: # use generator to walk the tree 
         return self.__traverse(  # yielding (key, data) pairs
            self.__root, traverseType) # starting at root
      
      raise ValueError("Unknown traversal type: " + str(traverseType))

   def __traverse(self,       # Recursive generator to traverse
                  node,       # subtree rooted at node in pre, in, or
                  traverseType): # post order
      if node is None:        # If subtree is empty, 
         return               # traversal is done
      if traverseType == "pre": # For pre-order, yield the current
         yield (node.key, node.data) # node before all the others
      for childKey, childData in self.__traverse( # Recursively
            node.leftChild, traverseType): # traverse the left subtree
         yield (childKey, childData)       # yielding its nodes
      if traverseType == "in": # If in-order, now yield the current
         yield (node.key, node.data) # node
      for childKey, childData in self.__traverse( # Recursively
            node.rightChild, traverseType): # traverse right subtree
         yield (childKey, childData)        # yielding its nodes
      if traverseType == "post": # If post-order, yield the current
         yield (node.key, node.data) # node after all the others

   def traverse(self,         # Non-recursive generator to traverse
                traverseType='in'): # tree in pre, in, or post order
      if traverseType not in [ # Verify traversal type is an
            'pre', 'in', 'post']: # accepted value
         raise ValueError(
            "Unknown traversal type: " + str(traverseType))
      
      stack = Stack()         # Create a stack
      stack.push(self.__root) # Put root node in stack
      
      while not stack.isEmpty(): # While there is work in the stack
         item = stack.pop() # Get next item
         if isinstance(item, self.__Node): # If it's a tree node
            if traverseType == 'post': # For post-order, put it last
               stack.push((item.key, item.data))
            stack.push(item.rightChild) # Traverse right child
            if traverseType == 'in': # For pre-order, put item 2nd
               stack.push((item.key, item.data))
            stack.push(item.leftChild) # Traverse left child
            if traverseType == 'pre': # For pre-order, put item 1st
               stack.push((item.key, item.data))
         elif item:           # Every other non-None item is a
            yield item        # (key, value) pair to be yielded

   def minNode(self):         # Find and return node with minimum key
      if self.isEmpty():      # If the tree is empty, raise exception
         raise Exception("No minimum node in empty tree")
      node = self.__root      # Start at root
      while node.leftChild:   # While node has a left child,
         node = node.leftChild # follow left child reference
      return (node.key, node.data) # return final node key and data

   def maxNode(self):         # Find and return node with maximum key
      if self.isEmpty():      # If the tree is empty, raise exception
         raise Exception("No maximum node in empty tree")
      node = self.__root      # Start at root
      while node.rightChild:  # While node has a right child,
         node = node.rightChild # follow right child reference
      return (node.key, node.data) # return final node key and data
         
   def levels(self):          # Count the levels in the tree
      return self.__levels(self.__root) # Count starting at root
   
   def __levels(self, node):  # Recursively count levels in subtree
      if node:                # If a node is provided, then level is 1
         return 1 + max(self.__levels(node.leftChild),  # more than
                        self.__levels(node.rightChild)) # max child
      else: return 0          # Empty subtree has no levels

   def nodes(self):           # Count the tree nodes, using iterator
      count = 0               # Assume an empty tree
      for key, data in self.traverse(): # Iterate over all keys in any
         count += 1           # order and increment count
      return count

   def nodes_rec(self):       # Count the tree nodes, recursively
      return self.__nodes(self.__root) # Count starting at root
   
   def __nodes(self, node):   # Recursively count nodes in subtree
      if node:                # If a node is provided, then sum the
         return (1 + self.__nodes(node.leftChild) +  # node with those
                 self.__nodes(node.rightChild))      # of its children
      else: return 0          # Empty subtree has no nodes

   def print(self,            # Print the tree sideways with 1 node
             indentBy=4):     # on each line and indenting each level
      self.__pTree(self.__root, # by some blanks.  Start at root node
                   "ROOT:   ", "", indentBy) # with no indent
       
   def __pTree(self,          # Recursively print a subtree, sideways 
               node,          # with the root node left justified
               nodeType,      # nodeType shows the relation to its
               indent,        # parent and the indent shows its level
               indentBy=4):   # Increase indent level for subtrees
      if node:                # Only print if there is a node
         self.__pTree(node.rightChild, "RIGHT:  ", # Print the right
                      indent + " " * indentBy, indentBy) # subtree
         print(indent + nodeType, node) # Print this node
         self.__pTree(node.leftChild,  "LEFT:   ", # Print the left
                      indent + " " * indentBy, indentBy) # subtree
#
   def delete(self, goal):
    """
    Elimina el nodo más profundo con la clave especificada. Si hay claves duplicadas,
    se prioriza eliminar la más reciente (LIFO).
    """
    # Encuentra el nodo más profundo con la clave y su padre.
    node, parent = self.__find(goal, find_shallow=False)  # Siempre busca el más profundo.
    if node is not None:  
        # Si el nodo fue encontrado, llama a __delete para realizar la eliminación.
        return self.__delete(parent, node)
    return None  # Si no se encontró, retorna None.

   def __delete(self, parent, node):
    """
    Realiza la eliminación física de un nodo en el árbol y ajusta las conexiones necesarias.

    """
    # Guarda los datos del nodo que se van a eliminar.
    deleted = node.data  

    if node.leftChild:  # Si el nodo tiene un hijo izquierdo.
        if node.rightChild:  # Si el nodo tiene ambos hijos.
            self.__promote_successor(node)  # Promociona al sucesor.
        else:  # Si solo tiene hijo izquierdo.
            if parent is self:  # Si el nodo a eliminar es la raíz.
                self.__root = node.leftChild  # Actualiza la raíz.
            elif parent.leftChild is node:  # Si el nodo es hijo izquierdo.
                parent.leftChild = node.leftChild  # Actualiza el hijo izquierdo.
            else:  # Si el nodo es hijo derecho.
                parent.rightChild = node.leftChild  # Actualiza el hijo derecho.
    else:  # Si el nodo no tiene hijo izquierdo.
        if parent is self:  # Si el nodo a eliminar es la raíz.
            self.__root = node.rightChild  # Actualiza la raíz.
        elif parent.leftChild is node:  # Si el nodo es hijo izquierdo.
            parent.leftChild = node.rightChild  # Actualiza el hijo izquierdo.
        else:  # Si el nodo es hijo derecho.
            parent.rightChild = node.rightChild  # Actualiza el hijo derecho.

    return deleted  # Retorna los datos del nodo eliminado.




   def __promote_successor( # When deleting a node with both subtrees,
         self,              # find successor on the right subtree, put
                            # its data in this node, and delete the
         node):             # successor from the right subtree
      successor = node.rightChild # Start search for successor in
      parent = node         # right subtree and track its parent
      while successor.leftChild: # Descend left child links until
         parent = successor # no more left links, tracking parent
         successor = successor.leftChild
      node.key = successor.key    # Replace node to delete with
      node.data = successor.data  # successor's key and data
      self.__delete(parent, successor) # Remove successor node




