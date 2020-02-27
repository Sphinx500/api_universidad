import web  # pip install web.py
import csv  # CSV parser
import json  # json parser
import app

'''
    URL: http://localhost:8080/alumnos?action=get&token=1234
'''


class Alumnos:

    app_version = "0.02"  # version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los datos

    def __init__(self):
        pass
    def GET(self):  # Método inicial o constructor de la clase
        try:
            datos=web.input()
            if datos['token']=="1234":
                if datos['action']=="get": #si corresponde a get
                    result2=self.actionGet(self.app_version,self.file)
                    return json.dumps(result2)
                elif datos['action']=="search":#si corresponde a busqueda
                    #TODO Revisar por que la indentacion no funciona
					matricula=datos['matricula']
					result2=self.actionSearch(self.app_version,self.file,matricula)
					return json.dumps(result2)
                elif datos['action']=="delete": #si corresponde a eliminacion
					matricula=datos['matricula']
					result2=self.actionDelete(self.app_version,self.file,matricula)
					return json.dumps(result2)
                else: #si la accion no corresponde
                    result2={}
                    result2['status']="not found"
                    return json.dumps(result2)
            else:
                result={}
                result['status']="Incorrecto"
                return json.dumps(result)
                   #si falta algun valor
        except Exception as e:
            result={}
            result['status']="faltan valores"
            return json.dumps(result)

#METODO PARA GET
@staticmethod
def actionGet(app_version,file):
    try:
        result=[]
        with open('static/csv/alumnos.csv','r') as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                result2 = {}  # Genera un diccionario por cada registro en el csv
                result2['matricula'] = row['matricula']  # obtiene la matricula y la agrega al diccionario
                result2['nombre'] = row['nombre']  # optione el nombre y lo agrega al diccionario
                result2['primer_apellido'] = row['primer_apellido']  # optiene el primer_apellido
                result2['segundo_apellido'] = row['segundo_apellido']  # optiene el segundo apellido
                result2['carrera'] = row['carrera']  # obtiene la carrera
                result.append(result2)  # agrega el diccionario generado al array alumnos
                result['alumnos'] = result  # agrega el array alumnos al diccionario result
            return result  # Regresa el diccionario generado
    except Exception as e:
        result={}
        result['version']=app_version
        result['status']="Falied"
        return json.dumps(result)

#METODO PARA BUSQUEDA
@staticmethod
def actionSearch(app_version,file,matricula):
    try:
        result=[]
        result2={}
        with open('static/csv/alumnos.csv','r') as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						if(matricula==row['matricula']): #busca si la matricula coincide
							print(matricula) #imprime la matricula que se busca
							result.append(row)
							result2['app_version']=app_version
							result2['status']="200 ok" #por si todo sale bien
							result2['alumnos']=result
							break
						else:
							result2={}
							result2['status']="matricula no encontrada"
        return result2
    except Exception as e: #por si nada sale bien
        result={}
        result['version']=app_version
        result['status']="Error"
        return json.dumps(result)

#METODO PARA ELIMINACION
def actionDelete(app_version,file,matricula):
		try:
				result=[]
				result2={}
				with open('static/csv/alumnos.csv','r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
					reader = csv.DictReader(csvfile)
					for row in reader:
						if(row['matricula']!=matricula):
							result2['app_version']=app_version
							result2['status']="200 ok"
							result.append(row)
							result2['alumnos']=result
				tam=(len(result))
				print(tam)
				with open('static/csv/alumnos.csv','w',newline='') as csvfile: 
					writer=csv.writer(csvfile)
					header=[]
					header.append("matricula")
					header.append("nombre")
					header.append("primer_apellido")
					header.append("segundo_apellido")
					header.append("carrera")
					writer.writerow(header)
					datos=[]
					for i in range(0,tam):
						datos.append(result[i]['matricula'])
						datos.append(result[i]['nombre'])
						datos.append(result[i]['primer_apellido'])
						datos.append(result[i]['segundo_apellido'])
						datos.append(result[i]['carrera'])
						writer.writerow(datos)
						datos=[]
				results=[]
				results2={}
				with open('static/csv/alumnos.csv','r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
					reader = csv.DictReader(csvfile)
					for row in reader:
						results.append(row)
						results2['app_version']=app_version
						results2['status']="200 ok"
						results2['alumnos']=result
				return results2  
		except Exception as e:
			result={}
			result['version']=app_version
			result['status']="ErrorD"
			return json.dumps(result)