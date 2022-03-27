class Control:
  def __init__(self):
    self.tv
  
  def setTv(nTv):
    self.tv = nTv
  
  def turnOn(self):
    self.tv.turnOn()
  
  def turnOff(self):
    self.tv.turnOff()
  
  def canalUp(self):
    self.tv.canalUp()

  def canalDown(self):
    self.tv.canalDown()
  
  def volumenUp(self):
    self.tv.volumenUp()
  
  def volumenDown(self):
    self.tv.volumenDown()
  
  def setCanal(self, nCanal):
    if (self.tv.getEstado() and nCanal >= 1 and nCanal <= 120):
      self.tv.canal = nCanal
  
  def enlazar(self, eTv):
    self.tv = eTv
    eTv.setControl(self)