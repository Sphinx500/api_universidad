import web 
import app 
import csv 
import json 


class Alumnos:

    def __init__(self): 
        pass 

    def GET(self):
        try:
            data = web.input() 
            if data['token'] == "1234": 
                if data['action'] == 'get': 
                    result = self.actionGet() 
                    return json.dumps(result) 
                else:
                    result = {} 
                    result['status'] = "Command not found"
                    return json.dumps(result) 
            else:
                result = {} 
                result['status'] = "Invalid Token"
                return json.dumps(result) 
        except Exception as e:
            result = {} 
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result) 

    @staticmethod
    def actionGet():
        try:
            result = {} 
            result['status'] = "200 Ok" 
            file = 'static/csv/alumnos.csv' 
            with open(file,'r') as csvfile: 
                reader = csv.DictReader(csvfile) 
                alumnos = [] 
                for row in reader: 
                    fila = {} 
                    fila['matricula'] = row['matricula'] 
                    fila['nombre'] = row['nombre'] 
                    fila['primer_apellido'] = row['primer_apellido'] 
                    fila['segundo_apellido'] = row['segundo_apellido'] 
                    fila['carrera'] = row['carrera'] 
                    alumnos.append(fila) 
                result['alumnos'] = alumnos 
            return result 
        except  Exception as e:
            result = {}
            result['status'] = "Error"
            return result 

#TODO revisar el codigo 