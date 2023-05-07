main
import csv
from claseviajero import Viajero
from clasemanejadora import Manejadora

def TestViajeros(lista):
    archivo = open('viajero.csv')
    reader = csv.reader(archivo, delimiter =',')
    for fila in reader:
      numV= int(fila[0])
      dni= fila[1]
      nom= fila[2]
      apell= fila[3]
      millasAcum= int(fila[4])
      unViajero= Viajero(numV,dni,nom,apell,millasAcum)
      lista.agregarViajero(unViajero)
      print("numero viajero: {}, dni: {},nombre: {},apellido{}, millas acumuladas:  {}\n".format(numV,dni,nom,apell,millasAcum))

      
def opcion0(lista,i):
  print("adios")

def opcion1(lista,i):
  print("cantidad de millas {}".format(lista.mostrarcantidadViajeros(i)))

def opcion2(lista,i):
  print("ingrese las millas a acumular")
  m=int(input(""))
  lista.setacumularMillas(i,m)
  print("la cantidad de millas acumuladas es {}".format(lista.canttotalmillas(i)))

def opcion3(lista,i):
  print("ingrese la cantidad de millas a cambiar")
  millas=int(input(""))
  lista.canjearmillas(i,millas)

switcher = {
  0:opcion0,
  1:opcion1,
  2:opcion2,
  3:opcion3
}
  
def switch (op, lista, indice):
  func= switcher.get (op, lambda: print("opcion incorrecta"))
  func(lista,indice)


if __name__=='__main__':
  listaV= Manejadora()
  TestViajeros(listaV)
  print(listaV)
  bandera= False
  numV=int(input("Ingrese un numero de viajero frecuente"))
  while not bandera:
    print("\nMENU DE OPCIONES:\n")
    print("0: Salir\n")
    print("1: Consultar cantidad de millas\n")
    print("2: Acumular millas\n")
    print("3: Canjer Millas\n")
    opcion= int(input("Ingrese una opcion\n"))
    switch(opcion,listaV,numV)
    bandera = int(opcion)==0   

v = Viajero("123", 2000)
print(v == 2000)  
print(3000 == v) 
v = Viajero("123", 2000)
v = 100 + v
print(v.millas) 
v = Viajero("123", 2000)
v = 100 - v
print(v.millas)  