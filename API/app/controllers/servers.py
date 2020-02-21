from flask import Blueprint
from flask import request
from flask import Response
import json
from datetime import date
import sqlalchemy as db
from datetime import datetime

bp = Blueprint("images", __name__)
mime_type = 'application/json'

servers = []

@bp.route("/", methods=['POST'])
def create_new_server():
	try:
	#print(request.json)
		content_to_json = request.json
		
		new_server={	
			"arquitectura_proc":content_to_json['arquitectura_proc'],
			"marca_proc":content_to_json['marca_proc'],
			"nombre_so":content_to_json['nombre_so'],
			"version_so":content_to_json['version_so'],
			"ipaddress":content_to_json['ipaddress'],
			"procesos":content_to_json['procesos'],
			"usuarios_activos":content_to_json['usuarios_activos'],
			"fecha_hora": content_to_json['fecha_hora']
		}

		#servers.append(new_server)
		today = str(date.today())
		#print(today) 

		archivo=str(new_server['ipaddress'])+"_"+today+".txt"
		f=open(archivo,"w+")
		f.write(json.dumps(new_server, indent=3))
		f.close()

		print (json.dumps(new_server, indent=3))
		#print (content_to_json)

		fecha = datetime.strptime(new_server['fecha_hora'],'%Y-%m-%d %H:%M:%S.%f')
		
		#################  CONEXION A LA BASE DE DATOS  ################
		#Create test.sqlite automatically
		engine = db.create_engine('sqlite:///testServers.sqlite')
		connection = engine.connect()
		metadata = db.MetaData()
		
		#####################  INSERTS EN LA BDD  #####################
		#Inserts en tabla SERVERS
		serversTab = db.Table('servers',metadata,autoload=True,autoload_with=engine)
		
		queryServer = db.insert(serversTab).values(
			ipaddress = new_server['ipaddress'],
			fecha_hora = fecha,
			arquitectura_proc = new_server['arquitectura_proc'],
			marca_proc = new_server['marca_proc'],
			nombre_so = new_server['nombre_so'],
			version_so = new_server['version_so']
			)
		ResultProxy = connection.execute(queryServer)
		#connection.commit()
		s=db.select([serversTab.c.id_serv]).where(serversTab.c.fecha_hora== fecha)
		for row in connection.execute(s):
			id_servidor=row['id_serv']
		
		#Inserts en tabla PROCESOS
		procesosTab = db.Table('procesos',metadata,autoload=True,autoload_with=engine)
		
		for proc in new_server['procesos']:
			queryProc = db.insert(procesosTab).values(
				ip_server = new_server['ipaddress'],
				fecha_hora = fecha,
				pid = proc['pid'],
				name = proc['name'],
				username = proc['username'],
				id_serv=id_servidor
				)
			ResultProxy = connection.execute(queryProc)
				
		#Inserts en tabla USUARIOS
		usersTab = db.Table('usuarios_activos',metadata,autoload=True,autoload_with=engine)
		
		for user in new_server['usuarios_activos']:
			queryUsers = db.insert(usersTab).values(
				ip_server = new_server['ipaddress'],
				fecha_hora = fecha,
				username = user['name'],
				pid = user['pid'],
				id_serv=id_servidor
				)
			ResultProxy = connection.execute(queryUsers)
		#connection.commit()
		
		###############################################################

	#	return 'received'	
		return Response(json.dumps(new_server), status=201, mimetype=mime_type)
	except Exception as e:
		print(e)
		msg_error = "Get Agent Status FAILED"
		response_error = {"ERROR": msg_error}
		return Response(json.dumps(response_error), status=400, mimetype=mime_type)
	
