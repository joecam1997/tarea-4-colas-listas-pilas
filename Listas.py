class Lista:
    def __init__(self,datos=[]):
      self.lista = datos
        
    def push(self,dato):
      self.lista. append(dato)
        
    def pop(self):
        dato = self.lista.pop()
        
        return dato
    
    def eleminarElemento(self,pos):
        if pos < 0 or  pos >= len(self. lista):
           
           
           return None 
         
        else: 
            
            
              self.lista = self.lista[0:pos] + self.lista[pos+1:]
            
    
    def InsertarElemento(self,pos):
        pass
    
    def buscar(self,pos,buscado):
        pass
    
    def mostrar(self):
        pass

        
numeros = Lista()
numeros. push("Daniel")
numeros. push("Yady")
numeros. push("Ana")
numeros. push("José")
numeros. push("Moisés")
# ["Daniel","Jose","Yady","Ana"]    "miguel" 
#      0      1      2    len = 3
#            pos
numeros. eleminarElemento(1)
#print(numeros.pop())
#print(numeros.pop())
print(numeros. lista)