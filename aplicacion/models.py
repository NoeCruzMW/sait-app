from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from aplicacion.app import db

class Inv_equipos(db.Model):
	"""inventario de los equipos"""
	__tablename__ = 'inv_equipos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100))
	catalogos = relationship("catalogos", backref="inv_equipos",lazy='dynamic')


	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Catalogos(db.Model):
	"""equipos de la empresa"""
	__tablename__ = 'catalogos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100),nullable=False)
	descripcion = Column(String(255))
	image = Column(String(255))
	Inv_equiposId=Column(Integer,ForeignKey('inv_equipos.id'), nullable=False)
	inv_equipos = relationship("Inv_equipos", backref="catalogos")



	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
