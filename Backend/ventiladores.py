import mysql.connector
from flask import Flask, request, Response, render_template, jsonify

mydb=mysql.connector.connect(host="localhost",database="dispositivos",
user="root",password="")

app=Flask(__name__)

@app.route('/',methods=['GET'])
def Ventiladores():
    cursor=mydb.cursor()
    cursor.execute("select * from ventiladores;")
    resultados=cursor.fetchall()
    print(resultados)
    resultado={"ventiladores":[]}
    resultado["ventiladores"].append({"id":resultados[0][0]})
    resultado["ventiladores"].append({"estado":resultados[0][1]})
    resultado["ventiladores"].append({"conexion":resultados[0][2]})
    resultado["ventiladores"].append({"nombre":resultados[0][3]})
    resultado["ventiladores"].append({"velocidad":resultados[0][4]})
    resultado["ventiladores"].append({"timer":resultados[0][5]})
    resultado["ventiladores"].append({"sleep":resultados[0][6]})
    return resultado
    # return {'resultado':resultados}
    cursor.close()
    mydb.close()


if __name__=='__main__':
    app.run(debug=True)
   

'''
r=request.get('API')
print(r)
print(r.content)

r=request.post('API',data={'key':'value'})
print(r)
print(r.json())
class Vent:
    def __init__(self,estado,conexion,nombre='',velocidad='',timer='',sleep=''):
        self.estado=estado
        self.conexion=conexion
        self.nombre=nombre
        self.velocidad=velocidad
        self.timer=timer
        self.slepp=sleep
'''

