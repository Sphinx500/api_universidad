import web
import app
import json
import csv

class Alumnos:
	file="/static/csv/alumnos.csv"
	version="1.0.0"
	def __init__(self):
		pass

	def GET(self):
		try:
			datos=web.input()
			if datos['token']=="1234": #revisa que el token este bien
				#PARA EL GET
				if datos['action']=="get": 
					resultAB=self.actionGet(self.version,self.file)
					return json.dumps(resultAB) #devuelve el resultAado del metodo
				#PARA EL SEARCH
				elif datos['action']=="search":
					matricula=datos['matricula']
					resultAB=self.actionSearch(self.version,self.file,matricula)
					return json.dumps(resultAB) #devuelve el resultAado del metodo
				#PARA INPUT(INSERTAR VALORES)
				elif datos['action']=="put": #funciona para insertar los valores y se especifican
					matricula=datos['matricula']
					nombre=datos['nombre']
					primer_apellido=datos['apellido1']
					segundo_apellido=datos['apellido2']
					carrera=datos['carrera']
					resultAB=self.actionInput(self.version,self.file,matricula,nombre,primer_apellido,segundo_apellido,carrera)
					return json.dumps(resultAB)#devuelve el resultAado del metodo
				#PARA ELIMINAR VALORES
				elif datos['action']=="delete":
					matricula=datos['matricula']
					resultAB=self.optiondelete(self.version,self.file,matricula)
					return json.dumps(resultAB) #devuelve el resultAado del metodo
				else: #POR SI EL COMANDO ESTA MAL
					resultAB={}
					resultAB['status']="Command not found"
					return json.dumps(resultAB)
			else: #por si el token es incorrecto
				resultA={}
				resultA['status']="Token incorrecto"
				return json.dumps(resultA)
		except Exception as e:
			resultA={}
			resultA['status']="Ingresa valores validos, revisa"
			return json.dumps(resultA)

#METODO PARA LA FUNCION GET
	@staticmethod
	def actionGet(version,file):
		try:
				resultA=[]
				resultAB={}
				with open('static/csv/alumnos.csv','r') as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader: #para recorrer los datos del archivo
						resultA.append(row)
						resultAB['version']=version
						resultAB['status']="200 ok" #indica que todo salio bien
						resultAB['alumnos']=resultA
				return resultAB 
		except Exception as e: #Por si algo sale mal
			resultA={}
			resultA['version']=version
			resultA['status']="ErrorG"
			return json.dumps(resultA)
	
#METODO PARA LA FUNCION SEARCH
	@staticmethod
	def actionSearch(version,file,matricula):
		try:
				resultA=[]
				resultAB={}
				with open('static/csv/alumnos.csv','r') as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						if(matricula==row['matricula']): #compara la matricula ingresada con los datos del csv
							print(matricula)
							resultA.append(row) #devuelve los datos si encuentra una coincidencia
							resultAB['version']=version
							resultAB['status']="200 ok"#por si todo sale bien
							resultAB['alumnos']=resultA
							break
						else:
							resultAB={}
							resultAB['status']="matricula no encontrada" #por si no se encuentra 
				return resultAB 
		except Exception as e: #Por si algo sale mal
			resultA={}
			resultA['version']=version
			resultA['status']="ErrorS"
			return json.dumps(resultA)


#METODO PARA LA FUNCION DE INPUT
	@staticmethod
	def actionInput(version,file,matricula,nombre,primer_apellido,segundo_apellido,carrera):
		try:
			resultA=[]
			resultAIN=[] #lista que sirve para que los datos introducidos vayan cayendo ahi
			resultAB={}
			resultAIN.append(matricula)
			resultAIN.append(nombre)
			resultAIN.append(primer_apellido)
			resultAIN.append(segundo_apellido)
			resultAIN.append(carrera)
			with open('static/csv/alumnos.csv','a',newline='') as csvfile: 
				writer=csv.writer(csvfile)
				# The writerow() method writes a row of data into the specified file
				writer.writerow(resultAIN)
			with open('static/csv/alumnos.csv','r') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					resultA.append(row)
					resultAB['version']=version
					resultAB['status']="200 ok" #si todo sale bien
					resultAB['alumnos']=resultA
			return resultAB 
		except Exception as e:
			resultA={} #si algo falla
			resultA['version']=version
			resultA['status']="Error"
			return json.dumps(resultA)

	