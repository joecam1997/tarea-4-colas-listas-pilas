class Pila: 
    def __init__(self,tamaño):
        self.lista=[]
        self.tope=0
        self.tamaño=tamaño
    def empty(self):
        #if self.tope==0:
        #     return True
        #else:
        #    return False
        
        return self.tope == 0
    def push(self,dato):
        if self. tope < self. tamaño:
            self. lista += [dato]
            self. tope += 1 
        else:
            print("La Lista está Llena")    
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self. lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return  top
            
    def longitud(self):
        return self.tope
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else: 
             for ele in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        
        return "Retorna la posicion del valor buscado"
    
    
pila = Pila(5)
pila.push("4")       
pila.push("3")       
pila. push("2")       
pila. push("5")       
pila. push("20")       
pila.push("10")   
pila. show ()    
print(pila. pop())
print(pila. pop())
print(pila. pop())
print(pila. pop())
print(pila. pop())
print(pila. pop())