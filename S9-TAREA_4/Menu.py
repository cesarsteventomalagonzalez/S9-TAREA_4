import os
os.system("cls")
class principal:
    def _init_(self):
        pass
    def menu(self,opciones):
        print("►"*7,"MENÚ","◄"*7)
        for opcion in opciones: 
            print(opcion)
        opc = input("Elija opcion[1...{}] : " .format(len(opciones)))
        return opc