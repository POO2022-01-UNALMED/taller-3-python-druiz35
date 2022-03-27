
class TV:
  _numTV = 0
  def __init__(self, marca, estado):
    self.marca = marca
    self.canal = 1
    self.precio = 500
    self.estado = estado
    self.volumen = 1
    self.control = None
    TV._numTV += 1
  
  def getMarca(self):
    return self.marca

  def getCanal(self):
    return self.canal

  def getPrecio(self):
    return self.precio

  def getVolumen(self):
    return self.volumen

  def getControl(self):
    return self.control
  
  def setMarca(self, nMarca):
    self.marca = nMarca
  
  def setCanal(self, nCanal):
    if (nCanal >= 1 and nCanal <= 120):
      self.canal = nCanal
  
  def setPrecio(self, nPrecio):
    self.precio = nPrecio
  
  def setVolumen(self, nVolumen):
    if (nVolumen >= 0 and nVolumen <= 7):
      self.volumen = nVolumen
  
  def setControl(self, nControl):
    self.control = nControl
  
  def getNumTV(self):
    return TV._numTV
  
  @classmethod
  def setNumTV(cls, nNumTV):
    cls._numTV = nNumTV
  
  def turnOn(self):
    self.estado = True
  
  def turnOff(self):
    self.estado = False
  
  def getEstado(self):
    return self.estado
  
  def canalUp(self):
    if (self.estado and self.canal < 121):
      self.canal += 1
  
  def canalDown(self):
    if (self.estado and self.canal > 1):
      self.canal -= 1
  
  def volumenUp(self):
    if (self.estado and self.volumen < 7):
      self.volumen += 1
  
  def volumenDown(self):
    if (self.estado and self.volumen > 0):
      self.volumen -= 1