import sqlalchemy as db
import pandas as pd
import os
#test
os.chdir("..")
engine = db.create_engine('sqlite:///API/DBServers.sqlite') #Create DBServers.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

#CONSTRUYO LA TABLA SERVERS
serversTab = db.Table('servers', metadata,
              db.Column('id_serv', db.Integer, primary_key = True, autoincrement= True),
              db.Column('ipaddress', db.String(20)),
              db.Column('fecha_hora', db.DateTime()),
              db.Column('arquitectura_proc', db.String(6)),
              db.Column('marca_proc', db.String(50)),
              db.Column('nombre_so', db.String(20)),
              db.Column('version_so', db.String(50))
              )

#CONSTRUYO LA TABLA PROCESOS              
procesosTab = db.Table('procesos', metadata,
                db.Column('id_proc', db.Integer, primary_key = True, autoincrement= True),
                db.Column('id_serv', db.Integer, db.ForeignKey("servers.id_serv", onupdate='CASCADE'), nullable= False),
				db.Column('ip_server', db.String(20)),
				db.Column('fecha_hora', db.DateTime()),
				db.Column('pid', db.Integer()),
				db.Column('name', db.String(30)),
				db.Column('username', db.String(30))
				)

#CONSTRUYO LA TABLA USUARIOS_ACTIVOS
usersTab = db.Table('usuarios_activos', metadata,
            db.Column('id_usr', db.Integer, primary_key = True, autoincrement= True),
            db.Column('id_serv', db.Integer, db.ForeignKey("servers.id_serv", onupdate='CASCADE'),nullable= False),
			db.Column('ip_server', db.String(20)),
			db.Column('fecha_hora', db.DateTime()),
			db.Column('username', db.String(30)),
			db.Column('pid', db.Integer())
			)

metadata.create_all(engine) #Creates the table
