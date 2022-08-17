import mysql.connector
from flask import Flask, request, Response, render_template, jsonify

mydb=mysql.connector.connect(host="localhost",database="dispositivos",
user="root",password="")

app=Flask(__name__)

@app.route('/',methods=['GET','UPDATE'])
def Ventiladores():
    cursor=mydb.cursor()
    cursor.execute("select conexion from ventiladores;")
    resultado=cursor.fetchall()
    print(resultado)
    cursor.close()
    mydb.close()
    return {'VENTILADORES':resultado}

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

