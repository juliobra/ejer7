
import csv
from claseviajero import Viajero

class Manejadora:
  def __init__(self):
    self.__listaViajeros= []

  def agregarViajero(self,unViajero):
    self.__listaViajeros.append(unViajero)
  
  def canttotalmillas(self, indice):    self.__listaViajeros[indice].cantTotaldeMillas()
  
  def setacumularMillas(self, indice, millas):    self.__listaViajeros[indice].setacumularMilla(millas)
  
  def mostrarcantidadViajeros(self,ind):
   c=self.__listaViajeros[ind].cantTotaldeMillas()
   print("la cant millas es",c)

  def canjearmillas(self,ind,cantmillas):
    self.__listaViajeros[ind].canjearMillas(cantmillas)
 