from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models import *
	
manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

@manager.command
def add_data_tables():
    db.create_all()

    Inv_equipos = ("redes","seguridad electronica",)

    for inv in Inv_equipos:
    	inv_equipos=Inv_equipos(nombre=inv)
    	db.session.add(inv_equipos)
    	db.session.commit()

    equipos=[
    {"nombre":"switch","descripcion":"equipo de 48 ports 100/1000 base ","CategoriaId":1},
    {"nombre":"switch catalist","descripcion":"equipo de 24 ports","CategoriaId":1},
    {"nombre":"acces point","descripcion":"8 ports","CategoriaId":2},
    
    ]
    for equi in equipos:
       	equipos=Catalogos(**equi)
       	db.session.add(equipos)
       	db.session.commit()

	
if __name__ == '__main__':
	manager.run()