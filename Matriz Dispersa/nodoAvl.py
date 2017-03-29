class nodoAvl:
  """docstring for ClassName"""
  def __init__(self, nombre, descripcion, idn):
    self.nombre = nombre
    self.descripcion = descripcion
    self.idn = idn
    #super(ClassName, self).__init__()
    #self.arg = arg
    
  def toJSON(self):
    return {'nombre': self.nombre,
                 'descripcion': self.descripcion,
                 'id': self.idn}

class nodoAvlD:
  """docstring for ClassName"""
  def __init__(self, nombre, descripcion, idn,dias):
    self.nombre = nombre
    self.descripcion = descripcion
    self.idn = idn
    self.dias = dias
    #super(ClassName, self).__init__()
    #self.arg = arg
    
  def toJSON(self):
    return {'nombre': self.nombre,
                 'descripcion': self.descripcion,
                 'id': self.idn,
                 'dias': self.dias}
