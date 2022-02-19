from listas import Lista
from Menu import principal
from pilas import Pilas
from colas import Colas
import time
import os
os.system("cls")
var = principal()
lis = ["1)Listas","2)Pilas","3)Colas","4)Salir"]
opcion = ""
while opcion != "4":
    os.system("cls")
    opcion = var.menu(lis)
    if opcion == "1":
        opc1= ""
        lista = Lista()
        while opc1 != "8":
            os.system("cls")
            opc1 = var.menu (["1.agregar", "2.eliminar", "3.mostrar", "4.Eliminarla posicion" , "5.insertar", "6.buscar", "7.vaciarla lista", "8. salir"])
            if opc1 == "1":
                for x in range(4):
                    valor=input("Ingrese elementos a la lista :")
                    lista.agregar(valor)
                time.sleep(1)
            elif opc1 == "2":
                    lista.eliminar()
                    time.sleep(1)
            elif opc1 == "3":
                    lista.mostrar()
                    time.sleep(1)
            elif opc1 == "4":
                    while True:
                            indice= int(input("ingrese el valor que desee eliminar, segun su posición: "))
                            os.system("cls")        
                            a = lista.eleminarElemento(indice)
                            if a == True:
                                break
                            else:
                                print("La posicion no se encuentra")
                                time.sleep(1)
                                os.system("cls")      
            elif opc1 == "5":
                    pos=int(input("ingrese una posición: "))
                    dato = input("ingrese un nombre: ")
                    lista.InsertarElemento(pos,dato)
                    time.sleep(1)
            elif opc1 == "6":
                    while True:
                            dato=input("ingrese el valor que desee saber en que posicion esta: ")
                            os.system("cls")        
                            a = lista.buscar(dato)
                            if a == True:
                                break
                            else:
                                print("La posicion no se encuentra")
                                time.sleep(1)
                                os.system("cls")         
            elif opc1 == "7":
                    lista.clear()
                    time.sleep(1)
            elif opc1 == "8":
                    print("Usted se dirige al Menú")
                    time.sleep(2)
                    os.system("cls")
    if opcion == "2":
        opc1 = ""
        tam = int(input("ingrese el tamaño de la pila: "))        
        pila = Pilas(tam)
        while opc1 != "6":
            os.system("cls")
            opc1 = var.menu (["1)Push", "2)Pop", "3)Show", "4)Buscar" , "5)Longitud", "6)Salir"])
            if opc1 == "1":
                valor=input("Ingrese elementos a la pila: ")
                pila.push(valor)
                time.sleep(2)
            elif opc1 == "2":
                print(pila.pop())
                time.sleep(2)
            elif opc1 == "3":
                pila.show()
                time.sleep(2)
            elif opc1 == "4":
                while True:
                    buscado=input("ingrese el valor que desee saber en que posicion esta: ")
                    os.system("cls")        
                    a = pila.buscar(buscado)
                    if a == True:
                        break
                    else:
                        print("La posicion no se encuentra")
                        time.sleep(1)
                        os.system("cls") 
                time.sleep(1)
            elif opc1 == "5":
                pila.longitud()
                time.sleep(1)
            elif opc1 == "6":
                    print("Usted se dirige al Menú")
                    time.sleep(2)
                    os.system("cls")
    if opcion == "3":
        opc1 = ""
        tam = int(input("ingrese el tamaño de la cola: "))        
        cola = Colas(tam)
        while opc1 != "6":
            os.system("cls")
            opc1 = var.menu (["1)Push", "2)Pop", "3)Show", "4)Buscar" , "5)Longitud", "6)Salir"])
            if opc1 == "1":
                valor=input("Ingrese elementos a la cola: ")
                cola.push(valor)
                time.sleep(2)
            elif opc1 == "2":
                print(cola.pop())
                time.sleep(2)
            elif opc1 == "3":
                cola.show()
                time.sleep(2)
            elif opc1 == "4":
                while True:
                    buscado=input("ingrese el valor que desee saber en que posicion esta: ")
                    os.system("cls")        
                    a = cola.buscar(buscado)
                    if a == True:
                        break
                    else:
                        print("La posicion no se encuentra")
                        time.sleep(1)
                        os.system("cls") 
                time.sleep(1)
            elif opc1 == "5":
                cola.longitud()
                time.sleep(1)
            elif opc1 == "6":
                    print("Usted se dirige al de Menú")
                    time.sleep(1)
                    os.system("cls")
    if opcion == "4":
           os.system("cls")
print("Gracias por entrar en el sistema....")
time.sleep(2)