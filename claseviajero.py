class Viajero:
  def __init__(self,numV,dni,nom,apell,millasAcum):
    self.__numV= numV
    self.__dni= dni
    self.__nom= nom
    self.__apell= apell
    self.__millasAcum= millasAcum

  def __str__(self):
    return "%d, %s, %s, %s, %d" % (self.__numV, self.__dni, self.__nom, self.__apell, self.__millasAcum)

  def getNumV(self):
    return self.__numV

  def getDni(self):
    return self.__dni

  def getNom(self):
    return self.__apell

  def getMillasA(self):
    return self.__millasAcum

  def setacumularMilla(self,M):
    self.__millasAcum += M
    
  def cantTotaldeMillas(self):
    return self.__millasAcum

 

  def canjearMillas(self,cantmillas):
    if (cantmillas<=self.__millasAcum):
      self.__millasAcum -= cantmillas
      print("millas canjeadas")
      print("millas despues del canje ",self.__millasAcum)
    else:
      print("la cantidad de millas es inferior a las millas acumuladas")
   
  def __gt__(self, otro):
     return self.__millasAcum > otro.__millasAcum

  def __add__(self, otro):
    nueva_cantidad_millas = self.__millasAcum + otro.__millasAcum
nuevo_viajero = Viajero(self.__numV, self.__dni, self.__nom, self.__apell, nueva_cantidad_millas)
      return nuevo_viajero


def __eq__(self, other):
        if isinstance(other, int):
            return self.millas == other
        elif isinstance(other, ViajeroFrecuente):
            return self.millas == other.millas
        else:
            return NotImplemented
        
    # Sobrecarga de operador de suma (+ o __add__)
    def __add__(self, other):
        if isinstance(other, int):
            return ViajeroFrecuente(self.num, self.millas + other)
        elif isinstance(other, ViajeroFrecuente):
            return ViajeroFrecuente(self.num, self.millas + other.millas)
        else:
            return NotImplemented
    
    # Sobrecarga de operador de resta (- o __sub__)
    def __sub__(self, other):
        if isinstance(other, int):
            return ViajeroFrecuente(self.num, self.millas - other)
        elif isinstance(other, ViajeroFrecuente):
            return ViajeroFrecuente(self.num, self.millas - other.millas)
        else:
            return NotImplemented
    
    # Sobrecarga de operador de suma por derecha (+= o __iadd__)
    def __radd__(self, other):
        return self + other
    
    # Sobrecarga de operador de resta por derecha (-= o __isub__)
    def __rsub__(self, other):
        return self - other