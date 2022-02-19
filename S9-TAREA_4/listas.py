import time
class Lista:
    def __init__(self,datos=[]):
       self.datos = []

    def agregar(self,dato):
        self.datos.append(dato)
        print(f'Se agregaron nuevos elementos : {self.datos}\n')
        
    def eliminar(self):
        dato = self.datos.pop()
        print(f'Se elimino un numero de la lista: {self.datos}\n')
    
    def clear(self):
        dato = self.datos.clear()
        print(f'Se elimino la lista: {self.datos}\n')
     
    def eleminarElemento(self,indice):
        try:
            if indice <= len(self.datos):
                print("el elemento se encuentra: {}".format(self.datos.pop(indice)))
                time.sleep(1)
                return True
        except ValueError:
            return False
    
    def InsertarElemento(self,pos,dato):
        self.datos.insert(pos,dato)
        print(f'Se agrego un nombre a la lista : {self.datos}\n')

    def buscar(self,dato):
        try:
            if dato in self.datos:
                print("el elemento se encuentra: {}".format(self.datos.index(dato)))
                time.sleep(1)
                return True
        except ValueError:
            return False
    
    def mostrar(self):
         print(f'Aqui se muestra como esta actualmente la lista: {self.datos}\n')





