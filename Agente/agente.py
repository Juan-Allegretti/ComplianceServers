import platform
import requests
import sys
import psutil
import netifaces
import cpuinfo
from datetime import datetime


procesos = []
#url = 'http://192.168.1.111:8080/servers'
url = 'http://192.168.1.106:8080/servers'

#OBTENGO INFORMACION DEL PROCESADOR
arquitectura_proc=cpuinfo.get_cpu_info()['arch']
marca_proc=cpuinfo.get_cpu_info()['brand']

#OBTENGO INFORMACION DEL SO
nombre_so= str(platform.system())
version_so= str(platform.version())

#OBTENGO LA IP DEL SERVIDOR
def get_ip():	
	interfaces = netifaces.interfaces()
	for i in interfaces:
    		#print(i)	
    		if i == 'lo':
        		continue
    		iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    		if iface != None:
        		for j in iface:
            			return j['addr']
ipaddress = get_ip()

#myobj = {'Arq':arqui}

#OBTENGO INFORMACION DE LOS PROCESOS CORRIENDO
for proc in psutil.process_iter():
	try:
		
		infoProceso = proc.as_dict(attrs=['name','pid','username'])
		procesos.append(infoProceso)		
		
	except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
		pass

#OBTENGO USUARIOS ACTIVOS
usuarios_activos=[]
for i in psutil.users():
	usuarios_activos.append({'name':i.name, 'pid':i.pid})

#OBTENGO FECHA Y HORA
fecha_hora = str(datetime.now())

#POST

myproceso = {'arquitectura_proc':arquitectura_proc,
		'marca_proc':marca_proc,
		'nombre_so':nombre_so,
		'version_so':version_so,
		'ipaddress':ipaddress,
		'usuarios_activos':usuarios_activos,
		'procesos':procesos,
		'fecha_hora':fecha_hora
		}

x = requests.post (url, json=myproceso)

print(x.content)
