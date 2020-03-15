class ListaEncadeada:
  class Node:
    def __init__(self,elemento,nxt):
      self.elemento = elemento
      self.nxt = nxt
  def __init__(self):
    self.head = None
    self.size = 0

  def inserir(self,elemento,pos):
    newNode = self.Node(elemento,None)
    if (pos == 0):
      newNode.nxt = self.head
      self.head = newNode
    else:
      corredor = self.head
      i = 1
      while i < pos:
        corredor = corredor.nxt  
        i+=1
      newNode.nxt = corredor.nxt
      corredor.nxt = newNode
    self.size += 1
  def __str__(self):
    to_print = []
    pivot = self.head
    while pivot is not None:
      to_print.append(pivot.elemento)
      pivot = pivot.nxt
    return str(to_print)
  def remover(self,pos):
    if pos == 0:
      self.head = self.head.nxt
    else:
      corredor = self.head
      i = 1
      while i < pos:
         corredor = corredor.nxt
         i+=1
      corredor.nxt = corredor.nxt.nxt
    self.size -= 1

lista = ListaEncadeada()
lista.inserir(1, 0)
lista.inserir(2, 0)
lista.inserir(3, 0)
lista.inserir(4, 0)
lista.inserir(10, 4)
print(lista)


      
